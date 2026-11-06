class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # S_n = S_{n-1} + "1" + reverse(invert(S_{n-1})), длина 2^n − 1, середина 2^(n−1).
        flip = 0  # сколько раз (по модулю 2) попадали в правую, инвертированную половину
        while n > 1:
            mid = 1 << (n - 1)
            if k == mid:
                return str(1 ^ flip)
            if k > mid:
                # Зеркалим в левую половину: позиция k ↔ (2^n − k), бит инвертирован.
                k = (1 << n) - k
                flip ^= 1
            n -= 1
        return str(flip)  # S_1 = "0"


def build(n: int) -> str:
    s = "0"
    for _ in range(n - 1):
        s = s + "1" + "".join("1" if c == "0" else "0" for c in reversed(s))
    return s


if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthBit(3, 1) == "0"
    assert sol.findKthBit(4, 11) == "1"
    assert build(4) == "011100110110001"
    # Полная сверка со строкой, построенной по определению.
    for n in range(1, 11):
        s = build(n)
        for k in range(1, len(s) + 1):
            assert sol.findKthBit(n, k) == s[k - 1], (n, k)
    print("OK")
