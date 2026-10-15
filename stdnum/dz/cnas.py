# cnas.py - functions for handling Algerian CNAS employer identifiers
# coding: utf-8

"""CNAS employer identifier, Algeria.

This module implements a structural check for the 12-digit employer number
format cited in Algerian administrative/statistical documentation. It does
not validate an insured person's personal affiliation number, confirm
issuance, or verify an employer against CNAS records.

>>> validate('123456789012')
'123456789012'
>>> is_valid('12345678901')
False
>>> is_valid('12345678901X')
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
    """Validate the 12-digit CNAS employer-number structure."""
    number = compact(number)
    if len(number) != 12:
        raise InvalidLength()
    if not isdigits(number):
        raise InvalidFormat()
    return number


def is_valid(number):
    """Return whether the number has a valid structural form."""
    try:
        return bool(validate(number))
    except ValidationError:
        return False


def format(number):
    """Return the compact representation of the number."""
    return compact(number)
