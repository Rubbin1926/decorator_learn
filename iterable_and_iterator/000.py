class NodeIter:
    def __init__(self, node):
        self.curr_code = node

    def __next__(self):
        if self.curr_code is None:
            raise StopIteration  # Raise StopIteration when there are no more elements
        node, self.curr_code = self.curr_code, self.curr_code.next
        return node  # Return the current node


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        return NodeIter(self)  # Return an instance of NodeIter for iteration


node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)

"""
Explanation:

The Node class represents a node in a linked list. Each node has a name attribute and a next attribute, 
which points to the next node in the list.

The Node class also defines the __iter__() method, which makes it an iterable object. 
It returns an instance of the NodeIter class when called.

The NodeIter class represents an iterator object. It keeps track of the current node (self.curr_code) and 
provides the __next__() method for retrieving the next node in the iteration sequence.

In the for loop, we iterate over the Node object node1. Python automatically calls the iter() function on node1, 
obtaining an iterator object from the __iter__() method of the Node class.

The loop then calls __next__() on the iterator object to retrieve each node and prints its name.
If there are no more nodes, the iterator raises a StopIteration exception, which terminates the loop.
"""