class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Окно s[left:right + 1] всегда без повторов.
        # last[ch] — индекс последнего вхождения символа ch.
        last = {}
        left = best = 0
        for right, ch in enumerate(s):
            # Повтор внутри окна: прыгаем левой границей сразу за прошлое вхождение.
            # Проверка >= left отсекает старые вхождения, оставшиеся левее окна.
            if last.get(ch, -1) >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring("abba") == 2
    assert s.lengthOfLongestSubstring(" ") == 1
    print("OK")
