from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)  # O(1) на проверку «есть ли число»
        m = k
        # Чисел n, значит среди k, 2k, ..., (n+1)k хотя бы одно отсутствует: цикл конечен.
        while m in seen:
            m += k
        return m


if __name__ == "__main__":
    s = Solution()
    assert s.missingMultiple([8, 2, 3, 4, 6], 2) == 10
    assert s.missingMultiple([1, 4, 7, 10, 15], 5) == 5
    assert s.missingMultiple([1], 1) == 2
    assert s.missingMultiple([3, 3, 6], 3) == 9
    print("OK")
