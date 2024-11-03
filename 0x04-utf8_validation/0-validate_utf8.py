#!/usr/bin/python3
"""There are no modules to be imported."""


def validUTF8(data):
    """Check for utf-8 encoding validity."""
    num_bytes = 0

    for num in data:
        binary = bin(num)[2:].zfill(8)

        if num_bytes == 0:
            if binary.startswith('0'):
                continue
            elif binary.startswith('110'):
                num_bytes = 1
            elif binary.startswith('1110'):
                num_bytes = 2
            elif binary.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            if not binary.startswith('10'):
                return False
            num_bytes -= 1

    return num_bytes == 0
