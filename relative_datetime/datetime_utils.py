from datetime import datetime
from dateutil import parser
import pytz

class DateTimeUtils:
    @staticmethod
    def relative_datetime(datetime_input):
        if datetime_input == "NOW":
            datetime_input = datetime.now(pytz.utc)
        elif not isinstance(datetime_input, datetime):
            raise ValueError("Input must be a datetime object")

        # Convert naive datetime to UTC
        if datetime_input.tzinfo is None:
            datetime_input = pytz.utc.localize(datetime_input)

        now = datetime.now(pytz.utc)
        diff = now - datetime_input

        if diff.total_seconds() < 0:
            diff = -diff
            time_direction = "future"
        else:
            time_direction = "past"

        periods = [
            (diff.days // 365, "year", "years"),
            (diff.days // 30, "month", "months"),
            (diff.days // 7, "week", "weeks"),
            (diff.days, "day", "days"),
            (diff.seconds // 3600, "hour", "hours"),
            (diff.seconds // 60, "minute", "minutes"),
            (diff.seconds, "second", "seconds")
        ]

        for period, singular, plural in periods:
            if period:
                return (f"{period} {singular if period == 1 else plural}", time_direction)
        
        return ("just now", time_direction)

    @staticmethod
    def parse_datetime(datetime_string):
        if datetime_string.lower() == "now":
            return datetime.now(pytz.utc)
        
        try:
            dt = parser.parse(datetime_string)
            if dt.tzinfo is None:
                dt = pytz.utc.localize(dt)
            return dt
        except (ValueError, OverflowError):
            raise ValueError("Invalid datetime string format")

