import unittest
from maxprofit import MaxProfit


class CheckMaxProfit(unittest.TestCase):
    def test_check_if_valid(self):
        arr = [7, 1, 5, 3, 6, 4]
        res = MaxProfit.maxProfit(arr)
        self.assertTrue(res, 5)

    def test_null_array(self):
        arr = []
        res = MaxProfit.maxProfit(arr)
        self.assertEqual(res, 0)

    def test_descending_prices(self):
        arr = [5, 4, 3, 2, 1]
        res = MaxProfit.maxProfit(arr)
        self.assertTrue(res, 0)


if __name__ == '__main__':
    unittest.main()
