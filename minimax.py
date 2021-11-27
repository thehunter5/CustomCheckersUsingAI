
from succesorFn import getSuccesors
from Terminal_test import Terminal_test
from Utility import utility
from initStateGenerator import initStateGenerator
#from Terminal_test import terminal_states

class Node:
    def __init__(self, name, state, value, parent):
        self.Name = name
        self.val = value
        self.parent = parent
        self.state = state
        self.children = []

    def addChild(self, childNode):
        self.children.append(childNode)

def minimax(node,depth, starter):
    recStack=[]
    if starter == 2:
        best_val = max_value(node, recStack, depth, starter)
    else:
        best_val = min_value(node, recStack, depth, starter)
    #successors = getSuccesors(node.state, node.Name)
    #print(best_val)
    best_move = None
    for elem in node.children:
        if elem.val == best_val:
            best_move = elem
            break
    return best_move

def max_value(node, recStack, depth, starter):
    infinity = float('inf')
    """if node.state in recStack:
        return infinity
    recStack.append(node.state)"""
    if node.val != 0:
        #recStack.remove(node.state)
        return node.val
    if Terminal_test(node.state) or depth == 0:
        #recStack.remove(node.state)
        node.val = utility(node.state, starter)
        return node.val
    #infinity = float('inf')
    max_val = -infinity
    successors_states = getSuccesors(node.state, node.Name)
    n1 = 1
    if node.Name == 1:
        n1 = 2
    for child in successors_states:
        #print(child)
        #if child not in recStack:
            #recStack.append(child)
        new_node = Node(n1, child, 0, node)
        node.children.append(new_node)
    #print("--------------------------")
    for state in node.children:
        #print(state.state)

        max_val = max(max_val, min_value(state, recStack, depth-1, starter))
    node.val = max_val
    #print(node.val)
    #recStack.remove(node.state)
    return max_val

def min_value(node, recStack, depth, starter):
    infinity = float('inf')
    """if node.state in recStack:
        return -infinity
    recStack.append(node.state)"""
    if node.val != 0:
        #recStack.remove(node.state)
        return node.val
    if Terminal_test(node.state) or depth == 0:
        #recStack.remove(node.state)
        node.val = utility(node.state, starter)
        return node.val
    #infinity = float('inf')
    min_val = infinity
    successors_states = getSuccesors(node.state, node.Name)
    n1 = 1
    if node.Name == 1:
        n1 = 2
    for child in successors_states:
        #if child not in recStack:
            #recStack.append(child)
        new_node = Node(n1, child, 0, node)
        node.children.append(new_node)
    for state in node.children:
        min_val = min(min_val, max_value(state, recStack, depth-1, starter))
    node.val = min_val
   # recStack.remove(node.state)
    return min_val
"""
i1 = initStateGenerator()
print(i1)
n = Node(1, i1, 0, None)
element = minimax(n, 3)
if element != None:
    print(element.state)
"""