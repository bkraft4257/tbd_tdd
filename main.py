#
# The Three Laws of TDD (Featuring Kotlin) by Uncle Bob Martin
# https://www.youtube.com/watch?v=qkblc5WRn-U
#
# Over the years, I have come to describe Test Drive Development in terms of three
# simple rules.  They are:
#
#    1. You are not allowed to write any production code unless it is to make a failing
#       unit test pass.
#
#    2. You are not allowed to write any more of a unit test than is sufficient to fail;
#       and compilation failures are failures.
#
#    3. You are not allowed to write any more production code than is sufficient to pass the
#       one failing unit test.
#
#

def factors_of(n):
    """
    Factor an integer into a list where the product of the list is equal to the original number.

    :param n: Integer to factor
    :return: List of integers whose product is equal to value.
    """
    # Use a breakpoint in the code line below to debug your script.

    if not(isinstance(n, int)):
        raise TypeError

    remainder = n
    factors = []
    divisor = 2

    while remainder > 1:
        while remainder % divisor == 0:
            factors.append(divisor)
            remainder /= divisor
        divisor += 1

    return factors


if __name__ == '__main__':
    print(factors_of(1))
