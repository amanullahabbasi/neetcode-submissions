class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # both runners start on the first node
        slow = head
        fast = head

        # fast needs room to jump two nodes: check fast, then fast.next, in that order
        while fast and fast.next:
            slow = slow.next            # one step
            fast = fast.next.next       # two steps
            # same node (not just the same value): fast has lapped slow
            if slow is fast:
                return True

        # fast reached the end, so the list has an end: no cycle
        return False