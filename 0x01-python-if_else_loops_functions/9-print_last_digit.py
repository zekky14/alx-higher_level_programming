#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(x):
    """Print the last digit of a number and return it."""
    print(abs(x) % 10, end="")
    return (abs(x) % 10)
