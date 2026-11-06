from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        # height[node] — высота совершенного поддерева или -1, если оно не совершенное.
        # Пустое поддерево считаем совершенным высоты 0.
        height = {None: 0}
        sizes = []
        # Итеративный post-order: вырожденное дерево на 2000 узлов пробило бы лимит рекурсии.
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
                sizes.append((1 << (hl + 1)) - 1)  # совершенное дерево высоты h: 2^h − 1 узлов
            else:
                height[node] = -1
        if len(sizes) < k:
            return -1
        sizes.sort(reverse=True)
        return sizes[k - 1]


def build(values: List[Optional[int]]) -> Optional[TreeNode]:
    # Дерево из массива в формате LeetCode (обход по уровням, None — пустое место).
    if not values:
        return None
    root = TreeNode(values[0])
    queue, i = deque([root]), 1
    while queue and i < len(values):
        node = queue.popleft()
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = TreeNode(values[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root


if __name__ == "__main__":
    s = Solution()
    assert s.kthLargestPerfectSubtree(build([5, 3, 6, 5, 2, 5, 7, 1, 8, None, None, 6, 8]), 2) == 3
    assert s.kthLargestPerfectSubtree(build([1, 2, 3, 4, 5, 6, 7]), 1) == 7
    assert s.kthLargestPerfectSubtree(build([1, 2, 3, None, 4]), 3) == -1
    assert s.kthLargestPerfectSubtree(build([1]), 1) == 1
    # Вырожденная «палка» из 2000 узлов: рекурсия упала бы, итеративный обход — нет.
    root = node = TreeNode(1)
    for _ in range(1999):
        node.left = TreeNode(1)
        node = node.left
    assert s.kthLargestPerfectSubtree(root, 1) == 1
    assert s.kthLargestPerfectSubtree(root, 2) == -1
    print("OK")
