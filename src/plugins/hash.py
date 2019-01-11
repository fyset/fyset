import hashlib
import os


def generate_hash(source: str):
    return hashlib.sha256(
        (source + str(os.environ.get('SECRET'))).encode('utf-8')
    ).hexdigest()
