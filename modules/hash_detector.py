def detect_hash_type(hash_value):
    if len(hash_value) == 32:
        return "MD5"
    elif len(hash_value) == 40:
        return "SHA1"
    elif len(hash_value) == 64:
        return "SHA256"
    elif hash_value.startswith("$2b$") or hash_value.startswith("$2a$"):
        return "bcrypt"
    else:
        return "Unknown"



