"""Convert a linked list to a string"""

class Node():
    """
    Class for Node
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    """
    function, which convert a linked list to a string
    """
    if not isinstance(node, Node) or node is None:
        return 'None'
    result = ''
    while node:
        result += str(node.data)
        if node.next is not None:
            result += ' -> '
        else:
            result += ' -> None'
        node = node.next
    return result

print(stringify(Node(1, Node(2, Node(3)))))
