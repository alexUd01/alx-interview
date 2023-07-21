#!/usr/bin/python3
"""A script that reads `stdin` line by line and computes metrics:

INSTRUCTIONS:
- Input format:
  `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
  code> <file size>`
  NOTE: if the format is not like above, the line must be skipped

- After every 10 lines and/or a keyboard interruption (CTRL + C), print
  these statistics from the beginning:
  - Total file size: `File size: <total size>`
  - Where `<total size>` is the sum of all previous `<file size>`
  - Number of lines by status code:
    - possible status code: `200`, `301`, `400`, `401`, `403`, `404`,
      `405` and `500`
    - if a status code doesn’t appear or is not an integer, don’t print
      anything for this status code
    - format: `<status code>: <number>`
    - status codes should be printed in ascending order
"""
import sys

codes = [200, 301, 400, 401, 403, 404, 405, 500]


def valid_line(lst):
    """ Validates the simulated log lines """
    if len(lst) != 9:
        return False
    if len(lst[0].split('.') != 4):
        return False  # Invalid ip adress
    try:
        file_size = int(lst[-1])
        status_code = int(lst[-2])
        if status_code not in codes:
            return False
    except ValueError:
        return False
    else:
        return True


def compute_stat(line):
    """ Compute and print statistics """
    lst = line.split()
    if not valid_line(lst):
        return None, None
    file_size = int(lst[-1].rstrip())
    code = int(lst[-2])
    return file_size, code


def print_stat(size, code_list):
    """ Prints computed stats """
    print("File size: {:d}".format(size))
    temp = list(set(code_list))
    for code in sorted(temp):
        print("{}: {}".format(code, code_list.count(code)))


if __name__ == "__main__":

    total_file_size = 0
    code_list = []
    count = 0

    try:
        for log_line in sys.stdin:
            count += 1
            if count <= 10:
                file_size, code = compute_stat(log_line)
                if file_size is None and code is None:
                    continue
                total_file_size += file_size
                code_list.append(code)
            if count == 10:
                print_stat(total_file_size, code_list)
                count = 0
    finally:
        print_stat(total_file_size, code_list)
