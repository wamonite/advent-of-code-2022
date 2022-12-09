#!/usr/bin/env python3

from __future__ import annotations

from collections.abc import Generator
from dataclasses import dataclass

from aocutil import Lines, print_results

Result = int


@dataclass
class Coord:
    x: int = 0
    y: int = 0

    def __add__(self: Coord, other: Coord) -> Coord:
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self: Coord, other: Coord) -> Coord:
        return Coord(self.x - other.x, self.y - other.y)


def parse_func(lines: Lines) -> Generator[tuple[str, int], None, None]:
    for line in lines:
        cmd, steps = line.split(" ")
        yield cmd, int(steps)


def move_head(cmd: str, head: Coord) -> tuple[Coord, Coord]:
    cmd_lookup = {
        "U": Coord(0, -1),
        "D": Coord(0, 1),
        "L": Coord(-1, 0),
        "R": Coord(1, 0),
    }
    move = cmd_lookup[cmd]
    return head + move, move


def follow_head(head: Coord, tail: Coord, move: Coord) -> tuple[Coord, Coord]:
    t_off = tail - head

    tail_move = Coord()
    # TODO there must be a nicer way!
    if move.x != 0:
        if t_off.x == -2:
            tail_move.x += 1
        if t_off.x == 2:
            tail_move.x -= 1
        if abs(t_off.x) == 2:
            if t_off.y == -1:
                tail_move.y += 1
            if t_off.y == 1:
                tail_move.y -= 1

    if move.y != 0:
        if abs(t_off.y) == 2:
            if t_off.x == -1:
                tail_move.x += 1
            if t_off.x == 1:
                tail_move.x -= 1
        if t_off.y == -2:
            tail_move.y += 1
        if t_off.y == 2:
            tail_move.y -= 1

    return tail + tail_move, tail_move


def results_1(lines: Lines) -> Result:
    head = Coord()
    tail = Coord()
    tail_positions = set()
    for cmd, steps in lines:
        for _ in range(steps):
            head, move = move_head(cmd, head)
            tail, _ = follow_head(head, tail, move)
            tail_positions.add((tail.x, tail.y))

    return len(tail_positions)


def results_2(lines: Lines) -> Result:
    snake_coords = [Coord()] * 10
    tail_positions = set()
    for cmd, steps in lines:
        for _ in range(steps):
            snake_coords[0], move = move_head(cmd, snake_coords[0])
            for idx in range(len(snake_coords) - 1):
                snake_coords[idx + 1], move = follow_head(
                    snake_coords[idx],
                    snake_coords[idx + 1],
                    move,
                )
            tail_positions.add((snake_coords[-1].x, snake_coords[-1].y))

    return len(tail_positions)


def run() -> None:
    print_results(
        "data/day09test-1.txt",
        results_1,
        parse_func=parse_func,
        expected=13,
    )
    print_results("data/day09.txt", results_1, parse_func=parse_func)
    print_results(
        "data/day09test-2.txt",
        results_2,
        parse_func=parse_func,
        expected=36,
    )
    print_results("data/day09.txt", results_2, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
