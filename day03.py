#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aocutil import print_results


def conv_char(c):
    return ord(c) - (96 if c >= "a" else 38)


def parse_func(lines):
    for line in lines:
        line = [conv_char(c) for c in line]
        split = len(line) // 2
        yield line[:split], line[split:]


def compartment_intersect(lines):
    for line in lines:
        c0 = set(line[0])
        c1 = set(line[1])
        yield c0.intersection(c1)


def results_1(lines):
    return sum(map(sum, compartment_intersect(lines)))


def run():
    print_results("data/day03test.txt", results_1, parse_func=parse_func, expected=157)
    print_results("data/day03.txt", results_1, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
