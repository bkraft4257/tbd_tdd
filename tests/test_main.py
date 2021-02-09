from main import factors_of
import pytest


def test_factors_of_1():

    # Given: integer
    value = 1

    # When: factoring integer
    result = factors_of(value)

    # Then return list factors
    expected_value = []
    assert result == expected_value


@pytest.mark.parametrize("test_input, expected_result",
                         [(1, []),
                          ])
def test_factors_of_integers(test_input, expected_result):

    # Given: integer
    value = 1

    # When: factoring integer
    result = factors_of(value)

    # Then return list factors
    expected_result = []
    assert result == expected_result
