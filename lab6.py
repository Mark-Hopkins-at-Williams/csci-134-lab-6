from linkedlist import make_node, head, value, next, set_head, set_next, is_empty
from linkedlist import lstr
from linkedlist import append
from linkedlist import make_empty_linked_list


def sum_up(ls):
    """ Replace this with your code for Question One ("Add Em Up, Cookie!"). """


def remove_all(ls, value):
    """ Replace this with your code for Question Two ("One of These Things"). """


def push(stack, element):
    """ Replace this with your code for Question Three ("Six Feet Under"). """


def peek(stack):
    """ Replace this with your code for Question Four ("Don't Look"). """


def pop(stack):
    """ Replace this with your code for Question Five ("Once You Pop"). """


def initial_towers(k):
    """ This code is provided for you by Cookie Monster. Do not modify it!"""
    left, middle, right = make_empty_linked_list(), make_empty_linked_list(), make_empty_linked_list()
    for i in range(k, 0, -1):
        push(left, i)
    return [left, middle, right]


def tstr(towers):
    """ Replace this with your code for Question Six ("You Can't Stop"). """


def which_move(towers, t1, t2):
    """ Replace this with your code for Question Seven ("One Way or Another"). """


def move(towers, src, dest):
    """ Replace this with your code for Question Eight ("Gonna Give You The Slip"). """


def solve(k):
    """ Replace this with your code for Question Nine ("Gonna Get Ya"). """


def make_moves(k):
    """ This code is provided for you by Cookie Monster. Do not modify it!"""
    towers = initial_towers(k)
    moves = solve(k)
    print('Original towers   : ' + tstr(towers))
    node = head(moves)
    while node != None: 
        next_move = value(node)       
        move(towers, next_move[0], next_move[1])
        print('After move ' + str(next_move) + ' : ' + tstr(towers))
        node = next(node)
