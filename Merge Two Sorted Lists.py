# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two
# lists.
#
# Return the head of the merged linked list.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:

        mergedList = ListNode(0)
        pointer = mergedList

        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                pointer = list1
                list1 = list1.next
            else:
                pointer.next = list2
                pointer = list2
                list2 = list2.next
        if list1:
            pointer.next = list1
        else:
            pointer.next = list2
        return mergedList.next
