from array import *
marks=array('i',[])
n=int(input("how many students marks u want to store"))
print("no of students=",n)
for i in range(n):
    x=int(input("enter the marks of students"))
    marks.append(x)
print(marks)



