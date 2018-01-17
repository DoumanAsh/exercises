#Please implement a program that lists the nodes of a random binary tree by nodes at the same depth.

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self, val):
        self.root = Node(val)

    def add(self, val):
        self._add(val, self.root)

    def _add(self, val, node):
        if val < node.value:
            if node.left != None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right != None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

def print_binary_tree(root_node):
    depth = 0
    current_nodes = [root_node]

    while current_nodes:
        print("Nodes depth {}: ".format(depth), end='')
        next_nodes = list()
        for node in current_nodes:
            print("%s, " % node.value, end='')
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

        print("")
        depth += 1
        current_nodes = next_nodes

def main():
    tree = Tree(10)
    tree.add(7)
    tree.add(8)
    tree.add(5)
    tree.add(2)
    tree.add(1)
    tree.add(15)
    tree.add(17)
    tree.add(20)

    print_binary_tree(tree.root)

main()
