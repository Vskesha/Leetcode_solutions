from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = None
        r = f = head
        while f and f.next:
            f = f.next.next
            r.next, r, l = l, r.next, r
        if f:
            r = r.next
        while l:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True


class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        first = head
        second = head.next
        fast = head.next
        first.next = None

        while fast and fast.next:
            fast, first, second, first.next = fast.next.next, second, second.next, first

        if not fast:
            first = first.next

        while first:
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                return False
        return True


class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]


def to_linked_list(arr: list):
    nxt = None
    for n in reversed(arr):
        curr = ListNode(n, nxt)
        nxt = curr
    return nxt


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.isPalindrome(head=to_linked_list([1, 2, 2, 1])) is True
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.isPalindrome(head=to_linked_list([1, 2])) is False
    print("OK")


if __name__ == "__main__":
    test()
