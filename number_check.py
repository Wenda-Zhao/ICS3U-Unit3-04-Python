#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program guessing random number


import random


def main():
    # this function is number check

    # input
    your_number = int(input("Enter your number: "))
    print("")

    # process
    if your_number > 0:
        # output
        print(" + ")
    # process
    elif your_number == 0:
        # output
        print(" 0 ")
    # process
    else:
        # output
        print(" - ")

    print("")
    print("Done!")


if __name__ == "__main__":
    main()
