# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums_list = []
        
        while head:
            nums_list.append(head.val)
            head = head.next
        f,l = 0, len(nums_list) -1
        while f <= l:
            if nums_list[f] != nums_list[l]:
                return False
            f+=1
            l-=1
        return True
        