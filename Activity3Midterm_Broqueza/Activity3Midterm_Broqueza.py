<<<<<<< HEAD
class ArrayStack:
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self)==0
    def push(self,val):
        self.data.append(val)
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data[-1]
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()
'''class Queue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self.data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._data[self.front]
        self._data[self._front]= None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return answer
    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail]= e
        self._size +=1
    def _resize(self,cap):
        old=self._data
        self._data=[None]  
        walk=self._front
        for k in range (self._size):
            self.data[k]=old[walk]
            walk = (1+walk)%len(old)
        self.front = 0
=======
class ArrayStack:
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self)==0
    def push(self,val):
        self.data.append(val)
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data[-1]
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()
'''class Queue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self.data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._data[self.front]
        self._data[self._front]= None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return answer
    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail]= e
        self._size +=1
    def _resize(self,cap):
        old=self._data
        self._data=[None]  
        walk=self._front
        for k in range (self._size):
            self.data[k]=old[walk]
            walk = (1+walk)%len(old)
        self.front = 0
>>>>>>> a2d55f29cf0e66aa86a2beeff1c98e015a9484f5
'''