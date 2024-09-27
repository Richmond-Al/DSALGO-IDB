class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"
    def top(self):
        if not self.is_empty():
            return  self.items[-1]
        else:
            return "Stack is empty"
    def size(self):
        return len(self.items)

S = Stack()
S.push(5)
print("Pushed: 5" )
S.push(3)
print("Pushed: 3" )
print("Length:",len(S.items))
print("Popped Element:",S.pop())
print ("Stack empty?",S.is_empty())
print("Popped Element",S.pop())
print ("Stack empty?",S.is_empty())
print("Popped Element",S.pop())
S.push(7)
print("Pushed: 7" )
S.push(9)
print("Pushed: 9" )
print("Top Element:",S.top())
S.push(4)
print("Pushed: 4" )
print("Popped Element",S.pop())
print("Length: ",len(S.items))
S.push(6)
print("Pushed: 6" )
S.push(8)
print("Pushed: 8" )
print("Popped Element",S.pop())
print(S.items)



class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"
    def top(self):
        if not self.is_empty():
            return  self.items[-1]
        else:
            return "Stack is empty"
    def size(self):
        return len(self.items)
S=Stack()
print()
print()
S.push(5)
print("Pushed: 5" )
S.push(3)
print("Pushed: 3" )
S.push(2)
print("Pushed: 2" )
S.push(8)
print("Pushed: 8" )
print("Popped Element:",S.pop())
print("Popped Element:",S.pop())
S.push(9)
print("Pushed: 9" )
S.push(1)
print("Pushed: 1" )
print("Popped Element:",S.pop())
S.push(7)
print("Pushed: 7" )
S.push(6)
print("Pushed: 6" )
print("Popped Element:",S.pop())
print("Popped Element:",S.pop())
S.push(4)
print("Pushed: 4" )
print("Popped Element:",S.pop())
print("Popped Element:",S.pop())
print (S.items)