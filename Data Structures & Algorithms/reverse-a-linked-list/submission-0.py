class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head


        while curr:
            nxt = curr.next      # save the rest
            curr.next = prev     # flip the arrow
            prev = curr          # slide
            curr = nxt           # slide


        return prev



