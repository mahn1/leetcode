from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # O(1) на проверку «есть ли число»
        for num in nums:
            if num in seen:
                # Нашли число, которое уже встречалось — дубликат.
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) == True
    assert s.containsDuplicate([1, 2, 3, 4]) == False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert s.containsDuplicate([7]) == False
    print("OK")