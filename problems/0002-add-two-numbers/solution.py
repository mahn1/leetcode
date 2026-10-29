from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Сложение в столбик: цифры уже идут от младшего разряда.
        dummy = tail = ListNode()
        carry = 0
        # Крутимся, пока есть цифры или незаписанный перенос (999 + 1).
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next
        return dummy.next


def build(values: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.addTwoNumbers(build([2, 4, 3]), build([5, 6, 4]))) == [7, 0, 8]
    assert to_list(s.addTwoNumbers(build([0]), build([0]))) == [0]
    assert to_list(s.addTwoNumbers(build([9] * 7), build([9] * 4))) == [8, 9, 9, 9, 0, 0, 0, 1]
    assert to_list(s.addTwoNumbers(build([5]), build([5]))) == [0, 1]
    print("OK")
