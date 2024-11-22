from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from CircularQueue import CircularQueue as CircularQueue
from LinkedDeque import LinkedDeque as Deque
from PositionalList import PositionalList as PositionalList
Q = Queue()
S = Stack()
CircQ = CircularQueue()
D = Deque()
P = PositionalList()
def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token not in operators:
            # If the token is a number, push it onto the stack
            stack.append(float(token))
        else:
            # Pop the top two elements from the stack
            b = stack.pop()
            a = stack.pop()

            # Perform the operation and push the result back onto the stack
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    # The final result will be the only element left in the stack
    return stack.pop()

# Example usage
postfix_expression = "5 2 + 8 3 - * 4 /"
result = evaluate_postfix(postfix_expression)
print(f"The result of the postfix expression '{postfix_expression}' is: {result}")


#adding elements to the PositionalList
P.add_first(1)
P.add_first(72)
P.add_first(81)
P.add_first(25)
P.add_first(65)
P.add_first(91)
P.add_last(11)
#Print the elements from the PositionalList
for x in P:
    print(x)

# Define the bubble sort function
def bubble_sort(L):
    n = len(L)
    for i in range(n):
        swapped = False
        current = L.first()
        for j in range(n - i - 1):
            next = L.after(current)
            if current.element() > next.element():
                a = next.element()
                b = current.element()
                L.replace(current, a)
                L.replace(next, b)
                swapped = True
            current = next
        if not swapped:
            break

# Sort the PositionalList
#bubble_sort(P)
#print("The sorted list of elements are: ")
# Print the sorted elements
#for x in P:
#    print(x)

def insertion_sort(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value > marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
insertion_sort(P)
print("The sorted list of elements are: ")
# Print the sorted elements
for x in P:
    print(x)
#change the insertion sort to descending order
def insertion_sort_descending(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value < marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
insertion_sort_descending(P)
print("The sorted list of elements are: ")
# Print the sorted elements
for x in P:
    print(x)