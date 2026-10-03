# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #arpan-star
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        def reverse_linked_list(head):
            prev = None
            curr = head

            while curr is not None:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        def linked_list_to_int_math(head):
            result = 0
            current = head
            
            while current:
                result = result * 10 + current.val
                current = current.next
                
            return result

        reverse_l1 = reverse_linked_list(l1)
        reverse_l2 = reverse_linked_list(l2)
        addition = linked_list_to_int_math(reverse_l1) + linked_list_to_int_math(reverse_l2)
        
        array = []
        for i in str(addition):
            array.append(int(i))
        array.reverse()

        dummy = ListNode(0)
        current = dummy

        for i in array:
            current.next = ListNode(i)
            current = current.next
        return dummy.next
       
        
