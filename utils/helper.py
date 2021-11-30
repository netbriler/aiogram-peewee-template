import hashlib
from time import time


def generate_inline_id(query: str):
    return hashlib.md5(f'{query}{time()}'.encode()).hexdigest()
