'''for i in range(1,5):
    for j in range(1,5):
        print("*",end="")
    print()'''

'''for j in range(5):
    for i in range(6):
        if  j==0 or j==4 or i==0 or i==5 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )'''

'''rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))

print("Hollow Rectangle Star Pattern") 
for i in range(rows):
    for j in range(columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()    ''' 

'''rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))

print("Hollow Rectangle Star Pattern") 
for i in range(rows):
    for j in range(columns):
        if(i == j):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()'''

'''rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))
for i in range(rows):
    for j in range(columns):
        if(  i==j or  j<=11 or i=<11):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )'''

'''f=open("myfile.txt","w")
print("name of the file",f.name)
print("filemode",f.mode)
print("readeable",f.readable)
f.close

f=open("covid.txt","w")
f.write("Garima is the university topper")
print("written work has done successfully")
f.close'''

'''f=open("covid.txt","w")
mylist=["garima","gattani","pythonclass"]
f.writelines(mylist)
f.close'''

'''f=open("covid.txt","r")
print(f.read())
print(f.read(5))
print(f.readline())
print(f.readlines())'''

'''with open("myfile.txt","w") as f:
    f.write("amit\n")
    f.write("garima\n")
    print("file closed:",f.closed)
print("file closed:",f.closed)

n=int(input("Enter the number of rows: "))
for i in range(1,n+1): 
    print("* "*n) 

n=int(input("Enter the number of rows: ")) #n=5
for i in range(1,n+1): #i=1  , n=6
    for j in range(1,n+1): # j=1
        print(i,end=" ")
    print()

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+j),end=" ")
    print()'''

'''f=open("myfile.txt","r")
print(f.tell())

print("total data",f.read())
print(f.tell())
f.seek(5)'''

f1=open("flowers.jpg","rb")
f2=open("flowers2.jpg","wb")
data=f1.read()
f2.write(data)

'''import csv
f=open("student.csv","w",newline="")
a=csv.writer(f)
a.writerow(["rollno","name","mobileno"])
rollno=101
name="garima"
mobileno=123456789
a.writerow([rollno,name,mobileno])
print("student record has save")'''

'''import csv
f=open("student.csv","w",newline="")
a=csv.writer(f)
b=int(input("enter the no of student"))
for i in range(1,b+1):
    a.writerow(["rollno","name","mobileno"])
    rollno=int(input("enter the roll no"))
    name=input("enter the name")
    mobileno=int(input("enter the mobileno"))
    a.writerow([rollno,name,mobileno])
print("student record has save")'''

import csv
f=open("student.csv","w",newline="")
a=csv.writer(f)
b=int(input("enter the no of student"))
a.writerow(["rollno","name","mobileno","email","address","paper1","paper2","paper3","paper4","paper5","total","percentage","result","grade"])
for i in range(1,b+1):
    rollno=int(input("enter the roll no"))
    name=input("enter the name")
    mobileno=int(input("enter the mobileno"))
    email=input("enter the email")
    address=input("enter the address")
    paper1=int(input("enter the marks"))
    paper2=int(input("enter the marks"))
    paper3=int(input("enter the marks"))
    paper4=int(input("enter the marks"))
    paper5=int(input("enter the marks"))
    total=paper1+paper2+paper3+paper4+paper5
    percentage=(total/500)*100
   
    a.writerow([rollno,name,mobileno,email,address,paper1,paper2,paper3,paper4,paper5,total,percentage])
print("student record has save")



