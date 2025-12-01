"""Pytest to check data converter functionality"""

import math
import pytest
from ..data_converter import convert


def test_celsius_to_fahrenheit():
    """Conversion of celsius to fahrenheit"""
    src, result = convert([0, 100], "celsius", "fahrenheit")
    assert src == [0, 100]
    assert result == [32.0, 212.0]


def test_fahrenheit_to_celsius():
    """Conversion of fahrenheit to celsius"""
    src, result = convert([32, 212], "fahrenheit", "c")
    assert src == [32, 212]
    assert all(
        math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
        for a, b in zip(result, [0.0, 100.0])
    )


def test_km_to_miles():
    """Conversion of km to miles"""
    src, result = convert([1], "km", "miles")
    assert src == [1]
    assert math.isclose(result[0], 0.62, rel_tol=1e-2)


def test_miles_to_km():
    """Conversion of miles to km"""
    src, result = convert([1], "miles", "km")
    assert src == [1]
    assert math.isclose(result[0], 1.61, rel_tol=1e-2)


def usd_to_eur():
    """Conversion of USD to EUR. Conversion rate is hardcoded: 1USD == 0.86EUR"""
    src, result = convert([20, 100], "usd", "eur")
    assert src == [20, 100]
    assert result == [17.2, 86.0]


def eur_to_usd():
    """Conversion of EUR to USD. Conversion rate is hardcoded: 1EUR == 1.16USD"""
    src, result = convert([50, 100], "eur", "usd")
    assert src == [50, 100]
    assert result == [58, 116]


def test_unsupported_unit_raises():
    """Negative test - usage of unsupported unit"""
    with pytest.raises(ValueError, match="Unsupported unit"):
        convert([1], "banana", "km")


def test_unsupported_conversion_pair_raises():
    """Negative test - usage of undefined conversion"""
    with pytest.raises(ValueError, match="No conversion defined"):
        convert([1], "celsius", "usd")


def test_empty_values_raises():
    """Negative test - usage of empty input"""
    with pytest.raises(ValueError, match="must not be empty"):
        convert([], "c", "f")
