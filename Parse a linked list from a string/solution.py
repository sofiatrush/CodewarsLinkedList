"""Parse a linked list from a string"""

class Node:
    """
    Class for Node
    """
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    """
    function, which parses a linked list from a string
    """
    lst = s.split(' -> ')
    lst.remove('None')
    if len(lst) == 0:
        return None

    head = Node(int(lst[0]))
    current = head

    for el in lst[1:]:
        current.next = Node(int(el))
        current = current.next

    return head

print(linked_list_from_string("0 -> 1 -> 4 -> 9 -> 16 -> None")) 
