import os, subprocess

with open('engpc', 'rb') as f:
    data = f.read()
print(f"engpc size: {len(data)} bytes")

with open('payload', 'wb') as f:
    f.write(data)

os.chmod('payload', 0o755)

subprocess.run(['setfattr', '-n', 'security.selinux',
    '-v', 'u:object_r:engpc_exec:s0',
    'payload'], check=False)

r = subprocess.run(['getfattr', '-n', 'security.selinux',
    'payload'], capture_output=True, text=True)
print(f"Label: {r.stdout}")

os.system('tar --xattrs --xattrs-include=security.selinux -czf payload.tar.gz payload')
print("Done!")
