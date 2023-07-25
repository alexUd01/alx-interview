#!/usr/bin/python3
""" A module that contains a method that determines if a given data set
represents a valid UTF-8 encoding.

INSTRUCTIONS:
- PROTOTYPE: def validUTF8(data)
- Return: `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle
  the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Check if the given data represents a valid UTF-8 encoding.

    Args:
    data (list[int]): A list of integers representing 1-byte data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, False otherwise.
    """

    if not isinstance(data, list):
        return False

    def is_valid_code_point(code_point):
        # Check if the code point is within valid Unicode range
        if (0xD800 <= code_point <= 0xDFFF) or (0xFDD0 <= code_point <= 0xFDEF):
            return False
        return code_point <= 0x10FFFF

    def is_overlong_encoding(byte_count, code_point):
        # Check for overlong encodings (UTF-8 characters represented with more bytes than necessary)
        return (
            (byte_count == 1 and code_point <= 0x7F)
            or (byte_count == 2 and code_point <= 0x7FF)
            or (byte_count == 3 and code_point <= 0xFFFF)
            or (byte_count == 4 and code_point <= 0x10FFFF)
        )

    idx = 0
    while idx < len(data):
        first_byte = data[idx]

        if first_byte < 0x80:  # 1 byte encoding (regular ASCII characters)
            idx += 1
            continue

        # Find the number of bytes in the UTF-8 character
        if first_byte & 0xE0 == 0xC0:  # 2 bytes
            byte_count = 2
            code_point = first_byte & 0x1F
        elif first_byte & 0xF0 == 0xE0:  # 3 bytes
            byte_count = 3
            code_point = first_byte & 0x0F
        elif first_byte & 0xF8 == 0xF0:  # 4 bytes
            byte_count = 4
            code_point = first_byte & 0x07
        else:
            # Invalid UTF-8 start byte
            return False

        idx += 1

        # Check continuation bytes
        for i in range(byte_count - 1):
            if idx >= len(data):
                return False

            cont_byte = data[idx]
            if cont_byte & 0xC0 != 0x80:  # Continuation byte must start with '10'
                return False

            code_point = (code_point << 6) | (cont_byte & 0x3F)
            idx += 1

        if not is_valid_code_point(code_point) or is_overlong_encoding(byte_count, code_point):
            return False

    return True

