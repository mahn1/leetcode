from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Бинарный поиск ведём по меньшему массиву: так log(min(m, n)) и j не выходит за границы.
        a, b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        m, n = len(a), len(b)
        half = (m + n + 1) // 2  # размер левой половины (при нечётной сумме она на 1 больше)

        lo, hi = 0, m
        while True:
            i = (lo + hi) // 2  # сколько элементов берём слева из a
            j = half - i        # и сколько из b
            # За краями массива — бесконечности, чтобы сравнения всегда проходили.
            a_left = a[i - 1] if i > 0 else float("-inf")
            a_right = a[i] if i < m else float("inf")
            b_left = b[j - 1] if j > 0 else float("-inf")
            b_right = b[j] if j < n else float("inf")

            if a_left <= b_right and b_left <= a_right:
                # Разрез верный: всё слева <= всего справа.
                if (m + n) % 2:
                    return float(max(a_left, b_left))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            if a_left > b_right:
                hi = i - 1  # взяли из a слишком много
            else:
                lo = i + 1  # взяли из a слишком мало


if __name__ == "__main__":
    import random
    import statistics

    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([], [1]) == 1.0
    assert s.findMedianSortedArrays([2], []) == 2.0
    # Сверка с эталоном на случайных данных.
    for _ in range(2000):
        x = sorted(random.randint(-20, 20) for _ in range(random.randint(0, 8)))
        y = sorted(random.randint(-20, 20) for _ in range(random.randint(0, 8)))
        if x or y:
            assert s.findMedianSortedArrays(x, y) == statistics.median(x + y), (x, y)
    print("OK")
