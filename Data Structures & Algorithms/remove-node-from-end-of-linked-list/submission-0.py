class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy: a start node, so removing the real head needs no special case
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        # open a gap of n nodes between slow and fast
        for _ in range(n):
            fast = fast.next

        # move both until fast falls off the end: slow is then just before the target
        while fast:
            slow = slow.next
            fast = fast.next

        # skip over the target node
        slow.next = slow.next.next
        return dummy.next