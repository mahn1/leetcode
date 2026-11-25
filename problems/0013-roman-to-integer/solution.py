class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        previous = 0
        # Идём справа налево: меньший символ перед большим вычитается,
        # во всех остальных случаях значение прибавляется.
        for ch in reversed(s):
            value = values[ch]
            if value < previous:
                total -= value
            else:
                total += value
            previous = value
        return total


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("CDXLIV") == 444
    assert s.romanToInt("MMMCMXCIX") == 3999
    print("OK")
