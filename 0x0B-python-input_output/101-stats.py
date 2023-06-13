#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C), prints the following statistics:
Total file size up to that point.
Count of read status codes up to that point.
"""

import sys

def print_metrics(total_size, status_codes):
    """Print accumulated metrics.
    Args:
    size (int): The accumulated read file size.
    status_codes (dict): The accumulated count of status codes.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = {}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            ip, _, _, status_code, file_size = line.split()
            total_size += int(file_size)
            if status_code not in status_codes:
                status_codes[status_code] = 0
            status_codes[status_code] += 1

            if count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
