#!/usr/bin/env python3
"""The auth script"""

import bcrypt
from uuid import uuid4
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


def _generate_uuid() -> str:
    """This method returns a tring representation of a new UUID.

    Returns:
        str: String representation of a new UUID."""
    id = uuid4()
    return str(id)


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

    def valid_login(self, email: str, password: str) -> bool:
        """A method that validates the password of a user.

        Args:
            email (str): the user's email.
            passsword (str): the user's password as a string.
        Returns:
            bool: True is password matches, False if otherwise.
            """
        try:
            user = self._db.find_user_by(email=email)

            if user:
                user_h_pwd = user.hashed_password
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user_h_pwd)
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """This method creates a new session for a user.
        Args:
            email (str): The user's email.
        Returns:
            str: The session ID.
        Raises:
            ValueError: If the user is not found."""
        try:
            user = self._db.find_user_by(email=email)
            user_sess_id = _generate_uuid()
            self._db.update_user(user.id, session_id=user_sess_id)
            return user.session_id
        except NoResultFound:
            raise ValueError("User not found")

    def get_user_from_session_id(self, session_id: str) -> User | None:
        """This method finds a user using the session id.

        Args:
        session_id (str): The session id.

        Returns:
            User | None: The method returns the user of none.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """This method destroys a user's session.

        Args:
        """
        return
