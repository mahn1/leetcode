from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k — длина уже готового префикса из уникальных элементов.
        # nums[0] всегда уникален, поэтому начинаем с k = 1.
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    s = Solution()
    for given, expected in [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ([7], [7]),
        ([2, 2, 2], [2]),
    ]:
        k = s.removeDuplicates(given)
        assert k == len(expected) and given[:k] == expected
    print("OK")
