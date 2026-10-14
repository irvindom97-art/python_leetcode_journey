"""LeetCode #1 — Two Sum.

Find the indices of two different elements whose sum equals target.
Encontrar los índices de dos elementos distintos cuya suma sea target.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers that add up to target.

    Uses a hash map to store previously seen values and their indices.
    Usa un diccionario para guardar los valores vistos y sus índices.
    """
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value

        if complement in seen:
            return [seen[complement], index]

        seen[value] = index

    # LeetCode guarantees one valid answer for the standard problem.
    # Raise an explicit error if the function is used outside that contract.
    raise ValueError("No two-sum solution exists for the given input.")


if __name__ == "__main__":
    examples = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for nums, target, expected in examples:
        result = two_sum(nums, target)
        print(f"nums={nums}, target={target} -> {result}")
        assert result == expected
