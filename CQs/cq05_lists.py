"""Mutating functions"""

__author__ = "730767392"


def manual_append(list: list[int], number: int) -> None:
    list.append(number)


def double(mylist: list[int]) -> None:
    idx: int = 0
    while len(mylist) > idx:
        mylist[idx] = mylist[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
