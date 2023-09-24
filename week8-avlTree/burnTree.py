class TreeNode(object): 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)
  
class AVL_Tree(object): 
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
 

        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
 
        balance = self.getBalance(root)

        # Case 1 - Left Left
        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and data > root.right.data:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getNode(self, data):
        q = [self.root]
        while q:
            cur = q.pop(0)
            if cur.data == data:
                return cur
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
  
    def burn(self, data): 
        target = self.getNode(data)
        if not target:
            print(f"There is no {data} in the tree.")
            return 
        will_burn = [target]
        burned = [target]
        while will_burn:
            for node in will_burn:
                burned.append(node)
                print(node.data, end=" ")
            will_burn = self.bfs(will_burn, burned)
            print()

    def bfs(self, burning, burned):
        res = []
        for node in burning: 
            if node.left and node.left not in burned:
                res.append(node.left)
            if node.right and node.right not in burned:
                res.append(node.right)
        q = [self.root]
        while q: 
            cur = q.pop(0)
            if (cur.left in burning or cur.right in burning) and cur not in burned:
                res.append(cur)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res
    
myTree = AVL_Tree() 

inp, delete= input("Enter node and burn node : ").split('/')
data = inp.split()
for e in data:
    root = myTree.insert(int(e))
target = int(delete)
myTree.burn(target)