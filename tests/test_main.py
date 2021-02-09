from main import factors_of
import pytest
from math import prod


@pytest.mark.parametrize("test_input",
                         [(1.2,),
                          ('2',)
                          ],
                         ids=['factor_of_float', 'factor_of_string'])
def test_factors_of_integers_with_error(test_input):
    # Given: an input other than type

    # When: calling factors_of return TypeError
    # Then return TypeError

    with pytest.raises(TypeError):
        factors_of(test_input)


factor_test_values = [([2]),
                      ([3]),
                      ([2, 2]),
                      ([5]),
                      ([2, 3]),
                      ([7]),
                      ([2, 2, 2]),
                      ([3, 3]),
                      ([2, 2, 3, 3, 5, 7]),
                      ]


@pytest.mark.parametrize(argnames="expected_result",
                         argvalues=factor_test_values,
                         ids=[f'factor_of({prod(ii)})' for ii in factor_test_values]
                         )
def test_factors_of_integers(expected_result):
    # Given: integer test_input
    test_input = prod(expected_result)

    # When: factoring integer
    result = factors_of(test_input)

    # Then return list factors
    assert result == expected_result
