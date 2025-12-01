import math
import pytest
from ..data_converter import convert


def test_celsius_to_fahrenheit():
    src, result = convert([0, 100], "celsius", "fahrenheit")
    assert src == [0, 100]
    assert result == [32.0, 212.0]


def test_fahrenheit_to_celsius():
    src, result = convert([32, 212], "fahrenheit", "c")
    assert src == [32, 212]
    assert all(
        math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
        for a, b in zip(result, [0.0, 100.0])
    )


def test_km_to_miles():
    src, result = convert([1], "km", "miles")
    assert src == [1]
    assert math.isclose(result[0], 0.62, rel_tol=1e-2)


def test_miles_to_km():
    src, result = convert([1], "miles", "km")
    assert src == [1]
    assert math.isclose(result[0], 1.61, rel_tol=1e-2)


def usd_to_eur():
    src, result = convert([20, 100], "usd", "eur")
    assert src == [20, 100]
    assert result == [17.2, 86.0]


def eur_to_usd():
    src, result = convert([50, 100], "eur", "usd")
    assert src == [50, 100]
    assert result == [58, 116]


def test_unsupported_unit_raises():
    with pytest.raises(ValueError, match="Unsupported unit"):
        convert([1], "banana", "km")


def test_unsupported_conversion_pair_raises():
    with pytest.raises(ValueError, match="No conversion defined"):
        convert([1], "celsius", "usd")


def test_empty_values_raises():
    with pytest.raises(ValueError, match="must not be empty"):
        convert([], "c", "f")
