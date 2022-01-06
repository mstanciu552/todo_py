#!/usr/bin/env python3
import sys

from utils import help
from todos import show, add, deltodo, completed


def handle_args(args):
    if len(args) == 0 or args[0] == "show":
        show()
    elif args[0] == "add":
        assert len(args) >= 2, "Missing arg 1"
        add(args[1], (args[2] if len(args) >= 3 else None))
    elif args[0] == "del":
        assert args[1], "Missing arg 1"
        deltodo(args[1])
    elif args[0] == "completed":
        assert args[1], "Missing arg 1"
        completed(args[1])
    elif args[0] == "help":
        help()


def main():
    handle_args(sys.argv[1:])


if __name__ == "__main__":
    main()
