#!/usr/bin/env python3
"""This houses the personal information data task"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """A function that returns the log message obfuscated."""
    patn = "({})=.*?{}".format('|'.join(fields), separator)
    return re.sub(patn, r"\1={}".format(redaction) + separator, message)
