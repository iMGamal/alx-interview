#!/usr/bin/python3
"""There are no modules to be imported."""


def validUTF8(data):
    """Check 2-byte and 1-byte representation of UTF-8."""
    new = []

    if data == []:
        return False

    for i in range(len(data)):
        if data[i] == 0:
            return False

        temp2 = data[i]
        b = ''

        while temp2 > 0:
            temp1 = temp2 % 2
            n = str(temp1)
            b += n
            temp2 = temp2 // 2

        s = b[::-1]
        if len(s) < 8:
            s = s.zfill(8)
        new.append(s)

    if int(new[0][:5]) == 11110 and
    len(new) >= 4:
        if int(new[1][:2]) == 10 and
        int(new[2][:2]) == 10 and
        int(new[3][:2]) == 10:
            return True
        else:
            return False
    elif int(new[0][:4]) == 1110 and
    len(new) >= 3:
        if int(new[1][:2]) == 10 and
        int(new[2][:2]) == 10:
            return True
        else:
            return False
    elif int(new[0][:3]) == 110 and
    len(new) >= 2:
        if int(new[1][:2]) == 10:
            return True
        else:
            return False
    elif int(new[0][:1]) == 0:
        return True
    else:
        return False
