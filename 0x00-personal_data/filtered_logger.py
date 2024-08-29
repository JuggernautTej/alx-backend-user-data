#!/usr/bin/env python3
"""This houses the personal information data task"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """A function that returns the log message obfuscated."""
    patn = "({})=.*?{}".format('|'.join(fields), separator)
    return re.sub(patn, r"\1={}".format(redaction) + separator, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        """Initializes the class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """This method filters the incoming log records using filter_datum"""
        source = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            source, self.SEPARATOR)
