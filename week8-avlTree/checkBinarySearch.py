class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class Tree:
    def __init__(self): 
        self.root = None
        self.num = 0

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.num += 1
        else:
            h = height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root
            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num+=1
            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num+=1
            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)
                else:
                    insert_subtree(current.right,self.num - pow(2,h),val)
                self.num+=1

def insert_subtree(r,num,val):
    if r != None:
        h = height(r)
        max_node = pow(2,h+1)-1
        current = r
        if num+1 > max_node:
            while(current.left != None):
                current = current.left
            current.left = Node(val)
            return
        elif num+1 == max_node:
            while(current.right != None):
                current = current.right
            current.right = Node(val)
            return
        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
            insert_subtree(current.left,num - round(pow(2,h)/2),val)
        else:
            insert_subtree(current.right,num - pow(2,h),val)
    else:
        return

def height(root):
    if root == None:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        if left>right:
            return left + 1
        else:
            return right + 1          

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

# def check_binary_search_tree_(root, min_value = 0, max_value = 100):
#     if root is None:
#         return True

#     if not (min_value < root.data < max_value):
#         return False

#     return (
#         check_binary_search_tree_(root.left, min_value, root.data) and
#         check_binary_search_tree_(root.right, root.data, max_value)
#     )

def inOrder(node, result):
    if node:
        inOrder(node.left, result)
        result.append(node.data)
        inOrder(node.right, result)

def check_range(lst):
    for i in lst:
        if i < 0 or i > 100:
            return True
    return False
            

def check_binary_search_tree_(root):
    result = []
    inOrder(root, result)
    for i in range(1, len(result)):
        if result[i] <= result[i - 1] or check_range(result):
            return False
    return True

tree = Tree()
data = input("Enter Input : ").split()

for e in data:
    tree.insert(int(e))

printTree90(tree.root)
print(check_binary_search_tree_(tree.root))