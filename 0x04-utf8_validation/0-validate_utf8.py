#!/usr/bin/python3
"""There are no modules to be imported."""


def validUTF8(data):
    """Check for utf-8 encoding validity."""
    new = []
    bit = []
    pool = []

    if data == []:
        return True

    if data[0] == 0:
        for i in data:
            temp = 0
            if data[i] == temp:
                new.append(data[i])

        if len(data) == len(new):
            return True

    for j in range(len(data)):
        binary = ""
        while data[j] > 0:
            binary = str(data[j] & 1) + binary
            data[j] = data[j] >> 1

        if len(binary) < 8:
           binary = binary.zfill(8)

        bit.append(binary)

    for k in range(len(bit)):
        if int(bit[k][:5]) == 11110:
            temp1 = 11110
            temp2 = 3
        elif int(bit[k][:4]) == 1110:
            temp1 = 1110
            temp2 = 2
        elif int(bit[k][:3]) == 110:
            temp1 = 110
            temp2 = 1
        elif int(bit[k][:1]) == 0:
            pool.append(True)
            temp2 = 0

        for l in range(k + 1, (k + 1) + temp2):
            if temp1 == 11110 and len(bit[k + 1 : k + 4]) == 3:
                if int(bit[l][:2]) == 10:
                    continue
            elif temp1 == 1110 and len(bit[k + 1 : k + 3]) == 2:
                if int(bit[l][:2]) == 10:
                    continue
            elif temp1 == 110 and len(bit[k + 1 : k + 2]):
                if int(bit[l][:2]) == 10:
                    continue
            else:
                pool.append(False)

    for m in range(len(pool)):
        if pool[m] == False:
            return False

    return True
