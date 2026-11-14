"""A tiny to-do list. Names are always compared case-insensitively."""

import sys

items = []


def add(name):
    items.append(name)


def show():
    for name in items:
        print(name)


COMMANDS = {"add": add, "show": show}


def run(lines):
    for line in lines:
        command, *args = line.split()
        COMMANDS[command](*args)


if __name__ == "__main__":
    run(sys.stdin)
