# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy
        
        for _ in range(n+1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next

        return dummy.next
    
if __name__ == "__main__":
    # Example usage:
    sol = Solution()
    
    # Creating a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    n = 2
    new_head = sol.removeNthFromEnd(head, n)
    
    # Print the modified linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # Output should be: 1 -> 2 -> 3 -> 5