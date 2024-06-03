import unittest
from relative_datetime.datetime_utils import DateTimeUtils
from datetime import datetime
import pytz

class TestDateTimeUtils(unittest.TestCase):
    def test_relative_datetime(self):
        input_datetime = datetime(2023, 6, 1, tzinfo=pytz.utc)
        relative_time, direction = DateTimeUtils.relative_datetime(input_datetime)
        self.assertIn(direction, ["past", "future"])

    def test_parse_datetime(self):
        datetime_string = "2023-06-01T12:34:56Z"
        parsed_datetime = DateTimeUtils.parse_datetime(datetime_string)
        self.assertEqual(parsed_datetime.year, 2023)
        self.assertEqual(parsed_datetime.month, 6)
        self.assertEqual(parsed_datetime.day, 1)

if __name__ == "__main__":
    unittest.main()
