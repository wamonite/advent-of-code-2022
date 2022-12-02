# -*- coding: utf-8 -*-


def load_file(file_name):
    with open(file_name) as file_object:
        yield from (line.rstrip() for line in file_object)


def print_results(file_name, results_func, *, parse_func=None, expected=None):
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
