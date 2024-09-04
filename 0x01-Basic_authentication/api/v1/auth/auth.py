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
        if path is None or path == '' or not path:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        # Time to normalize all paths in excluded_paths
        mod_paths = []
        for x in excluded_paths:
            if not x.endswith('/'):
                mod_paths.append(x + '/')
            else:
                mod_paths.append(x)
        excluded_paths = mod_paths
        # CHeck if  path starts with any exclude path
        # or vice versa
        for e_path in excluded_paths:
            if e_path.startswith(path):
                return False
            if path.startswith(e_path):
                return False
            if e_path.endswith("*"):
                if path.startswith(e_path[:-1]):
                    return False

        if path in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> str:
        """A public method"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method"""
        return request
