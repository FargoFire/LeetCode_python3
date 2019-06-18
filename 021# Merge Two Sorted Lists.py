# coding:utf-8

"""
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
    the nodes of the first two lists.

    Example:Input: 1->2->4, 1->3->4
            Output: 1->1->2->3->4->4

    题目地址：https://leetcode.com/problems/merge-two-sorted-lists/

    Date: 2019/06/18
    By: Fargo
    Difficulty: Easy
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_new_head = ListNode(0)
        l_new = l_new_head

        while l1 != None or l2 != None:
            if l1 == None:
                l_new.next = l2
                l_new = l_new.next
                l2 = l2.next
            elif l2 == None:
                l_new.next = l1
                l_new = l_new.next
                l1 = l1.next
            elif l1.val < l2.val:
                l_new.next = l1
                l_new = l_new.next
                l1 = l1.next
            else:
                l_new.next = l2
                l_new = l_new.next
                l2 = l2.next

        l_new_out = listNodeToString(l_new_head.next)
        return l_new_out


def LlistToListNode(numbers):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot

    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


l1 = LlistToListNode([1,2,4])
l2 = LlistToListNode([1,3,4])
print(Solution().mergeTwoLists(l1, l2))

