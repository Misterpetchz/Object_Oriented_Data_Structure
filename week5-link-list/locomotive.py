class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:
                t = t.next
                self.size += 1
            self.tail = t

    def isEmpty(self):
        return self.size == 0
    
    def size(self):
        return self.size
    
    # add at end of list
    def append(self, data):
        p = Node(data)
        if self.head is None:
            self.head = self.tail = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.size += 1

    # add at first of list
    def addFirst(self, data):
        p = Node(data)
        p.next = self.head
        self.head = p
        self.size += 1

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            p = self.head
            while p.next is not None and p.next.data != data:
                p = p.next
        p.next = p.next.next
        self.size -= 1

    def removeHead(self):
        if self.head is None:
            return
        if self.head.next is None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def removeTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            p = self.head
            while p.next is not None:
                p = p.next
        p.next = p.next.next
        self.size -= 1
        return p.data

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p

    def search(self, data):
        p = self.head
        while p is not None:
            if p.data == data:
                return p
            p = p.next
        return None
    
    def insertAfter(self, data, i):
        p = Node(data)
        q = self.nodeAt(i)
        p.next = q.next
        q.next = p
        self.size += 1

    def deleteAfter(self, i):
        q = self.nodeAt(i)
        q.next = q.next.next
        self.size -= 1

    def isIn(self, data):
        p = self.head
        while p is not None:
            if p.data == data:
                return True
            p = p.next
        return False
    
    def findTail(self):
        p = self.head
        while p is not None:
            if p.next is None:
                return p
            p = p.next

def sort_train(train):

    locomotive = None
    current = train.head
    prev = None
    while current is not None:
        if current.data == 0:
            # new Head
            locomotive = current
            break
        prev = current
        current = current.next
    if not locomotive:
        return None
    if prev:
        train.findTail().next = train.head
        train.head = locomotive
        prev.next = None
    return train

print(' *** Locomotive ***')
input_str = input('Enter Input : ').split()
train_linked_list = LinkedList()

for train in input_str:
    train_linked_list.append(int(train))

current_train = train_linked_list.head
print('Before : ', end='')
while current_train is not None:
    print(current_train.data, end=' <- ' if current_train.next is not None else '\n')
    current_train = current_train.next

current_train = sort_train(train_linked_list)
current_train = current_train.head
print('After : ', end='')
while current_train is not None:
    print(current_train.data, end=' <- ' if current_train.next is not None else '\n')
    current_train = current_train.next