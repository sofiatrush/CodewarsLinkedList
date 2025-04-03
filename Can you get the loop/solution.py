"""Can you get the loop?"""
class Node:
    """class for a node"""
    def __init__(self, next=None):
        self.next = next

def loop_size(node):
    """
    this function determines the length of the loop
    """
    visited = {}
    step = 0

    while node not in visited:
        visited[node] = step
        node = node.next
        step += 1
    cycle_length = step - visited[node]
    return cycle_length
