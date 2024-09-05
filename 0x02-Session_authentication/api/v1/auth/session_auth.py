#!/usr/bin/env python3
"""This contains the SessionAuth class"""

from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """The session class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """A method that creates a Session ID for
        user_id.
        Args:
            user_id (str): The user id.
        Returns:
            The session id as a string or none."""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """This method returns a user id based on the session id.
        Args:
            session_id (str): The session_id.
        Returns:
            str: The user id as a string."""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
