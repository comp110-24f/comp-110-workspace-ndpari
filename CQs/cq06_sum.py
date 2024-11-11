"""Summing the elements of a list using different loops"""

__author__ = "730767392"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    compute: float = 0.0
    while idx < len(vals):
        compute += vals[idx]
        idx += 1
    return compute


def f_sum(vals: list[float]) -> float:
    compute: float = 0.0
    for number in vals:
        compute += number
    return compute


def f_range_sum(vals: list[float]) -> float:
    compute: float = 0.0
    for idx in range(0, len(vals)):
        compute += vals[idx]
    return compute


vals = [1.1, 2.2, 3.3, 4.4]

print(w_sum(vals))
print(f_sum(vals))
print(f_range_sum(vals))
