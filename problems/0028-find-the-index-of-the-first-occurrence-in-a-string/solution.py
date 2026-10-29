class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Префикс-функция (KMP): lps[i] — длина наибольшего собственного префикса
        # needle[:i + 1], который одновременно является его суффиксом.
        lps = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
            lps[i] = j

        # Поиск: при несовпадении не откатываем i, а сдвигаем j по lps.
        j = 0
        for i, ch in enumerate(haystack):
            while j and ch != needle[j]:
                j = lps[j - 1]
            if ch == needle[j]:
                j += 1
                if j == len(needle):
                    return i - j + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.strStr("sadbutsad", "sad") == 0
    assert s.strStr("leetcode", "leeto") == -1
    assert s.strStr("aaaaab", "aab") == 3
    assert s.strStr("mississippi", "issip") == 4
    assert s.strStr("a", "a") == 0
    assert s.strStr("abc", "abcd") == -1
    print("OK")
