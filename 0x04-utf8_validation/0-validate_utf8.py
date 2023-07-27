#!/usr/bin/python3
"""
UTF-8 Validation module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers representing the data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    num_bytes = 0

    for num in data:
        # Check if the current number is a continuation byte
        if num_bytes == 0 and (num & 0x80) == 0x80:
            return False

        # If it's the start of a new character, determine the number of bytes
        if num_bytes == 0:
            if (num & 0b11110000) == 0b11110000:
                num_bytes = 3
            elif (num & 0b11100000) == 0b11100000:
                num_bytes = 2
            elif (num & 0b11000000) == 0b11000000:
                num_bytes = 1
            elif (num & 0b10000000) == 0b10000000:
                return False
        else:
            # Check if the current number is a continuation byte
            if (num & 0b11000000) != 0b10000000:
                return False

            num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32,
            105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
