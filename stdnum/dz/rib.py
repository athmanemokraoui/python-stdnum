# rib.py - functions for handling Algerian bank account identifiers
# coding: utf-8

"""Algerian RIB (Relevé d'Identité Bancaire) account identifier.

The identifier is 20 characters: 3 bank-code characters, 5 branch-code
characters, 10 account characters and a 2-character control key. The official
appendix describes a Modulo 97 check using the branch code and account number.
Alphabetic account characters are mapped A=1, ..., I=9, J=1, ..., R=9,
S=1, ..., Z=8 for the calculation only.

The appendix wording refers to a 3-character branch code, whereas Article 3
specifies a 5-character branch code. The published example
00100325030000134050 is consistent with using all 5 branch-code characters.
This implementation follows that example; confirm with the issuing bank for
edge cases before relying on it for payment processing.

>>> validate('00100325030000134050')
'00100325030000134050'
>>> is_valid('00100325030000134050')
True
>>> is_valid('00100325030000134051')
False
>>> validate('001 00325 0300001340 50')
'00100325030000134050'
>>> is_valid('00100325ABC00134050')
False
>>> is_valid('00100325-30001340500')
False
>>> is_valid('short')
False
>>> format('001 00325 0300001340 50')
'00100325030000134050'
>>> _account_digits('AB')
'12'
>>> _account_digits('JKLMNOPQR')
'123456789'
>>> _account_digits('STUVWXYZ')
'12345678'
>>> try:
...     _account_digits('A-')
... except InvalidFormat:
...     print('invalid')
invalid
"""

from stdnum.exceptions import *  # noqa: F401,F403
from stdnum.util import clean, isdigits


def compact(number):
    """Remove spaces and normalize account letters to uppercase."""
    return clean(number, ' ').upper()


def _account_digits(account):
    """Convert account letters according to the official appendix."""
    out = []
    for char in account:
        if char.isdigit():
            out.append(char)
        elif 'A' <= char <= 'Z':
            out.append(str((ord(char) - ord('A')) % 9 + 1))
        else:
            raise InvalidFormat()
    return ''.join(out)


def _check_key(number):
    """Return the expected control key from branch code and account."""
    base = number[3:8] + _account_digits(number[8:18])
    return 97 - (int(base + '00') % 97)


def validate(number):
    """Validate the RIB structure and Modulo 97 control key."""
    number = compact(number)
    if len(number) != 20:
        raise InvalidLength()
    if not isdigits(number[:8] + number[18:]) or not all(
            char.isdigit() or 'A' <= char <= 'Z' for char in number[8:18]):
        raise InvalidFormat()
    key = int(number[18:20])
    if not 1 <= key <= 97:
        raise InvalidChecksum()
    base = number[3:8] + _account_digits(number[8:18]) + number[18:20]
    if int(base) % 97 != 0 or key != _check_key(number):
        raise InvalidChecksum()
    return number


def is_valid(number):
    """Return whether the RIB structure and control key are valid."""
    try:
        return bool(validate(number))
    except ValidationError:
        return False


def format(number):
    """Return the compact representation of the RIB."""
    return compact(number)
