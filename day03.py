#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aocutil import print_results
from functools import reduce


def conv_char(c):
    return ord(c) - (96 if c >= "a" else 38)


def parse_func(lines):
    for line in lines:
        yield [conv_char(c) for c in line]


def results_intersect(lines, results_func):
    for line in results_func(lines):
        yield reduce(lambda e0, e1: set(e0).intersection(set(e1)), line)


def results_sum(lines, results_func):
    return sum(map(sum, results_intersect(lines, results_func)))


def split_compartments(lines):
    for line in lines:
        split = len(line) // 2
        yield line[:split], line[split:]


def results_1(lines):
    return results_sum(lines, split_compartments)


def get_elves(lines):
    return zip(*[iter(lines)] * 3)


def results_2(lines):
    return results_sum(lines, get_elves)


def run():
    print_results("data/day03test.txt", results_1, parse_func=parse_func, expected=157)
    print_results("data/day03.txt", results_1, parse_func=parse_func)
    print_results("data/day03test.txt", results_2, parse_func=parse_func, expected=70)
    print_results("data/day03.txt", results_2, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
