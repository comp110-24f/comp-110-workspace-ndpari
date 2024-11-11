"""excercise 04"""

__author__ = "730767392"


def all(list: list[int], number: int) -> bool:
    """see if all the integers in a list are the same value"""
    idx: int = 0
    while idx < len(
        list
    ):  # make sure the index is not greater than the length of the list
        if (
            list[idx] != number
        ):  # if a value in the list is not the same as the number,return false
            print("False")
            return False
        else:  # otherwise keep going thru the while loop by adding to the index value
            idx += 1
    if len(list) == 0:
        return False
    print(
        "True"
    )  # if it did not already return false, it will exit the while loop and print True
    return True


def max(input: list[int]) -> int:
    """find the maximum value of an integer"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max = input[0]  # start by setting the potential max as the first value in the list
    for number in input:
        if (
            number > max
        ):  # check if the number that the for loop is on is greater than max;
            # if it is, set the new max to that number
            max = number
    print(max)  # print whatever the outcome of the for loop is
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """ "see if two lists have the same content"""
    idx: int = 0  # set the index to 0
    if len(list1) == len(list2):
        while idx < len(
            list1
        ):  # make sure the index is shorter than the length of both lists
            for number in list1:
                if (
                    number != list2[idx]
                ):  # check the number aginst the index value of the other list
                    # these should be the same position.
                    # #return false if they are not the same
                    print("False")
                    return False
                else:  # if it doesn't return false, add to the index
                    idx += 1
        print("True")  # print true if it exits the for loop (so it is not false)
        return True
    else:
        return False


def extend(list1: list[int], list2: list[int]) -> None:
    """combine the contents of two lists"""
    idx: int = 0  # create an index variable
    while idx < len(
        list2
    ):  # go only while the index is shorter than the length of the second list
        list1.append(list2[idx])  # add the indexed value from list 2 to list 1
        idx += 1  # add 1 to the index
