# coding:utf-8

"""
    Given a linked list, remove the n-th node from the end of list and return its head.

    Example: Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.
    Note:  Given n will always be valid.

    题目地址：https://leetcode.com/problems/remove-nth-node-from-end-of-list/

    Date: 2019/06/16
    By: Fargo
    Difficulty: Medium
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        fast = head
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1
        if not fast and count < n:
            return head
        if not fast and count == n:
            return head.next

        slow = head
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        out = listNodeToString(head)
        return out


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


head = LlistToListNode([1,2,3,4,5])
print(Solution().removeNthFromEnd(head, 2))

