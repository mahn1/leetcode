from functools import lru_cache


class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2
        diff = 0   # сумма левой половины минус сумма правой
        q_diff = 0  # '?' слева минус '?' справа
        for i, ch in enumerate(num):
            sign = 1 if i < half else -1
            if ch == "?":
                q_diff += sign
            else:
                diff += sign * int(ch)
        # Нечётное число '?': последний ход у Алисы, и она всегда может испортить равенство.
        if num.count("?") % 2:
            return True
        # Чётное: Боб выигрывает, только если каждая пара «?» вносит ровно 9 в нужную сторону,
        # т. е. diff + 9 * q_diff / 2 == 0.
        return 2 * diff + 9 * q_diff != 0


def brute(num: str) -> bool:
    # Честный минимакс по состоянию (diff, '?' слева, '?' справа).
    # Чей ход, определяется числом уже сделанных ходов: чётное — ходит Алиса.
    half = len(num) // 2
    left, right = num[:half], num[half:]
    diff = sum(int(c) for c in left if c != "?") - sum(int(c) for c in right if c != "?")
    total = num.count("?")

    @lru_cache(maxsize=None)
    def alice_wins(d: int, ql: int, qr: int) -> bool:
        if ql == qr == 0:
            return d != 0
        alice_turn = (total - ql - qr) % 2 == 0
        outcomes = []
        for digit in range(10):
            if ql:
                outcomes.append(alice_wins(d + digit, ql - 1, qr))
            if qr:
                outcomes.append(alice_wins(d - digit, ql, qr - 1))
        return any(outcomes) if alice_turn else all(outcomes)

    return alice_wins(diff, left.count("?"), right.count("?"))


if __name__ == "__main__":
    import itertools

    s = Solution()
    assert s.sumGame("5023") is False
    assert s.sumGame("25??") is True
    assert s.sumGame("?3295???") is False
    # Полный перебор строк длины 2 и 4 из символов {0, 4, 9, ?} и случайные длины 6.
    for length in (2, 4):
        for chars in itertools.product("049?", repeat=length):
            t = "".join(chars)
            assert s.sumGame(t) == brute(t), t
    for t in ("??????", "9?????", "??9???", "0?0?9?", "?9?0??", "99??00"):
        assert s.sumGame(t) == brute(t), t
    print("OK")
