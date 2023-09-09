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

    def findMax(self):
        if self.root == None:
            return None
        else:
            cur = self.root
            while cur.right is not None:
                cur = cur.right
            return cur.data
        
    def findMin(self):
        if self.root == None:
            return None
        else:
            cur = self.root
            while cur.left is not None:
                cur = cur.left
            return cur.data

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)
T.printTree(T.root)
print('--------------------------------------------------')
print('Min :', T.findMin())
print('Max :', T.findMax())