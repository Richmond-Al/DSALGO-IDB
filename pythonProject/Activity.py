'''
#insertion sort
arr1=[10,9,21,3,7,8]
print("arr1 before insertion sort")
print(arr1)
def InsertionSort(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
            arr1[j + 1] = key
print("arr1 after insertion sort")
InsertionSort(arr1)
print (arr1)
=
#selection sort
arr2=[10,9,21,3,7,8]
print("arr2 before selection sort")
print(arr2)
for i in range (len(arr2)):
    mid_indx=i
    for j in range ( i+1, len(arr2)):
        if arr2[mid_indx] > arr2[j]:
            mid_indx = j
    arr2[i],arr2[mid_indx] = arr2[mid_indx], arr2[i]
print("arr2 after selection sort")
print(arr2)

#bubble sort
arr3=[10,9,21,3,7,8]
print("arr3 before bubble sort")
print(arr3)
def Bubblesort(arr3):
    for i in range (len(arr3)):
        for j in range(0,len(arr3)-i-1):
            if arr3[j]>arr3[j+1]:
                arr3[j],arr3[j+1] = arr3[j+1],arr3[j]
print("arr3 after bubble sort")
print (arr3)
'''
#1
num1=[23,89,7,56,44]
print("Before bubble sort")
print(num1)
for i in range(len(num1)):
    for j in range(0,len(num1) -1 -i):
        if num1[j]>num1[j+1]:
            num1[j],num1[j+1] = num1[j+1],num1[j]
print("After bubble sort")
print(num1)

#2
num2=[12,78,91,34,62]
print ("Before insertion sort")
print(num2)
for i in range(1, len(num2)):
        key = num2[i]
        j = i - 1
        while j >= 0 and key > num2[j]:
            num2[j + 1] = num2[j]
            j -= 1
            num2[j + 1] = key
print("After insertion sort")
print(num2)

#3
num3=[5, 99, 48, 15, 67]
print("Before Selection sort")
print(num3)
for i in range (len(num3)):
    middle=i
    for j in range ( i+1, len(num3)):
        if num3[middle] < num3[j]:
            middle= j
    num3[i],num3[middle] = num3[middle], num3[i]
print("After selection sort")
print(num3)

#4
num4=[38, 82, 25, 74, 13]
print("Before Insertion sort")
print (num4)
for i in range(len(num4)):
    for j in range(0,len(num4) -1 -i):
        if num4[j]<num4[j+1]:
            num4[j],num4[j+1] = num4[j+1],num4[j]
print("After Insertion Sort")
print(num4)

#5
num5=[7,56,91,34,38,15,25,74]
print("Unsorted values")
print (num5)
def AscendingOrder(num5):
    for i in range(1, len(num5)):
        key = num5[i]
        j = i - 1
        while j >= 0 and key < num5[j]:
            num5[j + 1] = num5[j]
            j -= 1
            num5[j + 1] = key
def DescendingOrder(num5):
    for i in range(1, len(num5)):
        key = num5[i]
        j = i - 1
        while j >= 0 and key > num5[j]:
            num5[j + 1] = num5[j]
            j -= 1
            num5[j + 1] = key
print("Ascending Order ")
AscendingOrder(num5)
print(num5)
print("Descending Order")
DescendingOrder(num5)
print(num5)

#6
num6=[38, 82, 25, 74, 13,5, 99, 48, 15, 67,12,78,91,34,62,23,89,7,56,44]
print("Before Selection sort")
print(num6)
for i in range (len(num6)):
    mid2=i
    for j in range ( i+1, len(num6)):
        if num6[mid2] > num6[j]:
            mid2 = j
    num6[i],num6[mid2] = num6[mid2], num6[i]
print("After Selection Sort")
print(num6)

#7
num7=[38, 82, 25, 74, 13,5, 99, 48, 15, 67,12,78,91,34,62,23,89,7,56,44]
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


