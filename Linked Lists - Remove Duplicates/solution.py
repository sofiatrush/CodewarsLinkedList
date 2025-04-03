"""Linked Lists - Remove Duplicates"""

class Node(object):
    """class for a node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    function which takes a list sorted in increasing \
    order and deletes any duplicate nodes from the list."""
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
