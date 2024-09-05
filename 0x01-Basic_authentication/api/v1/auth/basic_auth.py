#!/usr/bin/env python3
"""Contains the BasicAuth class"""

from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """This is the BasicAuth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """This method returns Base64 part of the
        authorization header for a basic authentication.
        Args:
            authorization_header: The Authorization
            header from the request as a string.
        Returns:
            A string as the Base64 part of the Authorization
            header or None if invalid."""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        # check if the authorization_header starts with
        # "Basic "
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """This method returns the decoded value of the
        Base64 string.
        Args:
            base64_authorization_header: The Authorization header
            as a string.
        Returns:
            A string as the Base64 part of the Authorization
            header or None if invalid.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(encoded)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """This method returns the user email and password
        from rhe Base64 decoded value.
        Args:
            decoded_base64_authorization_header: The Authorization header
            as a string.
        Returns:
            Tuple (str, str): Two values, the email and password, as strings.
            """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """This method returns the User instance based on email and
        password.
        Args:
            user_email (str): The user email.
            user_pwd (str): The user password.
        Returns:
            User instance."""
        if user_email is None:
            return None
        if user_pwd is None:
            return None
        try:
            users = User.search({'email': user_email})
            if not users or users == []:
                return None
            # Validate is password supplied is the password for the
            # user in question
            for user in users:
                if not user.is_valid_password(user_pwd):
                    return None
                return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """This method overloads Auth and retrieves the User Instance
        for a request.
        Args:
            request: The Flask request object.
        Returns:
            User instance or None if no valid user is found."""
        # Authorization header retrieval from the request
        auth_header = self.authorization_header(request)
        if auth_header is not None:
            # Extraction of the Base64 part of the Authorization header
            base64_p = self.decode_base64_authorization_header(auth_header)
            if base64_p is not None:
                # Decode the Base64 Authorization header
                decoded_p = self.decode_base64_authorization_header(base64_p)
                if decoded_p is not None:
                    # Extraction of user email and password from
                    # the decoded string
                    email, password = self.extract_user_credentials(decoded_p)
                    if email is not None or password is not None:
                        # Retrieval of User instance based on email
                        # and password
                        user = self.user_object_from_credentials(email,
                                                                 password)
                        return user
        return None
