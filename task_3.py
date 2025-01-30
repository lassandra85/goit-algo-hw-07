class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
    

    def sum_tree(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return node.key + self.sum_tree(node.left) + self.sum_tree(node.right)

# Приклад використання
bst = BST()
numbers = [20, 10, 30, 5, 15, 25, 35]

for num in numbers:
    bst.insert(num)


print("Сума всіх значень у дереві:", bst.sum_tree())
