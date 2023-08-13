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
        if self.search(data.data) is not None:
            return

        if self.head is None:
            self.head = data
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = data

    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return cur
            cur = cur.next

    def next_secondary_node(self,n,data):
        cur = self.search(n)
        if cur.snext is None:
            cur.snext = data
        else:
            scur = cur.snext
            while scur.next is not None:
                scur = scur.next
            scur.next = data

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
        l.next_node(Node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0], Snode(h[1]))
l.show_all()
