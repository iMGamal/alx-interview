def validUTF8(data):
    """Check if the data is a valid UTF-8 encoding."""
    num_bytes = 0  # Tracks the expected number of continuation bytes

    for num in data:
        # Check if `num` is within the valid byte range
        if num < 0 or num > 255:
            return False
        
        # If we are expecting continuation bytes
        if num_bytes > 0:
            # Check if the byte starts with '10' (continuation byte)
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1
        else:
            # Determine the number of bytes in the UTF-8 character
            if (num >> 7) == 0b0:
                num_bytes = 0  # 1-byte character
            elif (num >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (num >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (num >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8 character start

    # All characters should be complete by the end
    return num_bytes == 0
