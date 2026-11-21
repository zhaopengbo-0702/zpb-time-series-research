from pathlib import Path, PurePosixPath
import hashlib, io, json, os, subprocess, tarfile, urllib.request

root = Path.cwd()
manifest = json.loads((root / 'sources.lock.json').read_text())
selected = {'TimeSeriesLibrary-ZJ', 'tsai', 'neuralforecast', 'pytorch-forecasting', 'darts'}
for source in manifest['sources']:
    if source['name'] not in selected:
        continue
    print('Downloading pinned source: ' + source['name'], flush=True)
    request = urllib.request.Request(source['archive_url'], headers={'User-Agent':'zpb-pinned-source-import'})
    with urllib.request.urlopen(request, timeout=180) as response:
        archive_bytes = response.read()
    assert hashlib.sha256(archive_bytes).hexdigest() == source['archive_sha256']
    expected = {e['path']: e for e in source['files']}
    seen = set()
    with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode='r:gz') as archive:
        for member in archive:
            assert not member.issym() and not member.islnk()
            if member.isdir():
                continue
            assert member.isfile()
            parts = PurePosixPath(member.name).parts[1:]
            assert parts and not any(p in ('.','..','.git') for p in parts)
            relative = source['local_directory'] + '/' + '/'.join(parts)
            assert relative in expected and relative not in seen
            content = archive.extractfile(member).read()
            entry = expected[relative]
            assert len(content) == entry['size_bytes']
            assert hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest() == entry['git_blob_sha1']
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
            target.chmod(0o755 if entry['mode']=='100755' else 0o644)
            seen.add(relative)
    assert seen == set(expected)
    print(source['name'] + ': verified ' + str(len(seen)) + ' files', flush=True)
subprocess.run(['python','-B','tools/verify_sources.py','--strict'], check=True)
files = [e for s in manifest['sources'] for e in s['files']]
subprocess.run(['git','-c','core.autocrlf=false','add','-f','--pathspec-from-file=-','--pathspec-file-nul'],
    input=b'\0'.join(e['path'].encode() for e in files)+b'\0', check=True)
data = ''.join(e['mode']+' '+e['git_blob_sha1']+'\t'+e['path']+'\n' for e in files).encode()
subprocess.run(['git','update-index','--index-info'], input=data, check=True)
tree = subprocess.check_output(['git','write-tree'], text=True).strip()
print('Imported source tree: ' + tree, flush=True)
