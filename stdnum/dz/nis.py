# nis.py - functions for handling Algerian statistical identifiers
# coding: utf-8

"""NIS (Numéro d'Identification Statistique), Algeria.

Structural validation only. The commonly documented main-establishment
identifier has 15 digits; a secondary establishment may use the 15-digit
identifier followed by a 3-digit sequence (18 digits). This does not confirm
issuance or current registration.

>>> validate('545154845112202')
'545154845112202'
>>> validate('545154845112202001')
'545154845112202001'
>>> is_valid('123')
False
>>> is_valid('12345678901234X')
False
>>> format('545154845112202')
'545154845112202'
"""

from stdnum.exceptions import *  # noqa: F401,F403
from stdnum.util import clean, isdigits


def compact(number):
    """Remove spaces from the number."""
    return clean(number, ' ')


def validate(number):
    """Validate the documented NIS length and numeric structure."""
    number = compact(number)
    if len(number) not in (15, 18):
        raise InvalidLength()
    if not isdigits(number):
        raise InvalidFormat()
    return number


def is_valid(number):
    """Return whether the number has a valid NIS structure."""
    try:
        return bool(validate(number))
    except ValidationError:
        return False


def format(number):
    """Return the compact representation of the NIS."""
    return compact(number)
