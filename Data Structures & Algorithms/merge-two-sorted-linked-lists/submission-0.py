class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy: a throwaway start node, so the first real node needs no special case
        dummy = ListNode()
        # tail: the last node of the merged list so far
        tail = dummy

        while list1 and list2:
            # hook the smaller front node onto the merged list, then advance that list
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # slide tail onto the node we just attached
            tail = tail.next

        # at most one list still has nodes: attach all of it at once
        tail.next = list1 or list2
        # skip the dummy
        return dummy.next