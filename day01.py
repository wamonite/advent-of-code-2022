#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aocutil import print_results


def count_calories(lines):
    total = 0
    for line in lines:
        if line:
            total += int(line)

        else:
            yield total
            total = 0

    if total:
        yield total


def results_1(lines):
    calories_list = count_calories(lines)
    return max(calories_list)


def results_2(lines):
    calories_list = count_calories(lines)
    top3 = sorted(calories_list)[-3:]
    return sum(top3)


def run():
    print_results("data/day01test.txt", results_1, expected=24000)
    print_results("data/day01.txt", results_1)
    print_results("data/day01test.txt", results_2, expected=45000)
    print_results("data/day01.txt", results_2)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
