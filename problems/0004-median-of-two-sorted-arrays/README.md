<!-- meta: number=4; title=Median of Two Sorted Arrays; difficulty=Hard; topic=Binary Search; url=https://leetcode.com/problems/median-of-two-sorted-arrays/ -->
# 4. Median of Two Sorted Arrays

[Условие на LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) · **Hard** · Binary Search

Даны два отсортированных массива. Нужно найти медиану их объединения **за O(log(m + n))**,
то есть без слияния.

## Ключевая мысль

Медиана делит общий отсортированный массив на две равные половины. Сливать массивы не нужно,
достаточно найти **разрез**: взять `i` элементов слева из `a` и `j = half - i` из `b`, чтобы:

```
a[i-1] <= b[j]   и   b[j-1] <= a[i]
```

Тогда всё в левой половине не больше всего в правой. Медиана — это `max` левых краёв
(при нечётной сумме) или среднее `max` левых и `min` правых краёв (при чётной).

`j` однозначно задаётся через `i`, поэтому неизвестная всего одна, и она **монотонна**:
- `a[i-1] > b[j]`: из `a` взяли слишком много, сдвигаем `i` влево;
- `b[j-1] > a[i]`: из `a` взяли слишком мало, сдвигаем `i` вправо.

Это бинарный поиск по `i` в диапазоне `[0, m]`.

## Почему именно так

- **Бинарный поиск по разрезу меньшего массива (выбран).** O(log(min(m, n))), что даже лучше
  требуемого. Поиск идёт по **меньшему** массиву не случайно: тогда `j = half - i` всегда попадает
  в `[0, n]`, и индексы не выходят за границы.
- **Бесконечности за краями** (`-inf`, `+inf`) убирают четыре ветки `if` для случаев
  «из массива ничего не взяли» и «взяли весь массив». Сравнения просто всегда проходят.
- **Слияние, как в задаче 21, до середины**: O(m + n). Работает и проходит тесты LeetCode,
  но нарушает явное требование условия. На собеседовании это уровень Easy, а не Hard.
- **`sorted(nums1 + nums2)`**: O((m+n)·log(m+n)), вообще игнорирует отсортированность входов.
- **Поиск k-го элемента** (отбрасывать по k/2 элементов из одного из массивов): тоже
  O(log(m+n)) и классика, но в нём больше граничных случаев и рекурсия. Разрез проще доказать и написать.

## Сложность

- Время: **O(log(min(m, n)))**.
- Память: **O(1)**.

## Код

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        m, n = len(a), len(b)
        half = (m + n + 1) // 2

        lo, hi = 0, m
        while True:
            i = (lo + hi) // 2
            j = half - i
            a_left = a[i - 1] if i > 0 else float("-inf")
            a_right = a[i] if i < m else float("inf")
            b_left = b[j - 1] if j > 0 else float("-inf")
            b_right = b[j] if j < n else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if (m + n) % 2:
                    return float(max(a_left, b_left))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            if a_left > b_right:
                hi = i - 1
            else:
                lo = i + 1
```
