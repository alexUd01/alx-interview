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


def valid_line(lst):
    """ Validates the simulated log lines """
    if len(lst) != 11:
        return False
    try:
        x = int(lst[-1])
        x = int(lst[-2])
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
    for code in set(sorted(code_list)):
        print("{}: {}".format(code, code_list.count(code)))


if __name__ == "__main__":

    total_file_size = 0
    code_list = []
    count = 0

    try:
        for log_line in sys.stdin:
            file_size, code = compute_stat(log_line)
            if file_size is None:
                continue
            total_file_size += file_size
            code_list.append(code)
            count += 1
            if count % 10 == 0:
                print_stat(total_file_size, code_list)
    except KeyboardInterrupt:
        pass
    finally:
        print_stat(total_file_size, code_list)
