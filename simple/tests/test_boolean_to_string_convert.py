"""Pytest to check convert boolean to string function"""

import pytest
from ..convert_boolean_to_string import boolean_to_string


def test_boolean_to_string():
    """Convert boolean value to string"""
    pos_result = boolean_to_string(True)
    neg_result = boolean_to_string(False)
    assert pos_result == "True"
    assert neg_result == "False"


def test_unsupported_():
    """Negative test - usage of unsupported input format"""
    with pytest.raises(ValueError, match="Input must be boolean."):
        boolean_to_string("True")
