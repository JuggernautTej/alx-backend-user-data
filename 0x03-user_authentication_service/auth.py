#!/usr/bin/env python3
"""The auth script"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        """Initializes instance of DB"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """This method registers a new user.
        Args:
            email (str): the email address of the user.
            password (str): the user password.
        Returns:
            User: The newly created user.
        Raises:
            ValueError: If the user exists with the given email."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
        new_user = self._db.add_user(email, hashed_password)
        return new_user
