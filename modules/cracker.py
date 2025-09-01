import hashlib
import bcrypt
from modules.hash_detector import detect_hash_type

def crack_hash(target_hash, wordlist_file):
    hash_type = detect_hash_type(target_hash)

    with open(wordlist_file, "r", encoding="latin-1") as file:
        for word in file:
            word = word.strip()
            if hash_type == "MD5":
                guess = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "SHA1":
                guess = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == "SHA256":
                guess = hashlib.sha256(word.encode()).hexdigest()
            elif hash_type == "bcrypt":
                if bcrypt.checkpw(word.encode(), target_hash.encode()):
                    return word
                continue
            else:
                return None

            if guess == target_hash:
                return word
    return None
