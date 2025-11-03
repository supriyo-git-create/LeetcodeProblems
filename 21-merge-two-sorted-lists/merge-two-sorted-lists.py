class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode()
        tmp1, tmp2, tmp3 = l1, l2, head

        while tmp1 is not None and tmp2 is not None:
            if tmp1.val <= tmp2.val:
                tmp3.next = tmp1
                tmp1 = tmp1.next
            else:
                tmp3.next = tmp2
                tmp2 = tmp2.next
            tmp3 = tmp3.next#also move the pointer to the newly added node

        if tmp1 is not None:#leftover gulo add hoe jabe 
            tmp3.next = tmp1#dummy node tae tmp.next e baki leftover gulo chole asbe
        if tmp2 is not None:
            tmp3.next = tmp2

        return head.next# return kore debe dummy node ta k
