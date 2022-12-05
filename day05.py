#!/usr/bin/env python3

from collections import deque
from collections.abc import Callable, Generator
from typing import Union

from aocutil import Lines, print_results

Stacks = list[deque]
Moves = tuple[int, int, int]
ParsedFile = Generator[Union[Stacks, Moves], None, None]
InstructionFunc = Callable[[Stacks, int, int, int], None]
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


def results_return(file_input: ParsedFile, instruction_func: InstructionFunc) -> Result:
    stacks = None
    for val in file_input:
        if not stacks:
            stacks = val

        else:
            instruction_func(stacks, *val)

    return "".join([s.pop() for s in stacks])


def process_instruction_1(stacks: Stacks, number: int, start: int, end: int) -> None:
    for _ in range(number):
        container = stacks[start - 1].pop()
        stacks[end - 1].append(container)


def results_1(file_input: ParsedFile) -> Result:
    return results_return(file_input, process_instruction_1)


def process_instruction_2(stacks: Stacks, number: int, start: int, end: int) -> None:
    crane = deque()
    for _ in range(number):
        crane.append(stacks[start - 1].pop())
    for _ in range(number):
        stacks[end - 1].append(crane.pop())


def results_2(file_input: ParsedFile) -> Result:
    return results_return(file_input, process_instruction_2)


def run() -> None:
    print_results(
        "data/day05test.txt",
        results_1,
        parse_func=parse_func,
        expected="CMZ",
    )
    print_results("data/day05.txt", results_1, parse_func=parse_func)
    print_results(
        "data/day05test.txt",
        results_2,
        parse_func=parse_func,
        expected="MCD",
    )
    print_results("data/day05.txt", results_2, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
