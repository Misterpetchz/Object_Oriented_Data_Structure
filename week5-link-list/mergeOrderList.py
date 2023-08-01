class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def createList(l = []):
    head = None
    for val in l:
        new_node = Node(val)
        if head is None:
            head = new_node
        else:
            cur = head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
    return head

def printList(cur):
    while cur is not None:
        print(cur.data, end=' ' if cur.next is not None else '\n')
        cur = cur.next

def mergeOrderList(l1, l2):
    dummy = cur = Node(None)
    while l1 and l2:
        if l1.data < l2.data:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    
    while l1:
        cur.next = l1
        l1 = l1.next
        cur = cur.next

    while l2:
        cur.next = l2
        l2 = l2.next
        cur = cur.next

    return dummy.next

inp1, inp2 = input('Enter 2 Lists : ').split()
L1 = [int(x) for x in inp1.split(',')]
L2 = [int(x) for x in inp2.split(',')]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)