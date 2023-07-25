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
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False


if __name__ == "__main__":
    import random

    def generate_random_integer_list(length):
        return [random.randint(0, 255) for _ in range(length)]

    # Example usage:
    random_list = generate_random_integer_list(2)
    print(random_list)
    print(validUTF8(random_list))
