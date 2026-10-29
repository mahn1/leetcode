from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Фиктивная голова: не нужно отдельно решать, с какого списка начать.
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        # Остаток уже отсортирован, подвешиваем его целиком.
        tail.next = list1 or list2
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
    assert to_list(s.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(build([]), build([]))) == []
    assert to_list(s.mergeTwoLists(build([]), build([0]))) == [0]
    assert to_list(s.mergeTwoLists(build([5]), build([1, 2, 3]))) == [1, 2, 3, 5]
    print("OK")
