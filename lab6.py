from linkedlist import value, next, set_next, 
from linkedlist import is_empty, make_node, ll_str

def remove_all(llist, val):    
    """Replace this with your code for Question One ("Missing Links")."""

def empty_stack():
    """This code is provided for you by Cookie Monster. Do not modify it!"""
    return None

def put(stack, val):
    """Replace this with your code for Question Two ("Pushing Up Daisies")."""
    
def peek(stack):
    """Replace this with your code for Question Three ("Peek-a-boo")."""

def pop(stack):
    """Replace this with your code for Question Four ("Once You Pop")."""

def initial_towers(k):
    """This code is provided for you by Cookie Monster. Do not modify it!"""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    left, middle, right = None, None, None
    for i in range(k-1, -1, -1):
        left = put(left, alphabet[i])
    return [left, middle, right]

def example_towers():
    """This code is provided for you by Cookie Monster. Do not modify it!"""    
    left, middle, right = None, None, None
    left = put(left, "E")
    left = put(left, "D")
    middle = put(middle, "B")
    middle = put(middle, "A")
    right = put(right, "C")
    return [left, middle, right]

def towers_str(towers):
    """Replace this with your code for Question Five ("You Can't Stop")."""
    
def print_towers(towers):
    """This code is provided for you by Cookie Monster. Do not modify it!"""    
    print(towers_str(towers))

def which_move(towers, t1, t2):
    """Replace this with your code for Question Six ("One Way Or Another")."""
    
def move(towers, src, dest):
    """Replace this with your code for Question Seven ("Gonna Give You The Slip")."""

def solve(k):
    """Replace this with your code for Question Eight ("Gonna Get Ya")."""

def make_moves(k):
    """This code is provided for you by Cookie Monster. Do not modify it!"""
    towers = initial_towers(k)
    moves = solve(k)
    print('Original towers   : ' + towers_str(towers))
    for next_move in moves:
        move(towers, next_move[0], next_move[1])
        print('After move ' + str(next_move) + ' : ' + towers_str(towers))
        