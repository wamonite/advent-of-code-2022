#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aocutil import print_results, Lines
from collections.abc import Generator
from typing import Union
from collections import deque


Stacks = list[deque]
Moves = tuple[int, int, int]
ParsedFile = Generator[Union[Stacks, Moves], None, None]
Result = str


def parse_stack_level(line: str) -> str:
    return line[1::4]


def add_to_stacks(stacks: Stacks, stack_level: str) -> None:
    for idx, container in enumerate(stack_level):
        if idx >= len(stacks):
            stack = deque()
            stacks.append(stack)

        else:
            stack = stacks[idx]

        if container != " ":
            stack.appendleft(container)


def parse_func(lines: Lines) -> ParsedFile:
    stacks = []
    for line in lines:
        if "[" in line:
            add_to_stacks(stacks, parse_stack_level(line))

        elif stacks:
            yield stacks
            stacks = None

        if line.startswith("move"):
            instruction = line.split(" ")
            yield [int(i) for i in instruction[1::2]]


def process_instruction(stacks, number, start, end):
    for count in range(number):
        container = stacks[start - 1].pop()
        stacks[end - 1].append(container)


def results_1(file_input: ParsedFile) -> Result:
    stacks = None
    for val in file_input:
        if not stacks:
            stacks = val

        else:
            process_instruction(stacks, *val)

    return "".join([s.pop() for s in stacks])


def run():
    print_results(
        "data/day05test.txt",
        results_1,
        parse_func=parse_func,
        expected="CMZ",
    )
    print_results("data/day05.txt", results_1, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
