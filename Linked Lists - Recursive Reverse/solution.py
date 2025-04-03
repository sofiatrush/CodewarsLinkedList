"""Linked Lists - Recursive Reverse"""

class Node(object):
    """class for a node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """function that recursively reverses a linked list."""
    if head is None or head.next is None:
        return head
    rest = reverse(head.next)
    head.next.next = head
    head.next = None
    return rest
