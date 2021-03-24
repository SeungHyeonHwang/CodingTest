# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        str1 = ''
        while l1 != None : 
            str1 += str(l1.val)
            l1 = l1.next
        str2 = ''
        while l2 != None :
            str2 += str(l2.val)
            l2 = l2.next

        l_sum = int(str1[::-1]) + int(str2[::-1])
        rl = str(l_sum)[::-1]

        output = []
        for i in range(len(rl)):
            output.append(ListNode(int(rl[i])))
        for i in range(len(rl)-1):
            output[i].next = output[i+1]

        return output[0]