class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return f"{', '.join(str(x) for x in self.queue)}"
    
def wannabemybobo(days):

    activity = {'0': 'Eat', '1': 'Game', '2': 'Learn', '3': 'Movie'}
    location = {'0': 'Res.', '1': 'ClassR.', '2': 'SuperM.', '3': 'Home'}

    myQueue = Queue()
    yourQueue = Queue()
    myActLoc = Queue()
    yourActLoc = Queue()
    score = 0

    for day in days:
        day = day.split()
        myQueue.enqueue(day[0])
        yourQueue.enqueue(day[1])

    for queue in myQueue.queue:
        queue = queue.split(':')
        myActLoc.enqueue(activity[queue[0]] + ':' + location[queue[1]])
    
    for queue in yourQueue.queue:
        queue = queue.split(':')
        yourActLoc.enqueue(activity[queue[0]] + ':' + location[queue[1]])

    print(f'My   Queue = {myQueue}')
    print(f'Your Queue = {yourQueue}')
    print(f'My   Activity:Location = {myActLoc}')
    print(f'Your Activity:Location = {yourActLoc}')

    while not myQueue.isEmpty() and not yourQueue.isEmpty():
        
        mine = myQueue.dequeue().split(':')
        yours = yourQueue.dequeue().split(':')
        myAct = mine[0]
        myLoc = mine[1]
        yourAct = yours[0]
        yourLoc = yours[1]

        if activity[myAct] == activity[yourAct]:
            if location[myLoc] != location[yourLoc]:
                score += 1
            elif location[myLoc] == location[yourLoc]:
                score += 4
        elif activity[myAct] != activity[yourAct]:
            if location[myLoc] == location[yourLoc]:
                score += 2
            elif location[myLoc] != location[yourLoc]:
                score -= 5

    if score >= 7:
        print(f'Yes! You\'re my love! : Score is {score}.')
    elif 7 > score > 0:
        print(f'Umm.. It\'s complicated relationship! : Score is {score}.')
    else:
        print(f'No! We\'re just friends. : Score is {score}.')

input_str = input('Enter Input : ').split(',')
wannabemybobo(input_str)