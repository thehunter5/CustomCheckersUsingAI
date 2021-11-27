
from succesorFn import getSuccesors
from Terminal_test import Terminal_test
from Utility import utility
from minimax import Node
from minimax import max_value
from minimax import min_value
from initStateGenerator import initStateGenerator

def alpha_beta(node, depth, turn):
    if turn == 2:
        infinity = float('inf')
        best_val = -infinity
        beta = infinity
        successors_states = getSuccesors(node.state, node.Name)
        n1 = 1
        if node.Name == 1:
            n1 = 2
        for child in successors_states:
            new_node = Node(n1, child, 0, node)
            node.children.append(new_node)
        best_state = None
        for state in node.children:
            value = min_value(state, best_val, beta, depth, turn)
            if value > best_val:
                best_val = value
                best_state = state
        #print(best_val)
        return best_state
    else:
        infinity = float('inf')
        alpha = -infinity
        best_val = infinity
        successors_states = getSuccesors(node.state, node.Name)
        n1 = 1
        if node.Name == 1:
            n1 = 2
        for child in successors_states:
            new_node = Node(n1, child, 0, node)
            node.children.append(new_node)
        best_state = None
        for state in node.children:
            value = max_value(state, alpha, best_val, depth, turn)
            if value < best_val:
                best_val = value
                best_state = state
        # print(best_val)
        return best_state

def max_value(node, alpha, beta, depth, turn):
    if Terminal_test(node.state) or depth == 0:
        node.val = utility(node.state, turn)
        return node.val
    infinity = float('inf')
    value = -infinity
    successors_states = getSuccesors(node.state, node.Name)
    n1 = 1
    if node.Name == 1:
        n1 = 2
    for child in successors_states:
        new_node = Node(n1, child, 0, node)
        node.children.append(new_node)
    for state in node.children:
        value = max(value, min_value(state, alpha, beta, depth-1, turn))
        alpha = max(alpha, value)
        if value >= beta:
            return value

    return value

def min_value(node, alpha, beta, depth, turn):
    if Terminal_test(node.state) or depth == 0:
        node.val = utility(node.state, turn)
        return node.val
    infinity = float('inf')
    value = infinity
    successors_states = getSuccesors(node.state, node.Name)
    n1 = 1
    if node.Name == 1:
        n1 = 2
    for child in successors_states:
        new_node = Node(n1, child, 0, node)
        node.children.append(new_node)
    for state in node.children:
        value = min(value, max_value(state, alpha, beta, depth-1, turn))
        beta = min(beta, value)
        if value <= alpha:
            return value

    return value
"""
i1=initStateGenerator()
print(i1)
n = Node(1, i1, 0, None)
element = alpha_beta(n, 3)
print(element.state)
"""