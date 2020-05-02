import pytest
import datetime
from app import convert_datetime


@pytest.fixture
def beginning_of_time():
    return datetime.datetime.fromtimestamp(0)


def test_convert_datetime(beginning_of_time):
    a, b, c, d = convert_datetime(beginning_of_time)
    assert a == "0"
    assert b == "1970-01-01T01:00:00"
    assert c == "1970-01-01T00:00:00+00:00"
    assert d == 'Thu Jan  1 01:00:00 1970'
