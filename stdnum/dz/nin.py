
# nin.py - functions for handling Algeria NIN numbers
# coding: utf-8
#
# Copyright (C) 2026
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, see <https://www.gnu.org/licenses/>.

"""NIN, Numéro d'Identification National, Algeria.

The NIN is the Algerian national identification number.

The documented structure consists of 18 numeric digits.

This module performs structural validation only. It does not verify the
control key, establish whether a number has been issued, or confirm the
identity of its holder.

>>> validate('123456789012345678')
'123456789012345678'
>>> validate('123 456 789 012 345 678')
'123456789012345678'
>>> validate('12345')
Traceback (most recent call last):
    ...
InvalidLength: ...
>>> validate('X23456789012345678')
Traceback (most recent call last):
    ...
InvalidFormat: ...
>>> format('123 456 789 012 345 678')
'123456789012345678'
"""

from __future__ import annotations

from stdnum.exceptions import *
from stdnum.util import clean, isdigits


def compact(number: str) -> str:
    """Convert the number to the minimal representation.

    This strips the number of spaces and surrounding whitespace.
    """
    return clean(number, ' ')


def validate(number: str) -> str:
    """Check the structure of an Algerian NIN.

    This checks that the compacted number contains exactly 18 digits.
    It does not verify the control key or the actual issuance of the NIN.
    """
    number = compact(number)
    if len(number) != 18:
        raise InvalidLength()
    if not isdigits(number):
        raise InvalidFormat()
    return number


def is_valid(number: str) -> bool:
    """Check whether the number has the expected NIN structure."""
    try:
        return bool(validate(number))
    except ValidationError:
        return False


def format(number: str) -> str:
    """Return the compact representation of the NIN."""
    return compact(number)
