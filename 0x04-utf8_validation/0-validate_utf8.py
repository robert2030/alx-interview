#!/usr/bin/python3
"""
file: 0-validate_utf8.py

UTF-8 Validator
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Determines if a given data set represents a
        valid UTF-8 encoding.
    """
    i = 0
    while i < len(data):
        byte = data[i] & 0b11111111

        if byte >> 7 == 0:
            i += 1
        elif byte >> 5 == 0b110:
            if i + 1 < len(data) and data[i + 1] >> 6 == 0b10:
                i += 2
            else:
                return False
        elif byte >> 4 == 0b1110:
            if i + 2 < len(data) and data[i + 1] >> 6 == 0b10 and \
                    data[i + 2] >> 6 == 0b10:
                i += 3
            else:
                return False
        elif byte >> 3 == 0b11110:
            if i + 3 < len(data) and data[i + 1] >> 6 == 0b10 and \
                    data[i + 2] >> 6 == 0b10 and data[i + 3] >> 6 == 0b10:
                i += 4
            else:
                return False
        else:
            return False
    return True
