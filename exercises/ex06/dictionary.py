""""dictionary of ex06"""

__author__ = "730767392"


def invert(input_list: dict[str, str]) -> dict[str, str]:
    """invert the keys and values of a dictionary"""
    output_list: dict[str, str] = {}  # create an empty dictionary
    for key in input_list:  # cycle through all the keys in the list
        if (
            input_list[key] in output_list
        ):  # make sure that a key does not repeat by checking if it is in the output_list already
            raise KeyError("KeyError")
        output_list[input_list[key]] = (
            key  # create a new entry in the dictionary by creating a key that is the old value
        )
        # then setting it equal to the only key
    print(output_list)
    return output_list


def favorite_color(input: dict[str, str]) -> str:
    "find which color is mentioned the most"
    output_data: dict[str, int] = {}
    if input == {}:  # check if the list is empty the preemptively return nothing
        return ""
    for key in input:  # edit the new list before adding numbers to it
        output_data[input[key]] = 0
    for (
        key
    ) in input:  # add values to the list after already intiializing the list with zeros
        output_data[input[key]] += 1
    output_data["1"] = -1  # create a placeholder so the for loop if works
    final: str = "1"
    for key in output_data:
        if output_data[key] > output_data[final]:
            final = key
    print(final)
    return final


def count(input: list[str]) -> dict[str, int]:
    "count how many times a value appears in a list"
    output: dict[str, int] = {}
    for key in input:
        output[key] = 0  # intitalize the dictionary by setting all values to 0
    for key in input:
        if key in output:
            output[key] += 1  # add to the values everytime they come up
    print(output)
    return output


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    "alphabetize a list based on the first letter of each word"
    output: dict[str, list[str]] = {}
    for key in input:
        output[key[0]] = []  # create an empty list for every letter
    for key in input:
        if key[0] in output:
            output[key[0]].append(
                key
            )  # add to the list by appending; list is called as a value of output
    print(output)
    return output


def update_attendance(input: dict[str, list[str]], day: str, name: str) -> None:
    "update an attendance log when given a day and name"
    if (
        day not in input
    ):  # create a new list for a day if it is not already in the attendance log
        input[day] = []
    if name not in input[day]:  # make sure names aren't repeated
        input[day].append(name)
