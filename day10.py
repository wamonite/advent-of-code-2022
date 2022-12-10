#!/usr/bin/env python3

from __future__ import annotations

from collections.abc import Generator
from dataclasses import dataclass

from aocutil import Lines, print_results

Command = tuple[str, int]


def parse_func(lines: Lines) -> Generator[Command, None, None]:
    for line in lines:
        if line == "noop":
            yield "noop", None
        else:
            yield "addx", int(line[4:])


@dataclass
class CPU:
    command: str = None
    value: int = None
    cycle: int = 0
    command_cycle: int = 0
    register: int = 1

    def step(self: CPU, commands: Generator[Command, None, None]) -> None:
        if self.command is None:
            self.command, self.value = next(commands)

        command_complete = False
        if self.command == "addx":
            if self.command_cycle == 2:
                self.register += self.value
                command_complete = True

        elif self.command == "noop":
            if self.command_cycle == 1:
                command_complete = True

        if command_complete:
            self.command, self.value = next(commands)
            self.command_cycle = 0

        self.cycle += 1
        self.command_cycle += 1


def results_1(commands: Generator[Command, None, None]) -> int:
    ss_list = [60, 100, 140, 180, 220]
    ss_step = 20
    ss = 0
    cpu = CPU()
    while True:
        cpu.step(commands)
        if cpu.cycle == ss_step:
            ss += cpu.register * cpu.cycle
            if not ss_list:
                break
            ss_step = ss_list.pop(0)

    return ss


def results_2(commands: Generator[Command, None, None]) -> str:
    crt = ""
    row = 0
    cpu = CPU()
    while True:
        x = cpu.cycle % 40
        cpu.step(commands)
        crt += "#" if x >= cpu.register - 1 and x <= cpu.register + 1 else "."
        if cpu.cycle % 40 == 0:
            crt += "\n"
            row += 1
            if row == 6:
                break

    return crt


def run() -> None:
    print_results(
        "data/day10test.txt",
        results_1,
        parse_func=parse_func,
        expected=13140,
    )
    print_results("data/day10.txt", results_1, parse_func=parse_func)
    print_results(
        "data/day10test.txt",
        results_2,
        parse_func=parse_func,
        expected="""##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
""",
    )
    print_results("data/day10.txt", results_2, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
