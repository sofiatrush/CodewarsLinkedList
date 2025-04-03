"""Linked Lists - Sorted Insert"""

class Node(object):
    """class for a node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """
    function which inserts a node into the correct \
    location of a pre-sorted linked list which is \
    sorted in ascending order. 
    """
    current = head
    new_node = Node(data)
    if head is None or data < head.data:
        new_node.next = head
        return new_node
    while current.next and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head
