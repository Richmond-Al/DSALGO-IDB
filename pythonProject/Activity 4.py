#1
print("____________________________________")
num1=[23,89,7,56,44]
print("Before Bubble Sort")
print(num1)
for i in range(len(num1)):
    for j in range(0,len(num1) -1 -i):
        if num1[j]>num1[j+1]:
            num1[j],num1[j+1] = num1[j+1],num1[j]
print("After Bubble Sort")
print(num1)
print("____________________________________")
#2

num2=[12,78,91,34,62]
print ("Before Insertion Sort")
print(num2)
for i in range(1, len(num2)):
        key = num2[i]
        j = i - 1
        while j >= 0 and key < num2[j]:
            num2[j + 1] = num2[j]
            j -= 1
            num2[j + 1] = key
print("After Insertion Sort")
print(num2)
print("____________________________________")
#3
num3=[5, 99, 48, 15, 67]
print("Before Selection Sort")
print(num3)
for i in range (len(num3)):
    middle=i
    for j in range ( i+1, len(num3)):
        if num3[middle] < num3[j]:
            middle= j
    num3[i],num3[middle] = num3[middle], num3[i]
print("After Selection Sort")
print(num3)
print("____________________________________")
#4
num4=[38, 82, 25, 74, 13]
print("Before Insertion Sort")
print (num4)
for i in range(len(num4)):
    for j in range(0,len(num4) -1 -i):
        if num4[j]<num4[j+1]:
            num4[j],num4[j+1] = num4[j+1],num4[j]
print("After Insertion Sort")
print(num4)
print("____________________________________")
#5
num5=[7,56,91,34,38,15,25,74]
print("Unsorted Values")
print (num5)
num5ascending=[]
num5descending=[]
def AscendingOrder(num5):
    for i in range(1, len(num5)):
        key = num5[i]
        j = i - 1
        while j >= 0 and key < num5[j]:
            num5[j + 1] = num5[j]
            j -= 1
            num5[j + 1] = key
num5ascending=num5
def DescendingOrder(num5):
    for i in range(1, len(num5)):
        key = num5[i]
        j = i - 1
        while j >= 0 and key > num5[j]:
            num5[j + 1] = num5[j]
            j -= 1
            num5[j + 1] = key
num5descending=num5
print("Ascending Order ")
AscendingOrder(num5)
print(num5ascending)
print("Descending Order")
DescendingOrder(num5)
print(num5descending)
print("____________________________________")
#6
num6=[38, 82, 25, 74, 13,5, 99, 48, 15, 67,12,78,91,34,62,23,89,7,56,44]
print("Before Selection Sort")
print(num6)
for i in range (len(num6)):
    mid2=i
    for j in range ( i+1, len(num6)):
        if num6[mid2] > num6[j]:
            mid2 = j
    num6[i],num6[mid2] = num6[mid2], num6[i]
print("After Selection Sort")
print(num6)
print("____________________________________")
#7
num7=[38, 82, 25, 74, 13,5, 99, 48, 15, 67,12,78,91,34,62,23,89,7,56,44]
print("Unsorted Values")
print(num7)
even=[]
odd=[]
for x in range(0,len(num7)):
    if num7[x]%2 == 0:
        even.append(num7[x])
    else:
        odd.append(num7[x])
print("Even Numbers")
print(even)
print("Odd Numbers")
print (odd)
print("____________________________________")