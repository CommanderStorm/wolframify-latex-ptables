import json
import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_conversion(self):
        with open("testdata.json", "r") as outfile:
            test_data = json.load(outfile)
        for input, expected in test_data:
            self.assertEqual(expected, main.convert(input))


if __name__ == '__main__':
    unittest.main()
