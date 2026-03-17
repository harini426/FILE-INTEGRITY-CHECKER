import hashlib

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

file = "sample.txt"
current_hash = calculate_hash(file)

if current_hash:
    print("-" * 30)
    print(f"File Hash: {current_hash}")
    print("-" * 30)
else:
    print("Error: sample.txt file-ai kaanom!")