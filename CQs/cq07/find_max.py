"""cq07 pt 1"""

__author__ = "730767392"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        print(-1)
        return -1
    max = input[0]
    for number in input:
        if number > max:
            max = number
    while max in input:
        input.remove(max)
    print(max)
    return max


list1 = [1, 2, 3, 4, 6, 10, 5, 10, 4]

find_and_remove_max(list1)
print(list1)
