from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # low — минимальная цена слева от текущего дня, то есть лучшая покупка
        # для любой продажи сегодня. Продажа строго после покупки: минимум
        # обновляем после подсчёта прибыли.
        low = prices[0]
        best = 0
        for price in prices:
            best = max(best, price - low)
            low = min(low, price)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([2, 4, 1]) == 2
    assert s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 4
    print("OK")
