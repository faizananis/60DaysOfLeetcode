# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        prev=head
        temp=head
        while temp!=None:
            if temp.val in s:
                if head==temp:
                    temp=temp.next
                    prev=temp
                    head=temp
                else:
                    temp=temp.next
                    prev.next=temp
            else:
                prev=temp
                temp=temp.next
        return head

                    
