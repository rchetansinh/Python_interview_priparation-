# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#class Solution:
#    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
'''
class Solution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        l1 = len(list1)
        l2 = len(list2)
        third_list = []
        if l1 == 0 and l2 == 0 :
            return list1
        elif l1 == 0:
            list2.sort()
            return list2
        elif l2 == 0:
            list1.sort()
            return list1
        else:
            third_list = list1 + list2
            print(third_list.sort())
            return third_list
'''
class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Check if either of the lists is null
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    # Choose head which is smaller of the two lists
    if l1.val < l2.val:
        temp = head = ListNode(l1.val)
        l1 = l1.next
    else:
        temp = head = ListNode(l2.val)
        l2 = l2.next
    # Loop until any of the list becomes null
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            temp.next = ListNode(l1.val)
            l1 = l1.next
        else:
            temp.next = ListNode(l2.val)
            l2 = l2.next
        temp = temp.next
    # Add all the nodes in l1, if remaining
    while l1 is not None:
        temp.next = ListNode(l1.val)
        l1 = l1.next
        temp = temp.next
    # Add all the nodes in l2, if remaining
    while l2 is not None:
        temp.next = ListNode(l2.val)
        l2 = l2.next
        temp = temp.next
    return head


'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

l1 = [3,7,6,9]
l2 =[2,6,7,9]

#obj = Solution()
#print(obj.mergeTwoLists(l1,l2))

print(mergeTwoLists(l1,l2))