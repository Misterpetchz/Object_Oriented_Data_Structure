class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.snext = None

class Snode:
    def __init__(self, data):
        self.data = data
        self.next = None

class link:
    def __init__(self):
        self.head = None

    def next_node(self, data):
        if self.search(data) is not None:
            return

        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return cur
            cur = cur.next

    def next_secondary_node(self,n,data):
        snode = Snode(data)
        cur = self.head
        while cur is not None:
            if cur.data == n:
                if cur.snext is None:
                    cur.snext = snode
                else:
                    scur = cur.snext
                    while scur.next is not None:
                        scur = scur.next
                    scur.next = snode
                break
            cur = cur.next

    def show_all(self):
        cur = self.head
        while cur is not None:
            print(f'{cur.data} : ', end='')
            scur = cur.snext
            while scur is not None:
                print(scur.data, end=',')
                scur = scur.next
            print()
            cur = cur.next

inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(u[1])
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0], h[1])
l.show_all()
