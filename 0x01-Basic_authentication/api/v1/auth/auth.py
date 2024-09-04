#!/usr/bin/env python3
"""COntains the class to manage the
API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """This is the class that manages authentication"""
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """This method checks for authentication
        requirements.
        Args:
            path : A string that represents a path.
            excluded_paths : A list of strings of
            excluded paths.
        Returns:
            A boolean"""
        return False

    def authorization_header(self, request=None) -> str:
        """A public method"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method"""
        return request
