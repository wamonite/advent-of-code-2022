#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aocutil import print_results


def conv_char(c):
    return ord(c) - (96 if c >= "a" else 38)


def parse_func(lines):
    for line in lines:
        yield [conv_char(c) for c in line]


def split_line(lines):
    for line in lines:
        split = len(line) // 2
        yield line[:split], line[split:]


def compartment_intersect(lines):
    for line in split_line(lines):
        c0 = set(line[0])
        c1 = set(line[1])
        yield c0.intersection(c1)


def results_1(lines):
    return sum(map(sum, compartment_intersect(lines)))


def elf_intersect(lines):
    while e0 := set(next(lines, [])):
        e1 = set(next(lines))
        e2 = set(next(lines))
        yield e0.intersection(e1).intersection(e2)


def results_2(lines):
    return sum(map(sum, elf_intersect(lines)))


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
