# -*- coding: utf-8 -*-

from collections.abc import Generator, Callable
from typing import Any, Union


Lines = Generator[str, None, None]
ResultsFunc = Callable[[Generator[Any]], Any]
ParseFunc = Callable[[Lines], Generator[Any]]


def load_file(file_name: str) -> Lines:
    with open(file_name) as file_object:
        yield from (line.rstrip() for line in file_object)


def print_results(
    file_name: str,
    results_func: ResultsFunc,
    *,
    parse_func: Union[ParseFunc, None] = None,
    expected: Any = None,
):
    lines = load_file(file_name)
    if parse_func and callable(parse_func):
        lines = parse_func(lines)
    result = results_func(lines)
    suffix = (
        f" {'=' if result == expected else '!='} {expected}"
        if expected is not None
        else ""
    )
    print(f"{file_name}: {result}{suffix}")
    if expected is not None:
        assert result == expected
