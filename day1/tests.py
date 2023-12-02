import unittest

import trebuchet


class TestDay1(unittest.TestCase):
    def test_getInputData(self):
        input_filepath = "day1/data/day_one_data.txt"
        trebuchet.getInputData(input_filepath)

        pass

    def test_stripData(self):
        data = [" 1abc2\n ", "pqr3stu8vwx\n", "  a1b2c3d4e5f\n", "\ntreb7uchet\n"]
        stripped_data = trebuchet.stripData(data)

        return self.assertEqual(
            stripped_data, ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        )

    def test_removeLetters(self):
        data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        stripped_data = trebuchet.removeLetters(data)

        return self.assertEqual(stripped_data, ["12", "38", "12345", "7"])

    def test_retainFirstandLast(self):
        data = ["12", "38", "12345", "7"]
        stripped_data = trebuchet.retainFirstandLast(data)

        return self.assertEqual(stripped_data, ["12", "38", "15", "77"])

    def test_convertToInteger(self):
        data = ["12", "38", "15", "77"]
        stripped_data = trebuchet.convertToInteger(data)

        return self.assertEqual(stripped_data, [12, 38, 15, 77])

    def test_sumData(self):
        data = [12, 38, 15, 77]
        summed_data = trebuchet.sumData(data)

        return self.assertEqual(summed_data, 142)

    def test_advent1(self):
        input_filepath = "day1/data/day_one_data.txt"
        data: list[str] = trebuchet.getInputData(path=input_filepath)
        data = trebuchet.stripData(data=data)
        data = trebuchet.removeLetters(data=data)
        data = trebuchet.retainFirstandLast(data=data)
        data = trebuchet.convertToInteger(data=data)
        data = trebuchet.sumData(data=data)

        return self.assertEqual(data, 53386)

    def test_mapEnglishDigits(self):
        data: list[str] = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
            "eighthree",
        ]
        data = trebuchet.stripData(data=data)
        data = trebuchet.mapEnglishDigits(data)
        data = trebuchet.removeLetters(data=data)
        data = trebuchet.retainFirstandLast(data=data)

        return self.assertEqual(data, ["29", "83", "13", "24", "42", "14", "76", "83"])

    def test_advent2(self):
        data: list[str] = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
            "12",
            "nine",
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
            "eighthree",
        ]

        data = trebuchet.stripData(data=data)
        data = trebuchet.mapEnglishDigits(data)
        data = trebuchet.removeLetters(data=data)
        data = trebuchet.retainFirstandLast(data=data)
        data = trebuchet.convertToInteger(data=data)
        data = trebuchet.sumData(data=data)

        return self.assertEqual(data, (281 + 12 + 99 + 12 + 38 + 15 + 77 + 83))


if __name__ == "__main__":
    unittest.main()
