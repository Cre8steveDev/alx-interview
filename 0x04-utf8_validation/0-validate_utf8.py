#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Number of bytes in the current
     UTF-8 character"""
    num_bytes = 0

    for num in data:
        # Mask to keep only the least significant 8 bits
        num = num & 0xFF
        """ Check if the current number is a
          valid UTF-8 start byte"""
        if num_bytes == 0:
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7) != 0:
                return False
        else:
            """ Check if the current number is a
               valid UTF-8 continuation byte"""
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
