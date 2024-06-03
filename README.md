# relative-datetime

A Python library to get relative datetime strings and parse datetime strings.

## Installation

```bash
pip install relative-datetime
```

## Usage

```python
from relative_datetime import DateTimeUtils

# Example usage
input_datetime = datetime(2023, 6, 1, tzinfo=pytz.utc)
relative_time, direction = DateTimeUtils.relative_datetime(input_datetime)
print(f"Relative time: {relative_time}, Direction: {direction}")

datetime_string = "2023-06-01T12:34:56Z"
parsed_datetime = DateTimeUtils.parse_datetime(datetime_string)
print(f"Parsed datetime: {parsed_datetime}")
```