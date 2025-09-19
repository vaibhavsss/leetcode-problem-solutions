class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # using two pointer approach

        while curr:
            nxt = curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev