# class TreeNode(object): 
#     def __init__(self, data): 
#         self.data = data 
#         self.left = None
#         self.right = None
#         self.height = 1

#     def __str__(self):
#         return str(self.data)
  
# class AVL_Tree(object): 
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         self.root = self._insert(self.root, data)

#     def _insert(self, root, data):
#         if not root:
#             return TreeNode(data)
#         elif data < root.data:
#             root.left = self._insert(root.left, data)
#         else:
#             root.right = self._insert(root.right, data)
 

#         root.height = 1 + max(self.getHeight(root.left),
#                            self.getHeight(root.right))
 
#         balance = self.getBalance(root)

#         # Case 1 - Left Left
#         if balance > 1 and data < root.left.data:
#             return self.rightRotate(root)
 
#         # Case 2 - Right Right
#         if balance < -1 and data > root.right.data:
#             return self.leftRotate(root)
 
#         # Case 3 - Left Right
#         if balance > 1 and data > root.left.data:
#             root.left = self.leftRotate(root.left)
#             return self.rightRotate(root)
 
#         # Case 4 - Right Left
#         if balance < -1 and data < root.right.data:
#             root.right = self.rightRotate(root.right)
#             return self.leftRotate(root)
 
#         return root
 
#     def leftRotate(self, z):
 
#         y = z.right
#         T2 = y.left
 
#         # Perform rotation
#         y.left = z
#         z.right = T2
 
#         # Update heights
#         z.height = 1 + max(self.getHeight(z.left),
#                          self.getHeight(z.right))
#         y.height = 1 + max(self.getHeight(y.left),
#                          self.getHeight(y.right))
 
#         # Return the new root
#         return y
 
#     def rightRotate(self, z):
 
#         y = z.left
#         T3 = y.right
 
#         # Perform rotation
#         y.right = z
#         z.left = T3
 
#         # Update heights
#         z.height = 1 + max(self.getHeight(z.left),
#                         self.getHeight(z.right))
#         y.height = 1 + max(self.getHeight(y.left),
#                         self.getHeight(y.right))
 
#         # Return the new root
#         return y
 
#     def getHeight(self, root):
#         if not root:
#             return 0
 
#         return root.height
 
#     def getBalance(self, root):
#         if not root:
#             return 0
#         return self.getHeight(root.left) - self.getHeight(root.right)
    
#     def delete(self, data) :
#         self.root = self._delete(self.root, data)
  
#     def _delete(self, root, key) :
#         if root is None : return root
#         if int(key) < int(root.data) :
#             root.left = self._delete(root.left, key)
#         elif int(key) > int(root.data) :
#             root.right = self._delete(root.right, key)
#         else :
#             if root.left is None or root.right is None :
#                 root = root.left if root.right is None else root.right
#             else :
#                 temp = root.left
#                 while temp.right is not None :
#                     temp = temp.right
#                 root.data = temp.data
#                 root.left = self._delete(root.left, temp.data)
#             root = self.re(root)         
#         return root

#     def minInOrder(self):
#         return self._minInOrder(self.root)

#     def _minInOrder(self, root):
#         if root is None:
#             return []

#         left_result = self._minInOrder(root.left)
#         current_result = [root.data]
#         right_result = self._minInOrder(root.right)

#         return left_result + current_result + right_result
    
#     def maxInOrder(self):
#         return self._maxInOrder(self.root)

#     def _maxInOrder(self, root):
#         if root is None:
#             return []

#         left_result = self._maxInOrder(root.left)
#         current_result = [root.data]
#         right_result = self._maxInOrder(root.right)

#         return right_result + current_result + left_result
    
# def findResult(result):
#     lst = []
#     if len(result) >= 2:
#         while len(result) >= 2:
#             new_val = result.pop(0) + result.pop(0)
#             lst.append(new_val)
#             result.insert(0, new_val)
#     return sum(lst)

# t = AVL_Tree()
# inp = input("Enter Input: ").split()
# for val in inp:
#     t.insert(int(val))
# min = t.minInOrder()
# max = t.maxInOrder()
# print(f'Min cost: {findResult(min)}')
# print(f'Max cost: {findResult(max)}')
def min_cost(lst, result):
    if len(lst) >= 2:
        lst.sort()
        new_val = lst.pop(0) + lst.pop(0)
        lst.append(new_val)
        result.append(new_val)
        min_cost(lst, result)
    return sum(result)

def max_cost(lst, result):
    if len(lst) >= 2:
        lst.sort()
        new_val = lst.pop() + lst.pop()
        lst.append(new_val)
        result.append(new_val)
        max_cost(lst, result)
    return sum(result)

inp = input("Enter Input: ").split()
lst = []
lst1 = []
for val in inp:
    lst.append(int(val))
    lst1.append(int(val))

print(f'Min cost: {min_cost(lst, [])}')
print(f'Max cost: {max_cost(lst1, [])}')