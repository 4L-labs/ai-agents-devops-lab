import pytest

from lab_app.duration import parse_duration_seconds


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("10s", 10),
        ("2m", 120),
        ("1h", 3600),
        ("0s", 0),
        (" 5M ", 300),
    ],
)
def test_parse_duration_seconds_ok(value: str, expected: int) -> None:
    assert parse_duration_seconds(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        "",
        "10",
        "xs",
        "-1s",
        "1d",
    ],
)
def test_parse_duration_seconds_invalid(value: str) -> None:
    with pytest.raises(ValueError):
        parse_duration_seconds(value)
