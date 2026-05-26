import pytest



@pytest.mark.math_operations
@pytest.mark.smoke
@pytest.mark.regression
class TestSumSuite:

    NUMBER = 5

    @pytest.mark.xfail(reason="Endpoint is not implemented yet. Waiting for it")
    def test_sum(self):
        a = 5
        b = 3
        assert sum([a, b, self.NUMBER]) == 15, "Sum is not equal to 13" # AssertionError
        # if sum([a, b, self.NUMBER]) != 15:
        #     # raise AssertionError("Sum is not equal to 13")
        #     pytest.fail("Sum is not equal to 13")

@pytest.mark.math_operations
@pytest.mark.regression
class TestSumNegativeSuite:

    @pytest.mark.skip(reason="Not actual test for now")
    def test_sum_negative(self):
        a = 5
        b = -3
        assert sum([a, b, self.NUMBER]) != -2



