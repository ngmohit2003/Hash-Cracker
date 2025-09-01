import getpass
import hashlib
import os

# Get the absolute path to the project root (i.e., CrackSuite/)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct path to samples/hashes.txt
hashes_file_path = os.path.join(project_root, "samples", "hashes.txt")

# Get password and compute MD5 hash
password = getpass.getpass("Enter your password: ")
hash = hashlib.md5(password.encode()).hexdigest()
print("Hash of password:", hash)

# Append the hash to the file
with open(hashes_file_path, "a") as f:
    f.write(hash + "\n")

