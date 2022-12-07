#!/usr/bin/env python3

from collections.abc import Iterator
from pathlib import Path
from typing import Optional, Union

from aocutil import Lines, print_results

PathTree = dict[str, Union[dict, int]]
Result = int


def parse_tree(lines: Iterator[str], tree: Optional[PathTree] = None) -> PathTree:
    if tree is None:
        tree = {}

    while line := next(lines, False):
        if line.startswith("$ "):
            cmd = line[2:]
            if cmd != "ls":
                cd_arg = cmd[3:]
                if cd_arg == "..":
                    return tree

                tree[cd_arg] = {}
                parse_tree(lines, tree[cd_arg])

        else:
            try:
                size, file_name = line.split(" ")
                size = int(size)
                tree[file_name] = size

            except ValueError:
                continue

    return tree


def sum_tree(
    tree: PathTree,
    results: list[tuple[str, int]],
    path: Optional[Path] = None,
) -> int:
    total = 0
    for name, value in tree.items():
        if isinstance(value, dict):
            child_path = (path if path else Path()) / Path(name)
            total += sum_tree(value, results, child_path)

        else:
            total += value

    if path:
        results.append((str(path), total))

    return total


def parse_func(lines: Lines) -> PathTree:
    return parse_tree(iter(lines))


def results_1(path_tree: PathTree) -> Result:
    results = []
    sum_tree(path_tree, results)
    return sum([value[1] for value in results if value[1] <= 100000])


def run() -> None:
    print_results(
        "data/day07test.txt",
        results_1,
        parse_func=parse_func,
        expected=95437,
    )
    print_results("data/day07.txt", results_1, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
