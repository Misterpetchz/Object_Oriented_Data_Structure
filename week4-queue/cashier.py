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

def simulateMovement(people):
    main_queue = Queue()
    cashier1 = Queue()
    cashier2 = Queue()

    for person in people:
        main_queue.enqueue(person)
    
    minutes = 0
    minutes2 = 0
    status = False

    while not main_queue.is_empty():
        if cashier1.size() < 5:
            cashier1.enqueue(main_queue.dequeue())
        else:
            cashier2.enqueue(main_queue.dequeue())
            status = True

        minutes += 1
        print(f'{minutes} {main_queue.queue} {cashier1.queue} {cashier2.queue}')

        if cashier2.is_empty():
            status = False
            minutes2 = 0
        if status:
            minutes2 += 1
        if minutes % 3 == 0:
            cashier1.dequeue()
        if minutes2 % 2 == 0:
            cashier2.dequeue()

people = input("Enter people : ")
people_list = list(people)
simulateMovement(people_list)

