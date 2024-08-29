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
    """ Redacting Formatter class for
    filtering PII data in log messages. """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with a list of fields to redact.

        Args:
            fields (List[str]): The list of fields
            to obfuscate in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        # Store the fields to be redacted.
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, filtering out sensitive information.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log message with
            redacted sensitive information.
        """
        # Obfuscate the sensitive fields in the log message.
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        # Format the log record using the parent class's format method.
        return super(RedactingFormatter, self).format(record)
