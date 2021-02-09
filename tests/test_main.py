from main import factors_of


def test_factors_of_value_equals_1():

    # Given: integer
    value = 1

    # When: factoring integer
    result = factors_of(value)

    # Then return list factors
    expected_value = []
    assert result == expected_value
