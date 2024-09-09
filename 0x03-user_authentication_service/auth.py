#!/usr/bin/env python3
"""The auth script"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes passwords using bcrypt

    Args:
        password (str): the password as a string.
    Returns:
        bytes: The salted hash of the password."""
    # Convert the password from string to bytes
    pwd_bytes = password.encode('utf-8')
    # generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_pwd
