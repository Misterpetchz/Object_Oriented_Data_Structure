class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, str):
        self.root = self._createTree(str)

    def _createTree(self, str):
        stack = []
        for char in str:
            if char in '+-*/':
                sec = stack.pop()
                first = stack.pop()
                cur = Node(char)
                cur.left = first
                cur.right = sec
                stack.append(cur)
            else:
                stack.append(Node(char))
        return stack.pop()

    def printTree(self):
        self._printTree(self.root)

    def _printTree(self, node, level=0):
        if node is not None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self._printTree(node.left, level + 1)

    def preOrder(self):
        print(self._preOrder(self.root))

    def _preOrder(self, root):
        if root is None:
            return ''
        str = ''
        str += root.data
        str += self._preOrder(root.left)
        str += self._preOrder(root.right)
        return str
    
    def inOrder(self):
        print(self._inOrder(self.root))
    
    def _inOrder(self, root):
        if root.left is None and root.right is None:
            return root.data
        str = ''
        str += '('
        str += self._inOrder(root.left)
        str += root.data
        str += self._inOrder(root.right)
        str += ')'
        return str


tree = BinarySearchTree(input('Enter Postfix : '))
print('Tree :')
tree.printTree()
print('--------------------------------------------------')
print('Infix : ', end='')
tree.inOrder()
print('Prefix : ', end='')
tree.preOrder()
