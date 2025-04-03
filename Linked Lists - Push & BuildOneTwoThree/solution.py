"""Linked Lists - Push & BuildOneTwoThree"""

# from preloaded import Node

'''
Node is defined in preloaded like this:
'''
class Node:
    """
    Class for Node
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    """
    function fot pushing
    """
    return Node(data, head)

def build_one_two_three():
    """
    The buildOneTwoThree function should create \
    and return a linked list with three nodes: \
    1 -> 2 -> 3 -> null
    """
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
