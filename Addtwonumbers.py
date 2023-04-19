# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Optional:
#     def __init__(self, sequence):
#         self.head = ListNode(sequence[0])
#         current = self.head
#         for i in sequence[1:]:
#             current.next = ListNode(i)
#             current = current.next
#
#
# a = [1,2,3]
# li = Optional(a)
# current = li.head
# while current is not None:
#     print(current.val)
#     current = current.next


class Solution:
    def addTwoNumber(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = n = ListNode(0)
        num1 = num2 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        res = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        for i in res:
            d.next = ListNode(i)
            d = d.next
        return n.next

l1 = [2,4,3]
l2 = [5,6,4]
result = Solution().addTwoNumber(l1, l2)
print(result)