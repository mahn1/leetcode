class Solution:
    def isValid(self, s: str) -> bool:
        # Закрывающая скобка -> какая открывающая должна лежать на вершине стека.
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        # Незакрытые открывающие тоже ошибка.
        return not stack


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([])") is True
    assert s.isValid("([)]") is False
    assert s.isValid("]") is False
    assert s.isValid("((") is False
    print("OK")
