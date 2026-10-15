# rc.py - functions for handling Algerian commercial register numbers
# coding: utf-8

"""RC (Registre du Commerce) number, Algeria.

The CNRC public portal shows the common 10-character pattern DD L DDDDDDD
(e.g. ``12A3456789``). This module validates that documented pattern only;
other historical or special registration forms may exist and should be
confirmed with CNRC before being treated as invalid.

>>> validate('12A3456789')
'12A3456789'
>>> validate('99A9999999')
'99A9999999'
>>> is_valid('1234567890')
False
>>> is_valid('12A345678X')
False
>>> format('12a3456789')
'12A3456789'
"""

import re

from stdnum.exceptions import *  # noqa: F401,F403
from stdnum.util import clean

_RC_RE = re.compile(r'^[0-9]{2}[A-Z][0-9]{7}$')


def compact(number):
    """Remove spaces and normalize the letter to uppercase."""
    return clean(number, ' ').upper()


def validate(number):
    """Validate the common 10-character RC structure."""
    number = compact(number)
    if len(number) != 10:
        raise InvalidLength()
    if not _RC_RE.fullmatch(number):
        raise InvalidFormat()
    return number


def is_valid(number):
    """Return whether the number matches the common RC structure."""
    try:
        return bool(validate(number))
    except ValidationError:
        return False


def format(number):
    """Return the normalized representation of the RC number."""
    return compact(number)
