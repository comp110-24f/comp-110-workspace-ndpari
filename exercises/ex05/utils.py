"""ex05 acc code"""

__author__ = "730767392"


def only_evens(input: list[int]) -> list[int]:
    """a function that returns only the even values from a list"""
    even_list: list[int] = []  # create an empty list that values can be added to
    idx: int = 0
    while idx < len(input):
        if (
            input[idx] % 2 == 0
        ):  # if a value in the list is divisble by 2, add to the new list
            even_list.append(input[idx])
        idx += 1
    print(even_list)
    return even_list


def sub(input: list[int], start_index: int, end_index: int) -> list[int]:
    """a function that returns a list that is only part of the list"""
    sub_list: list[int] = []  # create an empty list that new values can be added to
    if start_index < 0:  # set the start index to 0 if it iss less than 0
        start_index = 0
    if end_index > len(
        input
    ):  # set the end index to the length of the list if it is greater than the length
        end_index = len(input)
    for idx in range(
        start_index, end_index
    ):  # create a range based on the inputted start and end index
        sub_list.append(
            input[idx]
        )  # add values to the empty list if they are within the range
    print(sub_list)
    return sub_list


def add_at_index(input: list[int], elem: int, idx: int) -> None:
    """a function that returns a list with a new value"""
    if idx < 0 or idx > len(input):  # create an error if the indexes are out of bounds
        raise IndexError("Index is out of bounds for the input list")
    mod_input: list[int] = list(
        input
    )  # create a new list that is a copy (not refernce) to the input list
    while idx < len(
        input
    ):  # remove every value at the end of the input list until it is the input index
        input.pop(idx)
    input.append(elem)  # add the element that was input
    while idx < len(
        mod_input
    ):  # append values from the copied list to the original list
        # going up through the list
        input.append(mod_input[idx])
        idx += 1
    print(input)
