from main import factors_of
import pytest


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


factor_test_values = [(1, []),
                      (2, [2]),
                      (3, [3]),
                      (4, [2, 2]),
                      (5, [5]),
                      (6, [2, 3]),
                      (7, [7]),
                      (8, [2, 2, 2]),
                      (9, [3, 3]),
                      (2 * 2 * 3 * 3 * 5 * 7, [2, 2, 3, 3, 5, 7]),
                      ]


@pytest.mark.parametrize(argnames="test_input, expected_result",
                         argvalues=factor_test_values,
                         ids=[f'factor_of({ii[0]})' for ii in factor_test_values]
                         )
def test_factors_of_integers(test_input, expected_result):
    # Given: integer test_input

    # When: factoring integer
    result = factors_of(test_input)

    # Then return list factors
    assert result == expected_result
