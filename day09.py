#!/usr/bin/env python3

from __future__ import annotations

from collections.abc import Generator
from dataclasses import dataclass

from aocutil import Lines, print_results

Result = int


@dataclass
class Coord:
    x: int
    y: int

    def __add__(self: Coord, other: Coord) -> Coord:
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self: Coord, other: Coord) -> Coord:
        return Coord(self.x - other.x, self.y - other.y)


def parse_func(lines: Lines) -> Generator[tuple[str, int], None, None]:
    for line in lines:
        cmd, steps = line.split(" ")
        yield cmd, int(steps)


def move_head(cmd: str, head: Coord, tail: Coord) -> tuple[Coord, Coord]:
    cmd_lookup = {
        "U": Coord(0, -1),
        "D": Coord(0, 1),
        "L": Coord(-1, 0),
        "R": Coord(1, 0),
    }
    head += cmd_lookup[cmd]
    t_off = tail - head

    if cmd in "LR":
        if t_off.x == -2:
            tail.x += 1
        if t_off.x == 2:
            tail.x -= 1
        if abs(t_off.x) == 2:
            if t_off.y == -1:
                tail.y += 1
            if t_off.y == 1:
                tail.y -= 1

    if cmd in "UD":
        if abs(t_off.y) == 2:
            if t_off.x == -1:
                tail.x += 1
            if t_off.x == 1:
                tail.x -= 1
        if t_off.y == -2:
            tail.y += 1
        if t_off.y == 2:
            tail.y -= 1

    return head, tail


def results_1(lines: Lines) -> Result:
    h_pos = Coord(0, 0)
    t_pos = Coord(0, 0)
    t_steps = set()
    for cmd, steps in lines:
        for _ in range(steps):
            h_pos, t_pos = move_head(cmd, h_pos, t_pos)
            t_steps.add((t_pos.x, t_pos.y))

    return len(t_steps)


def run() -> None:
    print_results(
        "data/day09test.txt",
        results_1,
        parse_func=parse_func,
        expected=13,
    )
    print_results("data/day09.txt", results_1, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
