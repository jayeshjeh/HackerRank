# !/bin/python3

import math
import os
import random
import re
import sys


def calcu(a):
    if a % 2 != 0:
        print("Weird")
    elif a % 2 == 0 and 2 <= a <= 5:
        print("Not Weird")
    elif a % 2 == 0 and 6 <= a <= 20:
        print("Weird")
    else:
        print("Not Weird")


def main():
    n = 0
    n = int(input())

    calcu(n)


if __name__ == '__main__':
    main()
