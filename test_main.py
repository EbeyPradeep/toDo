import pytest

from main import *


class Test:
    fame = [('1', 1), ('2', 2), ('3', 3)]

    @pytest.mark.parametrize("test,test2", fame)
    def test_important_awsome(self, test, test2):
        assert [important_awsome(test), 'hello'] == [test2, 'hello']

    def test_important_cool(self):
        assert True
