#!/usr/bin/env python3

from aocutil import print_results

ROCK = 1
PAPER = 2
SCISSORS = 3


def parse_func(lines):
    moves = (line.split(" ") for line in lines)
    yield from (
        (ord(move[0]) - ord("A") + 1, ord(move[1]) - ord("X") + 1) for move in moves
    )


def calculate_move(line):
    them, me = line

    move_func = {
        ROCK: lose,
        PAPER: lambda move: move,
        SCISSORS: win,
    }.get(me)

    return them, move_func(them)


def win(them):
    return {
        ROCK: PAPER,
        PAPER: SCISSORS,
        SCISSORS: ROCK,
    }[them]


def lose(them):
    return {
        ROCK: SCISSORS,
        PAPER: ROCK,
        SCISSORS: PAPER,
    }[them]


def score_game(line):
    them, me = line

    score = me

    if them == me:
        score += 3

    elif win(them) == me:
        score += 6

    return score


def results_1(lines):
    games = (score_game(line) for line in lines)
    return sum(games)


def results_2(lines):
    moves = (calculate_move(line) for line in lines)
    games = (score_game(move) for move in moves)
    return sum(games)


def run():
    print_results("data/day02test.txt", results_1, parse_func=parse_func, expected=15)
    print_results("data/day02.txt", results_1, parse_func=parse_func)
    print_results("data/day02test.txt", results_2, parse_func=parse_func, expected=12)
    print_results("data/day02.txt", results_2, parse_func=parse_func)


if __name__ == "__main__":
    try:
        run()

    except (KeyboardInterrupt, AssertionError):
        pass
