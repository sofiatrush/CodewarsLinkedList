"""Linked Lists - Move Node"""

class Node(object):
    """
    Class for a Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    we use a Context object to store and return the state of the two linked lists.
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    function which takes the node from the front of the source \
    list and moves it to the front of the destintation list.
    """
    new_source = source.next
    source.next = dest
    new_dest = source
    return Context(new_source, new_dest)
