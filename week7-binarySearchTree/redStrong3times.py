class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
        return root

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def multipleThree(self, node, k):
        if node is not None:
            if node.data > k:
                node.data *= 3
            self.multipleThree(node.left, k)
            self.multipleThree(node.right, k)

T = BST()
inp1, inp2 = input('Enter Input : ').split('/')
lst = [int(i) for i in inp1.split()]
value = int(inp2)
for i in lst:
    T.insert(i)
T.printTree(T.root)
print('--------------------------------------------------')
T.multipleThree(T.root, value)
T.printTree(T.root)