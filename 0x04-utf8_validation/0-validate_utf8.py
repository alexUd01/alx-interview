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


def to_bin(n):
    """ Converts integers to binary representation """
    return bin(n)[2:]


def validUTF8(data):
    """ The function """
    assert type(data) is list

    if data[0] < 128:  # 1 byte encoding (regular ACSII characters)
        for item in data[1:]:
            if item >= 128:
                return False
        return True
    else:  # More than 1 byte encoding
        first_byte = to_bin(data[0])
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
                bin_repr = to_bin(data[i])
                if bin_repr[0:2] != '10':  # Cont. bytes must be 10xxxxxx
                    return False
            return True


if __name__ == "__main__":
    import random

    def generate_random_integer_list(length):
        return [random.randint(0, 255) for _ in range(length)]

    # Example usage:
    random_list = generate_random_integer_list(2)
    print(random_list)
    print(validUTF8(random_list))
