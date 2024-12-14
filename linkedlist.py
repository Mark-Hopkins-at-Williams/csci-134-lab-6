"""Operations on linked list nodes."""

def make_node(x, y):
    return [x, y]


def value(p):
    return p[0]


def next(p):
    return p[1]


def set_value(p, val):
    p[0] = val


def set_next(p, node):
    p[1] = node


"""Operations on linked lists."""

def make_empty_linked_list():
    return [None]


def is_empty(ls):
    return ls[0] == None


def head(ls):
    return ls[0]


def set_head(ls, node):
    ls[0] = node


def append(ls, value):
    if is_empty(ls):
        set_head(ls, make_node(value, None))
    else:
        node = head(ls)
        while next(node) != None:
            node = next(node)
        set_next(node, make_node(value, None))
    

def lstr(ls):
    result = "<"
    node = head(ls)
    while node != None:
        result = result + str(value(node)) + ", "
        node = next(node)
    if result[-1] == ' ':
        result = result[:-2]
    result = result + ">"
    return result


def lprint(ls):
    print(lstr(ls))



