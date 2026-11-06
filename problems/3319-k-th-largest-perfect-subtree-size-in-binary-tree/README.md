<!-- meta: number=3319; title=K-th Largest Perfect Subtree Size in Binary Tree; difficulty=Medium; topic=Tree, DFS, Sorting; url=https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/ -->
# 3319. K-th Largest Perfect Subtree Size in Binary Tree

[Условие на LeetCode](https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/) · **Medium** · Tree, DFS, Sorting

Дано двоичное дерево и число `k`. Среди всех **совершенных** поддеревьев (у каждого внутреннего узла
два ребёнка, все листья на одном уровне) нужно найти размер `k`-го по величине, или `-1`, если их меньше `k`.

## Ключевая мысль

Поддерево с корнем `v` совершенное ⇔ **оба** его ребёнка — совершенные поддеревья **одной высоты**.
Это проверяется снизу вверх, то есть обходом **post-order**: каждый узел возвращает
- высоту `h`, если его поддерево совершенное;
- `-1`, если нет.

Пустое поддерево считаем совершенным высоты 0. Тогда лист (`0 == 0`) получает высоту 1, и
отдельного случая для листьев не нужно.

Размер совершенного дерева высоты `h` известен заранее: **`2^h − 1`**. Считать узлы не нужно.
Собираем размеры всех совершенных поддеревьев, сортируем по убыванию и берём `k`-й.

## Почему именно так

- **Один post-order обход (выбран).** Каждый узел обрабатывается один раз, ответ ребёнка
  переиспользуется родителем. O(n) на обход и O(n log n) на сортировку.
- **Итеративный обход вместо рекурсии.** В дереве до 2000 узлов, а лимит рекурсии в Python около 1000.
  Вырожденная «палка» уронит рекурсивное решение с `RecursionError`. Можно поднять лимит через
  `sys.setrecursionlimit`, но итеративный обход надёжнее. Тест на палку из 2000 узлов есть в `solution.py`.
- **Проверять каждый узел отдельно** (запускать от него обход и смотреть, совершенно ли поддерево):
  O(n²) в худшем случае. Post-order даёт тот же результат за один проход.
- **Куча размера `k` вместо сортировки**: O(n log k). Но совершенных поддеревьев не больше n = 2000,
  и сортировка проще и не медленнее на практике.
- **Подсчёт размеров** (вернуть число узлов и сравнить с `2^h − 1`) тоже работает, но сравнение
  высот детей проще и ничего не нужно считать дополнительно.

## Сложность

- Время: **O(n log n)**: обход O(n) плюс сортировка не больше n размеров.
- Память: **O(n)** под стек обхода, словарь высот и список размеров.

## Код

```python
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        height = {None: 0}
        sizes = []
        stack = [(root, False)]
        while stack:
            node, children_done = stack.pop()
            if node is None:
                continue
            if not children_done:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
                continue
            hl, hr = height[node.left], height[node.right]
            if hl == hr != -1:
                height[node] = hl + 1
                sizes.append((1 << (hl + 1)) - 1)
            else:
                height[node] = -1
        if len(sizes) < k:
            return -1
        sizes.sort(reverse=True)
        return sizes[k - 1]
```
