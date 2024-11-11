from find_max import find_and_remove_max

"""cq07 pt 2"""

__author__ = "730767392"


def test_find_and_remove_max_use_case_return_use_case() -> None:
    """testing that it returns max value"""
    assert find_and_remove_max([1, 4, 5, 7, 3]) == 7


def test_find_and_remove_max_use_case_mutate_use_case() -> None:
    """testing that it mutates the list"""
    test: list[int] = [1, 4, 5, 7, 3]
    find_and_remove_max(test)
    assert test == [1, 4, 5, 3]


def test_find_and_remove_max_use_case_unconventional_use_case() -> None:
    """testing that it mutates the list"""
    assert find_and_remove_max([]) == -1
