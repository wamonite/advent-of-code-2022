#!/usr/bin/env python3

from math import prod

import numpy as np

from aocutil import Lines, print_results

Result = int


def parse_func(lines: Lines) -> np.array:
    return np.array([[int(c) for c in line] for line in lines])


def get_visible(tree_line: np.array) -> set[int]:
    tree_list = list(enumerate(tree_line))
    results = [tree_list.pop(0)]
    for line_pos, line_height in sorted(tree_list, key=lambda v: v[1], reverse=True):
        for idx, result in reversed(list(enumerate(results))):
            result_pos, result_height = result
            if line_pos > result_pos:
                if line_height > result_height:
                    results.insert(idx + 1, (line_pos, line_height))

                break

    return {p for p, h in results}


def find_visible_trees(trees: np.array) -> set[tuple[int, int]]:
    width = trees.shape[0] - 1
    height = trees.shape[1] - 1
    results = {
        (0, 0),
        (0, height),
        (width, 0),
        (width, height),
    }
    for idx in range(1, height):
        results.update({(v, idx) for v in get_visible(trees[idx, :])})
        results.update({(width - v, idx) for v in get_visible(reversed(trees[idx, :]))})
    for idx in range(1, width):
        results.update({(idx, v) for v in get_visible(trees[:, idx])})
        results.update(
            {(idx, height - v) for v in get_visible(reversed(trees[:, idx]))},
        )

    return results


def results_1(trees: np.array) -> Result:
    return len(find_visible_trees(trees))


def get_scenic_tree_count(trees: np.array, x: int, y: int) -> int:
    width = trees.shape[0] - 1
    height = trees.shape[1] - 1

    tree_height = trees[y, x]
    ranges = [
        (range(x - 1, -1, -1), True),
        (range(x + 1, width + 1), True),
        (range(y - 1, -1, -1), False),
        (range(y + 1, height + 1), False),
    ]
    scores = []
    for r, a in ranges:
        s = 0
        for pos in r:
            h = trees[y, pos] if a else trees[pos, x]
            s += 1
            if h >= tree_height:
                break
        scores.append(s)

    return prod(scores)


def results_2(trees: np.array) -> Result:
    score_max = 0
    for x in range(0, trees.shape[0]):
        for y in range(0, trees.shape[1]):
            score = get_scenic_tree_count(trees, x, y)
            if score > score_max:
                score_max = score

    return score_max


def run() -> None:
    print_results(
        "data/day08test.txt",
        results_1,
        parse_func=parse_func,
        expected=21,
    )
    print_results("data/day08.txt", results_1, parse_func=parse_func)
    print_results(
        "data/day08test.txt",
        results_2,
        parse_func=parse_func,
        expected=8,
    )
    print_results("data/day08.txt", results_2, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
