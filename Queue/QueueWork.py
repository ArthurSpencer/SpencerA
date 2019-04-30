class my_queue():
    def __init__(self, maxsize):
        
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxsize = maxsize
        self.items = []
        while len(self.items) < maxsize:
            self.items.append("")

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        pass
    def isFull(self):
        if self.size == self.maxsize:
            return True
        else:
            return False
        pass
    def enqueue(self, newitem):
        if self.isFull():
            print("Queue full")
        else:
            self.rear = (self.rear + 1) % self.maxsize
            self.items[self.rear] = newitem
            self.size = self.size + 1
    def dequeue(self):
        if self.isEmpty():
            print("Queue empty")
            item = None
        else:
            item = self.items[self.front]
            self.front = (self.front + 1) % self.maxsize
            self.size = self.size - 1
        #print(item)
        return item

hwqueue = my_queue(5)

hwqueue.enqueue("job1")
hwqueue.enqueue("job2")
hwqueue.enqueue("job3")
print(hwqueue.items)
hwqueue.enqueue("job4")
hwqueue.enqueue("job5")
print(hwqueue.items)
hwqueue.dequeue()
hwqueue.dequeue()
hwqueue.dequeue()
print(hwqueue.items)
hwqueue.enqueue("job6")
hwqueue.enqueue("job7")
print(hwqueue.items)
hwqueue.dequeue()
hwqueue.dequeue()
hwqueue.dequeue()
hwqueue.dequeue()
print(hwqueue.items)
hwqueue.dequeue()

