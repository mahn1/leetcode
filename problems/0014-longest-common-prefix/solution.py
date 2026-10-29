from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Идём по столбцам: zip(*strs) отдаёт i-е символы всех строк
        # и сам останавливается на самой короткой строке.
        prefix = []
        for chars in zip(*strs):
            if len(set(chars)) != 1:
                break
            prefix.append(chars[0])
        return "".join(prefix)


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix(["alone"]) == "alone"
    assert s.longestCommonPrefix(["", "abc"]) == ""
    assert s.longestCommonPrefix(["ab", "abc", "abcd"]) == "ab"
    print("OK")
