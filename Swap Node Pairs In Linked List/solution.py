"""Swap Node Pairs In Linked List"""
class Node:
    """class for a node"""
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """
    method that swaps each pair of nodes in the list, \
    then returns the head node of the list.
    """
    basic = Node()
    basic.next = head
    prev = basic

    while head and head.next:
        first = head
        second = head.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
        head = first.next

    return basic.next
