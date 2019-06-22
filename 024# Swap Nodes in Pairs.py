# coding:utf-8

"""
    Given a linked list, swap every two adjacent nodes and return its head.
    You may not modify the values in the list's nodes, only nodes itself may be changed.

    题目地址：https://leetcode.com/problems/swap-nodes-in-pairs/

    Date: 2019/06/20
    By: Fargo
    Difficulty: Medium
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # iteratively
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        second = head.next
        print('second', listNodeToString(second), '\n')
        pre = ListNode(0)
        while head and head.next:
            nxt = head.next
            print('nxt', listNodeToString(nxt))
            head.next = nxt.next
            print('head', listNodeToString(head))
            nxt.next = head
            print('nxt', listNodeToString(nxt))
            pre.next = nxt
            print('pre', listNodeToString(pre))
            head = head.next
            print('head', listNodeToString(head))
            pre = nxt.next
            print('pre', listNodeToString(pre))

            print('second', listNodeToString(second), '\n')
        out = listNodeToString(second)
        return out


    # recursively
    # def swapPairs(self, head):
    #     if not head or not head.next:
    #         return head
    #     second = head.next
    #     head.next = self.swapPairs(second.next)
    #     second.next = head
    #     return second

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


head = LlistToListNode([1,2,3,4])
print(Solution().swapPairs(head))

