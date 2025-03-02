"""Code for linked lists."""

def empty_linked_list():
    """Creates an empty linked list."""
    return None

def make_node(val, nxt):
    """Creates a linked list node."""
    return [val, nxt]

def value(node):
    """Returns the value of a linked list node."""
    return node[0]

def next(node):
    """Returns the next node of a linked list node."""
    return node[1]

def set_value(node, val):
    """Resets the value of a linked list node."""
    node[0] = val

def set_next(node, next_node):
    """Resets the next node of a linked list node."""
    node[1] = next_node

def is_empty(node):
    """Returns whether a linked list is empty."""
    return node == None

def convert_to_linked_list(ls):
    """Converts a Python list to a linked list."""
    head = None
    for value in ls[::-1]:
        head = [value, head]
    return head

def ll_str(node):
    """Represents a linked list as a string."""
    if is_empty(node):
        return "<>"
    else:
        prefix = "<"        
        while not is_empty(next(node)):
            prefix += str(value(node)) + ", "
            node = next(node)        
        return prefix + str(value(node)) + ">"

def ll_print(linked_list):
    """Convenience function for printing a linked list."""
    print(ll_str(linked_list))

