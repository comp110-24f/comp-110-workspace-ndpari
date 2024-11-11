"""ex05 testing"""

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

__author__ = "73076392"


def test_only_evens_return_use_case() -> None:
    """testing that it returns even values"""
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert only_evens(input=test) == [2, 4, 6, 8]


def test_only_evens_mutate_use_case() -> None:
    """testing that it doesn't mutate the list"""
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    only_evens(input=test)
    assert test == [1, 2, 3, 4, 5, 6, 7, 8]


def test_only_evens_edge_case() -> None:
    """testing an edge case"""
    assert only_evens(input=[]) == []


def test_sub_return_use_case() -> None:
    """testing that it subs correctly"""
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sub(input=test, start_index=1, end_index=4) == [2, 3, 4]


def test_sub_mutate_use_case() -> None:
    """testing that it doesn't mutate the list"""
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    sub(input=test, start_index=1, end_index=4)
    assert test == [1, 2, 3, 4, 5, 6, 7, 8]


def test_sub_edge_case() -> None:
    """testing an edge case"""
    assert sub(input=[], start_index=1, end_index=5) == []


def test_add_at_index_return_use_case() -> None:
    """testing that it adds correctly"""
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert (
        add_at_index(input=test, elem=1, idx=4) is None
    )  # returns none, not what is printed


def test_add_at_index_mutate_use_case() -> None:
    """testing that it mutates the list"""
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    add_at_index(input=test, elem=1, idx=4)
    assert test == [1, 2, 3, 4, 1, 5, 6, 7, 8]


def test_add_at_index_edge_case() -> None:
    """testing an edge case"""
    test: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(input=test, elem=1, idx=4)
