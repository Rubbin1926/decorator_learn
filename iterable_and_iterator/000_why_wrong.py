class NodeIter:
    def __init__(self, node):
        self.curr_code = node

    def __next__(self):
        if self.curr_code is None:
            raise StopIteration
        node, self.curr_code = self.curr_code, self.curr_code.next
        return node


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        return NodeIter(self)


node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
node1.next = node2
node2.next = node3

it = iter(node1)
first = next(it)

for node in it:
    print(node.name)

"""
Traceback (most recent call last):
  File "xxx.py", line xx, in <module>
    for node in it:
TypeError: 'NodeIter' object is not iterable
"""