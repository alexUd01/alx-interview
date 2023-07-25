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
    """ The function """
    assert type(data) is list

    if data[0] < 128:  # 1 byte encoding (regular ACSII characters)
        for item in data:
            if not item < 128:
                return False
        else:
            return True
    else:  # More than 1 byte encoding
        first_byte = bin(data[0])[2:]
        try:
            expected_nb_bytes = first_byte.index('0')
        except IndexError:
            return False
        else:
            if expected_nb_bytes > 6:  # Maximum possible bit reached
                return False
            if len(data) != expected_nb_bytes:
                return False
            # Evaluate the remaining items on the list
            for i in range(1, len(data)):  # Start iteration from the 2nd item
                bin_repr = bin(data[i])[2:]
                if bin_repr.find('0') != 1:  # Cont. bytes must be 10xxxxxx
                    return False
            else:
                return True
    return False
