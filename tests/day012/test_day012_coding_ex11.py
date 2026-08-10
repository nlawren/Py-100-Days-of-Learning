import pytest

from day012.day012_coding_ex11 import is_prime

PRIMES = [2, 3, 5, 7, 11, 13, 97, 7919]
NON_PRIMES = [-7, 0, 1, 4, 9, 100, 7917]


@pytest.mark.parametrize("number", PRIMES)
def test_primes(number):
    assert is_prime(number) is True


@pytest.mark.parametrize("number", NON_PRIMES)
def test_non_primes(number):
    assert is_prime(number) is False
