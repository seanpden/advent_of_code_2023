def iterPrint(data: list[str]) -> None:
    """
    Print each element in the given list.

    Parameters:
        data (list[str]): A list of strings.

    Returns:
        None
    """
    for ele in data:
        print(ele)


def getInputData(path: str) -> list[str]:
    """
    Reads the content of a file and returns it as a list of strings.

    Parameters:
        path (str): The path to the file to be read.

    Returns:
        list[str]: A list of strings containing the lines of the file.

    Raises:
        Exception: If an error occurs while reading the file.
    """
    data: list[str]
    try:
        with open(path, "r") as f:
            data = f.readlines()
    except Exception as e:
        raise e
    return data


def stripData(data: list[str]) -> list[str]:
    """
    Strips leading and trailing whitespace from each element in the input data list.

    Parameters:
        data (list[str]): The input data list.

    Returns:
        list[str]: The stripped data list.

    Raises:
        Exception: If any element in the stripped data list contains a space or a newline character.
    """
    stripped_data: list[str] = [ele.strip() for ele in data]
    if (" " in stripped_data) or ("\n" in stripped_data):
        raise Exception("stripData failed: ' ' | '\n' in stripped_data")
    return stripped_data


def removeLetters(data: list[str]) -> list[str]:
    """
    Remove any letters from the given list of strings and return the modified list.

    Parameters:
        data (list[str]): A list of strings.

    Returns:
        list[str]: A modified list of strings with all letters removed.
    """
    stripped_data: list[str]
    stripped_data = ["".join(i for i in ele if i.isdigit()) for ele in data]
    return stripped_data


def retainFirstandLast(data: list[str]) -> list[str]:
    """
    Generates a new list by retaining the first and last characters of each element in the input list.

    Parameters:
        data (list[str]): The input list of strings.

    Returns:
        list[str]: A new list that contains the first and last characters of each element in the input list.
    """
    stripped_data: list[str] = [ele[0] + ele[-1] for ele in data]
    return stripped_data


def convertToInteger(data: list[str]) -> list[int]:
    """
    Convert a list of strings to a list of integers.

    Parameters:
    - data (list[str]): The list of strings to be converted.

    Returns:
    - list[int]: The list of integers converted from the input strings.

    Raises:
    - Exception: If any element in the input list is not convertible to an integer.
    """
    stripped_data: list[int] = [int(ele) for ele in data]
    if not all(isinstance(ele, int) for ele in stripped_data):
        raise Exception("convertToInteger failed: type(stripped_data) is not list[int]")
    return stripped_data


def sumData(data: list[int]) -> int:
    """
    A function that takes a list of integers as input and returns the sum of all the integers in the list.

    Parameters:
    - data: A list of integers.

    Returns:
    - The sum of all the integers in the list.
    """
    return sum(data)


def mapEnglishDigits(data: list[str]) -> list[str]:
    """
    Maps English digits in the given list of strings to their corresponding encoded values.

    Args:
        data (list[str]): A list of strings containing English digits.

    Returns:
        list[str]: A list of strings with English digits mapped to their encoded values.
    """
    digits = {
        "one": "o1e",
        "two": "t2w",
        "three": "th3ee",
        "four": "fo4r",
        "five": "f5ve",
        "six": "s6x",
        "seven": "se7en",
        "eight": "ei8ght",
        "nine": "n9ne",
        "zero": "ze0o",
    }

    for key, value in digits.items():
        data = [ele.replace(key, value) for ele in data]

    return data
