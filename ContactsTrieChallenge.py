# HackerRank Challenge requiring Tries to efficiently add/count contacts
# The trick is to accumulate totals on the children nodes so no recursion is required

class Node():
    
    # This explicitely declares what slots your object will have, saving memory due to allocation
    __slots__ = ['value', 'children']

    def __init__(self):
       # Note that using dictionary for children (as in this implementation) would not allow lexicographic sorting mentioned in the next section (Sorting),
       # because ordinary dictionary would not preserve the order of the keys
        self.children = {}  # mapping from character ==> Node
        self.value = 0

def startsWith(node, prefix):
    i = 0
    for letter in prefix:
        if letter in node.children:
            node = node.children[letter]
        else:
            return 0
        i += 1
    return node.value if i == len(prefix) else 0

def insert(root, string, value):
    node = root
    i = 0
    while i < len(string):
        if string[i] in node.children:
            node = node.children[string[i]]
            node.value += 1
            i += 1
        else:
            break
    # append new nodes for the remaining characters, if any
    while i < len(string):
        node.children[string[i]] = Node()
        node = node.children[string[i]]
        node.value += 1
        i += 1
    # store value in the terminal node
    node.value = value

root = Node()

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        insert(root,contact,1)
    elif op == 'find':
        print(startsWith(root,contact))
