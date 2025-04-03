"""Linked Lists - Alternating Split"""
class Node(object):
    """class for a node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """
    we use a Context object to store and \
    return the state of the two linked lists
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    function that takes one list and divides up \
    its nodes to make two smaller lists. 
    """
    first_head = head
    second_head = head.next

    first = first_head
    second = second_head

    current = head.next.next
    one = True

    while current:
        if one:
            first.next = current
            first = first.next
        else:
            second.next = current
            second = second.next

        current = current.next
        one = not one

    first.next = None
    second.next = None

    return Context(first_head, second_head)
