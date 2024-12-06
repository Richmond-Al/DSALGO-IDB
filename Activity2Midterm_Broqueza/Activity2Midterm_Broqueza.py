<<<<<<< HEAD
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def first(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)

Q = Queue()
Q.enqueue(5)
Q.enqueue(3)
print("Length: ",len(Q.queue))
print("Dequeued number: ",Q.dequeue())
print("Is it empty: ",Q.is_empty())
print("Dequeued number: ",Q.dequeue())
print("Is it empty: ",Q.is_empty())
print("Dequeued number: ",Q.dequeue())
Q.enqueue(7)
Q.enqueue(9)
print("First",Q.first())
Q.enqueue(4)
print("Length: ",len(Q.queue))
print("Dequeued number: ",Q.dequeue())
print(Q.queue)


print()
print("Answers: ")
Q=Queue()
Q.enqueue(5)
Q.enqueue(3)
print("Dequeued number: ",Q.dequeue())
Q.enqueue(2)
Q.enqueue(8)
print("Dequeued number: ",Q.dequeue())
print("Dequeued number: ",Q.dequeue())
Q.enqueue(9)
Q.enqueue(1)
print("Dequeued number: ",Q.dequeue())
Q.enqueue(7)
Q.enqueue(6)
print("Dequeued number: ",Q.dequeue())
print("Dequeued number: ",Q.dequeue())
Q.enqueue(4)
print("Dequeued number: ",Q.dequeue())
print("Dequeued number: ",Q.dequeue())
=======
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def first(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)

Q = Queue()
Q.enqueue(5)
Q.enqueue(3)
print("Length: ",len(Q.queue))
print("Dequeued number: ",Q.dequeue())
print("Is it empty: ",Q.is_empty())
print("Dequeued number: ",Q.dequeue())
print("Is it empty: ",Q.is_empty())
print("Dequeued number: ",Q.dequeue())
Q.enqueue(7)
Q.enqueue(9)
print("First",Q.first())
Q.enqueue(4)
print("Length: ",len(Q.queue))
print("Dequeued number: ",Q.dequeue())
print(Q.queue)


print()
print("Answers: ")
Q=Queue()
Q.enqueue(5)
Q.enqueue(3)
print("Dequeued number: ",Q.dequeue())
Q.enqueue(2)
Q.enqueue(8)
print("Dequeued number: ",Q.dequeue())
print("Dequeued number: ",Q.dequeue())
Q.enqueue(9)
Q.enqueue(1)
print("Dequeued number: ",Q.dequeue())
Q.enqueue(7)
Q.enqueue(6)
print("Dequeued number: ",Q.dequeue())
print("Dequeued number: ",Q.dequeue())
Q.enqueue(4)
print("Dequeued number: ",Q.dequeue())
print("Dequeued number: ",Q.dequeue())
>>>>>>> a2d55f29cf0e66aa86a2beeff1c98e015a9484f5
print(Q.queue)