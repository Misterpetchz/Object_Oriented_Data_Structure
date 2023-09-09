class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)
        return self.root

    def _insert(self, root, val):
        if root is None:
            return Node(val)
        else:
            if val < root.data:
                root.left = self._insert(root.left, val)
            else:
                root.right = self._insert(root.right, val)
        return root

    def delete(self, data):
        self.root = BinarySearchTree._delete(self.root, data)
        return self.root
    
    def _delete(root, val):
        if root is None:
            return root
        if int(val) < int(root.data):
            root.left = BinarySearchTree._delete(root.left, val)
        elif int(val) > int(root.data):
            root.right = BinarySearchTree._delete(root.right, val)
        else:
            if root.left is None or root.right is None:
                root = root.left if root.right is None else root.right
            else:
                temp = root.right
                while temp.left is not None:
                    temp = temp.left
                root.data = temp.data
                root.right = BinarySearchTree._delete(root.right, temp.data)
        return root

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

lst = []
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        lst.append(root.data)
        inOrder(root.right)

tree = BinarySearchTree()
data = input('Enter Input : ').split(',')
for i in data:
    lst = []
    inOrder(tree.root)
    if  i[0] == 'i':
        print('insert', i[2:])
        tree.insert(int(i[2:]))
        printTree90(tree.root)
    elif i[0] == 'd':
        print('delete', i[2:])
        if tree.root is None:
            print('Error! Not Found DATA')
        else:
            if int(i[2:]) not in lst:
                print('Error! Not Found DATA')
                printTree90(tree.root)
            else:
                tree.delete(int(i[2:]))
                printTree90(tree.root)