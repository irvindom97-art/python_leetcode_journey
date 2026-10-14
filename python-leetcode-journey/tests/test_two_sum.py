import unittest

from solutions.two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_pair_not_adjacent(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_duplicate_values(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_no_solution_raises_error(self):
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 100)


if __name__ == "__main__":
    unittest.main()
