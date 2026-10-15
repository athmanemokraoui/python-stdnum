# casnos.py - functions for handling Algerian CASNOS identifiers
# coding: utf-8

"""CASNOS social security number, Algeria.

The social security number is structurally validated as exactly 12 digits.
This check does not establish whether the number was actually issued.

>>> validate('123456789012')
'123456789012'
>>> is_valid('123456789012')
True
>>> is_valid('12345678901')
False
>>> is_valid('1234567890123')
False
>>> is_valid('12345678901A')
False
>>> format('123 456 789 012')
'123456789012'
"""

from stdnum.exceptions import *  # noqa: F401,F403
from stdnum.util import clean, isdigits


def compact(number):
    """Remove spaces from the number."""
    return clean(number, ' ')


def validate(number):
    """Validate the 12-digit structural form."""
    number = compact(number)
    if len(number) != 12:
        raise InvalidLength()
    if not isdigits(number):
        raise InvalidFormat()
    return number


def is_valid(number):
    """Return whether the number has a valid structural form."""
    try:
        validate(number)
        return True
    except ValidationError:
        return False


def format(number):
    """Return the compact representation of the number."""
    return compact(number)
