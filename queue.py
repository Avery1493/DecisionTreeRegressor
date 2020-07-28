# python queue.py 

class Queue:
    def __init__(self):
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            dequeue = self.storage[0]
            self.storage.remove(self.storage[0])
            return dequeue



if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("hi")
    queue.enqueue([2,4,6])
    queue.enqueue(8)

    print(queue.storage)

    print(queue.dequeue())
