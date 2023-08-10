class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __str__(self):
        if self.isEmpty():
            return
        else:
            cur, s = self.head, ''
            while cur is not None:
                s += str(cur.value) + ' '
                cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        if self.isEmpty():
            return 0
        cur = self.head
        i = 1
        while cur.next is not None:
            cur = cur.next
            i += 1
        return i

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addHead(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self, pos):
        i = 0
        if pos < 0:
            pos = self.size() + pos
        if pos >= self.size() or pos < 0:
            return 
        elif pos == 0:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None and i < pos - 1:
                cur = cur.next
                i += 1
            if pos == self.size() - 1:
                self.tail = cur
                self.tail.next = None
            else:
                cur.next = cur.next.next

    def index(self, pos):
        cur = self.head
        i = 0
        while i < pos:
            cur = cur.next
            i += 1
        return cur.value
    
    def insert(self, data, pos):
        new_node = Node(data)
        i = 1
        if pos < 0:
            pos = self.size() + pos
        if self.isEmpty():
            self.head = self.tail = new_node
        elif pos <= 0:
            self.addHead(new_node)
        elif pos >= self.size():
            self.append(new_node)
        else:
            cur = self.head
            while cur.next is not None and i < pos:
                cur = cur.next
                i += 1
            new_node.next = cur.next
            cur.next = new_node

def createLL(ll):
    link = LinkedList()
    for val in ll:
        link.append(val)
    return link

def printLL(head):
    return str(head)

def SIZE(head):
    return head.size()

def bottomUp(head, b):
    for _ in range(b):
        data = head.head.value
        head.pop(0)
        head.append(data)

def deBottomUp(head, b):
    for _ in range(b):
        data = head.tail.value
        head.pop(-1)
        head.addHead(data)

def riffleShuffle(head, r):
    linkedList = LinkedList()
    for i in range(head.size() - r):
        linkedList.addHead(head.tail.value)
        head.pop(-1)
    for i in range(linkedList.size()):
        head.insert(linkedList.head.value, 2 * i + 1)
        linkedList.pop(0)

def deRiffleShuffle(head, r):
    linkedList = LinkedList()
    if r <= head.size() - r:
        for i in range(r):
            linkedList.append(head.index(i))
            head.pop(i)
        for i in range(linkedList.size()):
            head.addHead(linkedList.tail.value)
            linkedList.pop(-1)
    else:
        for i in range(head.size() - r):
            linkedList.append(head.index(i + 1))
            head.pop(i + 1)
        for i in range(linkedList.size()):
            head.append(linkedList.head.value)
            linkedList.pop(0)

def scramble(head, b, r, size):
    bot = int((b / 100) * size)
    riff = int((r / 100) * size)
    bottomUp(head, bot)
    print(f'BottomUp {b:.3f} % :', head)
    riffleShuffle(head, riff)
    print(f'Riffle {r:.3f} % :', head)
    deRiffleShuffle(head, riff)
    print(f'Deriffle {r:.3f} % :', head)
    deBottomUp(head, bot)
    print(f'Debottomup {b:.3f} % :', head)

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scramble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scramble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)

'''
Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 62,B 23
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 23.000 % : 3 4 5 6 7 8 9 10 1 2
Riffle 62.000 % : 3 9 4 10 5 1 6 2 7 8
Deriffle 62.000 % : 3 4 5 6 7 8 9 10 1 2
Debottomup 23.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------



Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 16.98,B 68.42|R 26.9257,B 57
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 68.420 % : 7 8 9 10 1 2 3 4 5 6
Riffle 16.980 % : 7 8 9 10 1 2 3 4 5 6
Deriffle 16.980 % : 7 8 9 10 1 2 3 4 5 6
Debottomup 68.420 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 57.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 26.926 % : 6 8 7 9 10 1 2 3 4 5
Deriffle 26.926 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 57.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------


Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20/B 32.4367,R 49.5484863|B 89.4642,R 12.8962|R 11.546678,B 20.77867|R 40.56,B 93.7567
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 32.437 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6
Riffle 49.548 % : 7 16 8 17 9 18 10 19 11 20 12 1 13 2 14 3 15 4 5 6
Deriffle 49.548 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6
Debottomup 32.437 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 89.464 % : 18 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Riffle 12.896 % : 18 20 19 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Deriffle 12.896 % : 18 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Debottomup 89.464 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 20.779 % : 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
Riffle 11.547 % : 5 7 6 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
Deriffle 11.547 % : 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
Debottomup 20.779 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 93.757 % : 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Riffle 40.560 % : 19 7 20 8 1 9 2 10 3 11 4 12 5 13 6 14 15 16 17 18
Deriffle 40.560 % : 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Debottomup 93.757 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------


Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 10,B 20|B 27,R 73
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 
BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3 
Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10 
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 
BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 20.000 % : 3 4 5 6 7 8 9 10 1 2
Riffle 10.000 % : 3 4 5 6 7 8 9 10 1 2
Deriffle 10.000 % : 3 4 5 6 7 8 9 10 1 2
Debottomup 20.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
Riffle 73.000 % : 1 8 2 9 3 10 4 5 6 7
BottomUp 27.000 % : 2 9 3 10 4 5 6 7 1 8
Debottomup 27.000 % : 1 8 2 9 3 10 4 5 6 7
Deriffle 73.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
'''