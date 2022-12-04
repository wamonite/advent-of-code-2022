#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aocutil import print_results


def parse_func(lines):
    for line in lines:
        yield [[int(v) for v in split_val.split("-")] for split_val in line.split(",")]


def test_inside(p0, p1):
    return p0[0] >= p1[0] and p0[1] <= p1[1]


def results_1(lines):
    count = 0
    for pairs in lines:
        if test_inside(pairs[0], pairs[1]) or test_inside(pairs[1], pairs[0]):
            count += 1

    return count


def test_overlap(p0, p1):
    return not (p0[1] < p1[0] or p0[0] > p1[1])


def results_2(lines):
    count = 0
    for pairs in lines:
        if test_overlap(pairs[0], pairs[1]):
            count += 1

    return count


def run():
    print_results("data/day04test.txt", results_1, parse_func=parse_func, expected=2)
    print_results("data/day04.txt", results_1, parse_func=parse_func)
    print_results("data/day04test.txt", results_2, parse_func=parse_func, expected=4)
    print_results("data/day04.txt", results_2, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
