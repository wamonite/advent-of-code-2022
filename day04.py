#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aocutil import print_results, Lines
from collections.abc import Generator


Pair = tuple[int, int]
Pairs = tuple[Pair, Pair]
PairGenerator = Generator[Pairs, None, None]


def parse_func(lines: Lines) -> PairGenerator:
    for line in lines:
        yield [[int(v) for v in split_val.split("-")] for split_val in line.split(",")]


def test_inside(p0: Pair, p1: Pair) -> bool:
    return p0[0] >= p1[0] and p0[1] <= p1[1]


def results_1(pairs: PairGenerator) -> int:
    result = [p for p in pairs if test_inside(p[0], p[1]) or test_inside(p[1], p[0])]
    return len(result)


def test_overlap(p0: Pair, p1: Pair) -> bool:
    return not (p0[1] < p1[0] or p0[0] > p1[1])


def results_2(pairs: PairGenerator) -> int:
    result = [p for p in pairs if test_overlap(p[0], p[1])]
    return len(result)


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
