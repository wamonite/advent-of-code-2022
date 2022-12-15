#!/usr/bin/env python3

from __future__ import annotations

import operator
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from math import prod

from aocutil import Lines, print_results


@dataclass
class Monkey:
    items: list
    test_op: Callable[[int, int], int]
    test_val: int
    test_divisor: int
    target_true: int
    target_false: int


def parse_func(lines: Lines) -> list[Monkey]:
    monkeys = []
    while True:
        _ = int(next(lines).split(" ")[1][:-1])

        items = [int(i) for i in next(lines).replace(",", "").split(" ")[4:]]

        test_line = next(lines).split(" ")[6:]
        test_op = {
            "*": operator.mul,
            "+": operator.add,
        }[test_line[0]]
        test_val = None if test_line[1] == "old" else int(test_line[1])

        test_divisor = int(next(lines).split(" ")[-1])

        target_true = int(next(lines).split(" ")[-1])

        target_false = int(next(lines).split(" ")[-1])

        monkeys.append(
            Monkey(
                items,
                test_op,
                test_val,
                test_divisor,
                target_true,
                target_false,
            ),
        )

        try:
            next(lines)

        except StopIteration:
            break

    return monkeys


def calculate_rounds(monkeys: list[Monkey], relief: bool, rounds: int) -> int:
    count_activity = Counter()
    sm = prod([m.test_divisor for m in monkeys])
    for _ in range(rounds):
        for idx, monkey in enumerate(monkeys):
            count_activity[idx] += len(monkey.items)
            for item in monkey.items:
                test_val = item if monkey.test_val is None else monkey.test_val
                item = monkey.test_op(item, test_val)
                item %= sm
                if relief:
                    item //= 3
                target = (
                    monkey.target_true
                    if item % monkey.test_divisor == 0
                    else monkey.target_false
                )
                monkeys[target].items.append(item)
            monkey.items = []

    return prod(sorted([v[1] for v in count_activity.items()])[-2:])


def results_1(monkeys: list[Monkey]) -> int:
    return calculate_rounds(monkeys, True, 20)


def results_2(monkeys: list[Monkey]) -> int:
    return calculate_rounds(monkeys, False, 10000)


def run() -> None:
    print_results(
        "data/day11test.txt",
        results_1,
        parse_func=parse_func,
        expected=10605,
    )
    print_results("data/day11.txt", results_1, parse_func=parse_func)
    print_results(
        "data/day11test.txt",
        results_2,
        parse_func=parse_func,
        expected=2713310158,
    )
    print_results("data/day11.txt", results_2, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
