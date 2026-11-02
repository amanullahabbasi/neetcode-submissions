class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # pass 1: count the nodes
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # dummy: so removing the head needs no special case
        dummy = ListNode(0, head)

        # pass 2: walk to the node just BEFORE the target
        slow = dummy
        for _ in range(length - n):
            slow = slow.next

        # skip over the target
        slow.next = slow.next.next
        return dummy.next