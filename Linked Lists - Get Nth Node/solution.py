"""Linked Lists - Get Nth"""

# from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    function that takes a linked list and an integer \
    index and returns the node stored at the Nth \
    index position.
    """
    result = ''
    while node:
        result += str(node.data)
        if node.next is not None:
            result += ' -> '
        else:
            result += ' -> None'
        node = node.next
    lst = result.split(' -> ')
    return Node(int(lst[index]))
