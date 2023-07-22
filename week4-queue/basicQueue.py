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
    
def separate(inputs):
    q = Queue()
    for input in inputs:
        str = input.split()
        action = str[0]
        if action == 'E':
            q.enqueue(str[1])
            print(f'Add {str[1]} index is {q.size() - 1 }')
        elif action == 'D':
            if not q.is_empty():
                val = q.dequeue()
                print(f'Pop {val} size in queue is {q.size()}')
            else:
                print('-1')

    if not q.is_empty():
        print(f"Number in Queue is :  {q.queue}")
    else:
        print("Empty")

inputs = input("Enter Input : ").split(',')
separate(inputs)