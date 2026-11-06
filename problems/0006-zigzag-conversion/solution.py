class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Одна строка или строк не меньше, чем символов: зигзага нет.
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        row, step = 0, 1
        for ch in s:
            rows[row].append(ch)
            # На верхней и нижней строке разворачиваемся.
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return "".join("".join(r) for r in rows)


def by_period(s: str, numRows: int) -> str:
    # Эталон через период 2·(numRows − 1): строка r берёт индексы r, cycle − r по модулю cycle.
    if numRows == 1:
        return s
    cycle = 2 * (numRows - 1)
    return "".join(ch for r in range(numRows) for i, ch in enumerate(s) if i % cycle in (r, cycle - r))


if __name__ == "__main__":
    import random
    import string

    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert("A", 1) == "A"
    assert sol.convert("AB", 1) == "AB"
    for _ in range(500):
        t = "".join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 30)))
        k = random.randint(1, 10)
        assert sol.convert(t, k) == by_period(t, k), (t, k)
    print("OK")
