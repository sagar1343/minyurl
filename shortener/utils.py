import random
import string
import hashlib
import base62

from django.conf import settings


def get_random_code():
    """
    generates random CODE_LENGTH string
    """
    code = "".join(
        random.choices(
            string.ascii_letters + string.digits, k=settings.SHORT_CODE_LENGTH
        )
    )
    return code


def generate_md5_hash_code(url):
    """
    generates code using md5 hash
    """
    m = hashlib.md5()
    m.update(str(url).encode())
    hash = m.digest().hex()
    return hash[: settings.SHORT_CODE_LENGTH]


def convert_to_base_62(number):
    """
    convert id to bas62 encoding
    """
    return base62.encode(number)
