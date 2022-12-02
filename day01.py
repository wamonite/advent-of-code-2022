#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aoc-2022 day01
"""


def load_file(file_name):
    with open(file_name) as file_object:
        for line in file_object:
            yield line.strip()


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


def print_results(file_name, results_func, expected=None):
    lines = load_file(file_name)
    result = results_func(lines)
    print(f"{file_name}: {result}{f' = {expected}' if expected is not None else ''}")
    if expected is not None:
        assert result == expected


def run():
    print_results("data/day01test.txt", results_1, 24000)
    print_results("data/day01.txt", results_1)
    print_results("data/day01test.txt", results_2, 45000)
    print_results("data/day01.txt", results_2)


if __name__ == '__main__':
    run()
