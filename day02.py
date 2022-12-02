#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aocutil import print_results


def parse_func(lines):
    yield from (line.split(" ") for line in lines)


def score_game(line):
    them, me = line

    score = ord(me) - ord("X") + 1

    if score == ord(them) - ord("A") + 1:
        score += 3

    elif {
        "C": "X",
        "A": "Y",
        "B": "Z",
    }[them] == me:
        score += 6

    return score


def results_1(lines):
    return sum(map(score_game, lines))


def run():
    print_results("data/day02test.txt", results_1, parse_func=parse_func, expected=15)
    print_results("data/day02.txt", results_1, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
