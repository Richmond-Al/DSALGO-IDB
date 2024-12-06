Exam = [1,2,3,4,5]
z=[]
y=[]
z.append(Exam.pop())
z.append(Exam.pop())
Exam.reverse()
y.append(Exam.pop())
y.append(Exam.pop())
y.append(Exam.pop())
Exam.clear()

print(z)
print(y)
print(Exam)