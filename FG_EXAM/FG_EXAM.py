x=[1,2,3,4,5]
y=[]
z=[]
print("Before")
print(x)
print(y)
print(z)
y.append(x.pop())
y.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.sort()
x.clear()
print("After")
print(x)
print(y)
print(z)

X=[1,2,21,33,45,65,12]
print("_____________")
print("Number 2")
print(X)
def Insertion():
    for i in range(1,len(X)):
        key=X[i]
        j=i-1
        while j>=0 and key>X[j]:
            X[j+1]=X[j]
            j-=1
        X[j+1]=key
    print("After Insertion Sort")
    print(X)

def Selection():
    for i in range(len(X)):
        middle=i
        for j in range( i +1, len(X)):
            if X[middle] > X[j]:
                middle=j
        X[i],X[middle]=X[middle],X[i]
    print("After Selection sort")
    print(X)
Insertion()
Selection()
print("_____________")