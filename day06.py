#!/usr/bin/env python3

from collections import deque

from aocutil import Lines, print_results

Result = list[int]


def get_marker(line: str) -> int:
    marker = deque()
    for idx, c in enumerate(line, 1):
        while c in marker:
            marker.popleft()

        marker.append(c)

        if len(marker) == 4:
            return idx


def results_1(lines: Lines) -> Result:
    return [get_marker(line) for line in lines]


def run() -> None:
    print_results(
        "data/day06test.txt",
        results_1,
        expected=[7, 5, 6, 10, 11],
    )
    print_results("data/day06.txt", results_1)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
