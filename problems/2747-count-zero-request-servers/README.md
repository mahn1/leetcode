<!-- meta: number=2747; title=Count Zero Request Servers; difficulty=Medium; topic=Sliding Window, Sorting; url=https://leetcode.com/problems/count-zero-request-servers/ -->
# 2747. Count Zero Request Servers

[Условие на LeetCode](https://leetcode.com/problems/count-zero-request-servers/) · **Medium** · Sliding Window, Sorting

Есть `n` серверов и журнал запросов вида «сервер, время». Для каждого запроса `q` нужно сказать,
сколько серверов **не получили ни одного** запроса в отрезке времени `[q - x, q]`.

## Ключевая мысль

Все отрезки имеют **одинаковую длину** `x`. Если обходить запросы по возрастанию `q`, то обе границы
отрезка только растут, а значит отрезки образуют **скользящее окно** по отсортированным логам.

Внутри окна храним:
- `cnt[s]`: сколько логов сервера `s` попало в окно;
- `active`: сколько серверов имеют `cnt > 0`.

Лог входит в окно справа: если `cnt` был 0, `active += 1`. Лог выходит слева: если `cnt` стал 0,
`active -= 1`. Ответ на запрос: `n - active`.

Порядок запросов во входе произвольный, поэтому сортируем **индексы** запросов и пишем ответ
в `ans[исходный индекс]`. Это приём **офлайн-обработки** запросов: ответы считаются в удобном
порядке и раскладываются по исходным местам.

## Почему именно так

- **Офлайн + скользящее окно (выбран).** Каждый лог один раз входит в окно и один раз выходит.
  Итого O(L log L + Q log Q) из-за сортировок, а сам проход линейный.
- **Наивно, для каждого запроса пройти все логи** и собрать `set` серверов: O(Q·L) = 10¹⁰ при
  максимальных ограничениях. Получится TLE.
- **Бинарный поиск по логам** для каждого запроса находит границы отрезка за O(log L), но
  уникальные серверы внутри всё равно придётся считать за длину отрезка. В худшем случае те же O(Q·L).
- **`set` активных серверов вместо счётчиков** не работает: если у сервера два лога в окне и
  один вышел, сервер ещё активен. Нужна кратность, то есть `cnt`.
- Обрати внимание на границы: отрезок **включительный**, поэтому справа добавляем `t <= q`,
  а слева удаляем только `t < q - x`.

## Сложность

- Время: **O(L log L + Q log Q + n)**, где L — число логов, Q — число запросов.
- Память: **O(n + Q)** под счётчики, порядок запросов и ответ.

## Код

```python
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        order = sorted(range(len(queries)), key=queries.__getitem__)

        cnt = [0] * (n + 1)
        active = 0
        left = right = 0
        ans = [0] * len(queries)
        for qi in order:
            start, end = queries[qi] - x, queries[qi]
            while right < len(logs) and logs[right][1] <= end:
                server = logs[right][0]
                if cnt[server] == 0:
                    active += 1
                cnt[server] += 1
                right += 1
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                cnt[server] -= 1
                if cnt[server] == 0:
                    active -= 1
                left += 1
            ans[qi] = n - active
        return ans
```
