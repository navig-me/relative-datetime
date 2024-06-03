# relative-datetime

`relative-datetime` is a Python library for working with relative datetime strings and parsing datetime strings. It provides utility functions to easily convert datetime objects to human-readable relative times and to parse various datetime string formats into `datetime` objects.

## Features

- Convert `datetime` objects to human-readable relative time strings, such as:
  - "2 seconds ago"
  - "5 minutes ago"
  - "3 hours ago"
  - "1 day ago"
  - "2 weeks ago"
  - "1 month ago"
  - "2 years ago"
- Determine if a `datetime` object is in the past or future.
- Parse a wide variety of datetime string formats into `datetime` objects.
- Support for timezones.

## Installation

You can install the library using `pip`:

```bash
pip install relative-datetime
```

## Usage

### Importing the Library

```python
from relative_datetime import DateTimeUtils
```

### Getting Relative Datetime Strings

To convert a `datetime` object to a relative datetime string and determine if it is in the past or future, use the `relative_datetime` method.

#### Example 1: Datetime in the Past

```python
from datetime import datetime, timedelta
import pytz
from relative_datetime import DateTimeUtils

# Example datetime object (1 day ago)
input_datetime = datetime.now(pytz.utc) - timedelta(days=1)

# Get relative datetime string and direction
relative_time, direction = DateTimeUtils.relative_datetime(input_datetime)
print(f"Relative time: {relative_time}, Direction: {direction}")
# Output: Relative time: 1 day, Direction: past
```

#### Example 2: Datetime in the Future

```python
from datetime import datetime, timedelta
import pytz
from relative_datetime import DateTimeUtils

# Example datetime object (in 2 hours)
input_datetime = datetime.now(pytz.utc) + timedelta(hours=2)

# Get relative datetime string and direction
relative_time, direction = DateTimeUtils.relative_datetime(input_datetime)
print(f"Relative time: {relative_time}, Direction: {direction}")
# Output: Relative time: 2 hours, Direction: future
```

### Parsing Datetime Strings

To parse a datetime string into a `datetime` object, use the `parse_datetime` method.

#### Example 1: ISO 8601 Format

```python
from relative_datetime import DateTimeUtils

# Example datetime string in ISO 8601 format
datetime_string = "2023-06-01T12:34:56Z"

# Parse the datetime string
parsed_datetime = DateTimeUtils.parse_datetime(datetime_string)
print(f"Parsed datetime: {parsed_datetime}")
# Output: Parsed datetime: 2023-06-01 12:34:56+00:00
```

#### Example 2: Custom Format

```python
from relative_datetime import DateTimeUtils

# Example datetime string in a custom format
datetime_string = "June 1, 2023 12:34 PM"

# Parse the datetime string
parsed_datetime = DateTimeUtils.parse_datetime(datetime_string)
print(f"Parsed datetime: {parsed_datetime}")
# Output: Parsed datetime: 2023-06-01 12:34:00+00:00
```

### Handling Different Timezones

The library can also handle datetime objects with different timezones.

#### Example: Datetime with a Specific Timezone

```python
from datetime import datetime
import pytz
from relative_datetime import DateTimeUtils

# Example datetime object with a specific timezone
timezone = pytz.timezone("Asia/Singapore")
input_datetime = timezone.localize(datetime(2023, 6, 1, 12, 0, 0))

# Get relative datetime string and direction
relative_time, direction = DateTimeUtils.relative_datetime(input_datetime)
print(f"Relative time: {relative_time}, Direction: {direction}")
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Python DateUtil](https://dateutil.readthedocs.io/)
- [Pytz](https://pythonhosted.org/pytz/)


### Explanation of Examples

- **Example 1: Datetime in the Past**: Demonstrates how to convert a datetime object representing a time in the past to a relative time string.
- **Example 2: Datetime in the Future**: Demonstrates how to convert a datetime object representing a future time to a relative time string.
- **Example 1: ISO 8601 Format**: Shows how to parse a datetime string in the ISO 8601 format.
- **Example 2: Custom Format**: Shows how to parse a datetime string in a custom format.
- **Example: Datetime with a Specific Timezone**: Demonstrates handling of datetime objects with specific timezones.

