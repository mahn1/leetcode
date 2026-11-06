<!-- meta: number=2166; title=Design Bitset; difficulty=Medium; topic=Design, Lazy Flag; url=https://leetcode.com/problems/design-bitset/ -->
# 2166. Design Bitset

[Условие на LeetCode](https://leetcode.com/problems/design-bitset/) · **Medium** · Design, Lazy Flag

Нужно реализовать класс битового набора фиксированного размера: установить бит, сбросить бит,
инвертировать все биты, проверить «все единицы» и «есть хотя бы одна единица», посчитать единицы,
вывести строку битов.

## Ключевая мысль

Дорогая операция только одна: `flip`, которая трогает **все** биты. Её делаем **ленивой**: не переписываем
массив, а переключаем флаг `flipped`. Реальное значение бита: `bits[i] ^ flipped`.

Остальное держится на счётчике `ones` (число реальных единиц):
- `fix` / `unfix` меняют бит и счётчик, **только если** реальное значение действительно меняется;
- `flip`: `ones = size − ones`, потому что все нули стали единицами и наоборот;
- `all`, `one`, `count` сводятся к сравнению `ones`.

`toString` единственная честно идёт по массиву, но по условию вызывается не больше 5 раз.

## Почему именно так

- **Ленивый флаг + счётчик (выбран).** Все операции O(1), кроме `toString` за O(n).
  При 10⁵ вызовов это 10⁵ операций плюс до 5 · 10⁵ на строки.
- **Честный `flip` по массиву**: O(n) на вызов, итого до 10⁵ · 10⁵ = 10¹⁰ при сплошных `flip`. TLE.
- **`count` через `sum(bits)`**: тоже O(n) на вызов, та же проблема. Счётчик обязателен.
- **Два массива (прямой и инвертированный)** и обмен ссылок при `flip`: тоже O(1) на `flip`,
  но каждый `fix`/`unfix` пишет в оба массива, и памяти в 2 раза больше. Флаг проще.
- **Python `int` как битовая маска** (`mask ^= (1 << size) − 1`): `flip` выглядит как одна операция, но это
  длинная арифметика, O(size / 64) на вызов. Выигрыш только по константе, и `fix` тоже создаёт новое число.
- Ловушка: `fix` на бит, который уже 1, не должен увеличивать `ones`. Поэтому сначала проверяем
  реальное значение.

## Сложность

- Время: **O(1)** на `fix`, `unfix`, `flip`, `all`, `one`, `count`; **O(n)** на `toString`.
- Память: **O(n)**.

## Код

```python
class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.flipped = 0
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.bits[idx] ^ self.flipped == 0:
            self.bits[idx] ^= 1
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx] ^ self.flipped == 1:
            self.bits[idx] ^= 1
            self.ones -= 1

    def flip(self) -> None:
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
```
