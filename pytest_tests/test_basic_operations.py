from pytest_tests import basic_operations
import pytest
import sys


#@pytest.mark.skip(reason='I dont want to run this at the moment')
@pytest.mark.skipif(sys.version_info < (3,5), reason='I dont want to run this at the moment')
def test_add_fnc():
    total = basic_operations.add_fnc(4, 5)
    assert total == 9


def test_mult_fnc():
    result = basic_operations.mult_fnc(10, 3)
    assert result == 30

