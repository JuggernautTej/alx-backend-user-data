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
    """ Redacting Formatter class for filtering PII in logs"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        """Initializes the class
        Args:
            fields: A list of fields."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """This method filters the incoming log records using filter_datum
        Args:
            record (logging.LogRecord): The log record to be formatted.
        Returns:
            A string of the formated log message with redaction implemented"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)
