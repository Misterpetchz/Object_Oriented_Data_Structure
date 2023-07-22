class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
def findSecretCode(string, hint):
    queue = Queue()
    diff = ord(hint) - ord(string[0])

    for char in string:
        queue.enqueue(chr(ord(char) + diff))
        print(queue.queue)

str, hint = input("Enter code,hint : ").split(',')
findSecretCode(str, hint)