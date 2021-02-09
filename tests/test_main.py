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
                          (2, [2])
                          ],
                         ids=['factor_of_1', 'factor_of_2'])
def test_factors_of_integers(test_input, expected_result):

    # Given: integer test_input

    # When: factoring integer
    result = factors_of(test_input)

    # Then return list factors
    assert result == expected_result


@pytest.mark.parametrize("test_input",
                         [(1.2, ),
                          ('2', )
                          ],
                         ids=['factor_of_float', 'factor_of_string'])
def test_factors_of_integers_with_error(test_input, expected_result):

    # Given: integer test_input

    # When: factoring integer
    result = factors_of(test_input)

    # Then return list factors
    assert result == expected_result


