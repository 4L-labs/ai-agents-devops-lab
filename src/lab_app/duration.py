def parse_duration_seconds(value: str) -> int:
    """
    Parse duration strings like:
    - "10s" => 10
    - "2m"  => 120
    - "1h"  => 3600
    """
    value = value.strip()
    if not value:
        raise ValueError("duration is empty")

    unit = value[-1].lower()
    number_part = value[:-1]

    if unit == "s":
        multiplier = 1
    elif unit == "m":
        multiplier = 60
    elif unit == "h":
        multiplier = 3600
    else:
        raise ValueError(f"unknown duration unit: {unit!r}")

    seconds = int(number_part) * multiplier
    if seconds < 0:
        raise ValueError("duration must be >= 0")
    return seconds
