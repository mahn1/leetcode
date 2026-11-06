class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size  # хранимые биты; реальный бит = bits[i] ^ flipped
        self.flipped = 0        # ленивый флаг: была ли нечётная по счёту инверсия
        self.ones = 0           # число реальных единиц

    def fix(self, idx: int) -> None:
        if self.bits[idx] ^ self.flipped == 0:
            self.bits[idx] ^= 1
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx] ^ self.flipped == 1:
            self.bits[idx] ^= 1
            self.ones -= 1

    def flip(self) -> None:
        # Не трогаем массив: меняем трактовку всех битов сразу.
        self.flipped ^= 1
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return "".join("1" if b ^ self.flipped else "0" for b in self.bits)


class NaiveBitset:
    # Эталон для тестов: честный список, flip за O(n).
    def __init__(self, size):
        self.b = [0] * size

    def fix(self, i):
        self.b[i] = 1

    def unfix(self, i):
        self.b[i] = 0

    def flip(self):
        self.b = [1 - v for v in self.b]

    def all(self):
        return all(self.b)

    def one(self):
        return any(self.b)

    def count(self):
        return sum(self.b)

    def toString(self):
        return "".join(map(str, self.b))


if __name__ == "__main__":
    import random

    bs = Bitset(5)
    bs.fix(3)
    bs.fix(1)
    bs.flip()
    assert bs.all() is False
    bs.unfix(0)
    bs.flip()
    assert bs.one() is True
    bs.unfix(0)
    assert bs.count() == 2
    assert bs.toString() == "01010"

    for _ in range(300):
        size = random.randint(1, 8)
        fast, slow = Bitset(size), NaiveBitset(size)
        for _ in range(30):
            op = random.choice(["fix", "unfix", "flip", "all", "one", "count", "toString"])
            args = (random.randrange(size),) if op in ("fix", "unfix") else ()
            assert getattr(fast, op)(*args) == getattr(slow, op)(*args), op
    print("OK")
