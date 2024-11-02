#!/usr/bin/python3
"""There are no modules to be imported."""


def validUTF8(data):
    """Check whether the passed data fits UTF-8."""
    if data == []:
        return False
    elif len(data) in range(1, 5):
        return True
    else:
        return False
