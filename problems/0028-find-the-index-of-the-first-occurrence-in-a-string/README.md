<!-- meta: number=28; title=Find the Index of the First Occurrence in a String; difficulty=Easy; topic=String Matching (KMP); url=https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ -->
# 28. Find the Index of the First Occurrence in a String

[Условие на LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) · **Easy** · String Matching (KMP)

Нужно найти индекс первого вхождения строки `needle` в строку `haystack` или вернуть `-1`, если вхождения нет.

## Ключевая мысль

Наивный поиск при несовпадении откатывается назад по `haystack` и начинает сравнение заново.
KMP никогда не откатывает указатель по тексту: если совпало `j` символов, а следующий не совпал,
то уже известно, что последние `j` символов текста равны `needle[:j]`. Значит, можно сразу
продолжить с самого длинного префикса `needle`, который одновременно является суффиксом
`needle[:j]`. Эти длины заранее считаются в **префикс-функции** `lps`.

Пример: `needle = "aab"`, текст `"aaaab"`. После `"aa"` пришла `a` вместо `b`. Мы не начинаем
заново, а сдвигаемся на `lps[1] = 1`: одна `a` уже совпала.

## Почему именно так

- **KMP (выбран).** Гарантированно O(n + m) в худшем случае. Каждая итерация либо двигает `i`
  вперёд, либо уменьшает `j`, а `j` растёт не больше чем на 1 за шаг. Поэтому вложенный `while`
  в сумме даёт O(n), а не O(n·m).
- **Наивный перебор / срезы** (`haystack[i:i+m] == needle` для каждого `i`): O(n·m) в худшем
  случае, например `"aaaa…ab"` и `"aa…ab"`. Для ограничений до 10⁴ это 10⁸ операций, на грани.
- **`haystack.find(needle)`**: однострочник, и в продакшене правильный выбор, потому что в CPython
  он написан на C и быстрый. Но на собеседовании ждут, что вы покажете алгоритм, а не вызов функции.
- **Rabin-Karp** (rolling hash): в среднем O(n + m), но при коллизиях хешей нужна повторная
  проверка, и худший случай O(n·m). KMP детерминирован и не зависит от выбора хеша.

## Сложность

- Время: **O(n + m)**: O(m) на префикс-функцию и O(n) на поиск.
- Память: **O(m)** под массив `lps`.

## Код

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
            lps[i] = j

        j = 0
        for i, ch in enumerate(haystack):
            while j and ch != needle[j]:
                j = lps[j - 1]
            if ch == needle[j]:
                j += 1
                if j == len(needle):
                    return i - j + 1
        return -1
```
