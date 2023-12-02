import trebuchet

INPUT_DATA_FILEPATH = "day1/data/day_one_data.txt"


def performAdvent() -> int:
    """
    Perform the advent process.

    Returns:
        int: The sum of the processed data.
    """
    data: list[str] = trebuchet.getInputData(path=INPUT_DATA_FILEPATH)
    data = trebuchet.stripData(data=data)
    data = trebuchet.removeLetters(data=data)
    data = trebuchet.retainFirstandLast(data=data)
    data = trebuchet.convertToInteger(data=data)
    summed_data: int = trebuchet.sumData(data=data)
    return summed_data


def performAdvent2():
    """
    Performs the second advent process, handling any spelled out numbers.

    Parameters:
    None

    Returns:
    int: The sum of the transformed data.
    """
    data: list[str] = trebuchet.getInputData(path=INPUT_DATA_FILEPATH)
    data = trebuchet.stripData(data=data)
    data = trebuchet.mapEnglishDigits(data)
    data = trebuchet.removeLetters(data=data)
    data = trebuchet.retainFirstandLast(data=data)
    data = trebuchet.convertToInteger(data=data)
    summed_data: int = trebuchet.sumData(data=data)
    return summed_data


def main() -> None:
    print(f"Sum of all the calibration values: {performAdvent()}")
    print(
        f"Sum of all the calibration values after handling digits: {performAdvent2()}"
    )


if __name__ == "__main__":
    main()
