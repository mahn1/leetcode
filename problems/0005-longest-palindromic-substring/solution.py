class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> tuple:
            # Расширяемся, пока края совпадают; возвращаем границы последнего палиндрома.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right

        start, end = 0, 1
        for c in range(len(s)):
            # Два вида центров: символ (нечётная длина) и промежуток (чётная).
            for lo, hi in (expand(c, c), expand(c, c + 1)):
                if hi - lo > end - start:
                    start, end = lo, hi
        return s[start:end]


if __name__ == "__main__":
    import random

    s = Solution()
    assert s.longestPalindrome("babad") in ("bab", "aba")
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("abacdfgdcaba") == "aba"
    # Сверка длины с перебором.
    for _ in range(500):
        t = "".join(random.choice("ab") for _ in range(random.randint(1, 12)))
        best = max(
            (t[i:j] for i in range(len(t)) for j in range(i + 1, len(t) + 1) if t[i:j] == t[i:j][::-1]),
            key=len,
        )
        got = s.longestPalindrome(t)
        assert got == got[::-1] and got in t and len(got) == len(best), t
    print("OK")
