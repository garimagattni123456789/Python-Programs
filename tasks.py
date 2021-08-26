'''#task 1
print("task1")
a=input("enter the range")
x=range(a)
for i in x:
    print(i)

print("task2")
y=range(10,0,-1)
for i in y:
    print(i)


print("task3")
b=int(input("tables of"))
d=int(input("enter the range of table"))
c=range(0,d)
for i in c:
    print(b,'*',i,'=',b*i)


print("task4")
a=int(input("enter the range of the tables"))
b=int(input("enter the nos tables"))
print("\t\t\tMULTIPLICATION TABLES OF",a)

for i in range(1,a):
    for j in range(1,b):
        print(i,'*',j,'=',i*j)
    print("\n")


asc=str(input("enter any value from keyboard"))
ch = int(asc)
if(ch >= 65 and ch <= 90):
	print("Upper")
elif(ch >= 97 and ch <= 122):
	print("Lower")
elif(ch >= 48 and ch <= 57):
	print("Number")
else:
	print("Symbol")


print("task5")
year = int(input("Enter Year: "))
#Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

print("task6")
a=int(input("enter the number"))
for i in range(1,a):
    print(i*2, " " ,i*3, " " ,i*4, " " ,i*5," " ,i*6, " " ,i*7," " ,i*8," " ,i*9," " ,i*10)


print("task7")
for i in range(a):
    if i==12:
        print("this is right time to take the the break")
        continue
    print(i)

print("task8")
mycart=[10,20,50,50,45,48,85,600000]
for i in mycart:
    if i>50:
        continue
    print(i)

print("task9")
count=0
for i in range(a):
    if i%2==0:
        continue
    else:
        print(i)
        count+=1
print("count",count)

print("task10")
for i in range(a):
    if i==5:
        break
    else:
        print(i)

name=input("enter the name")
i=0
for i in name:
        if x=='n':
            print("the charatar present at index no",i,"value is :",x)
            break
        i=i+1

list=[1,2,3,4,5,6,7,8,9,10]
sum=0
for x in list:
    sum=sum+x
print("the sum of list:",sum)


print("task11")
a=int(input("enter the number"))
sum=0
for i in range(1,a+1):
    sum=sum+i
print("sum:-",sum)


print("task12")
a=int(input("enter the number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print("factorial of number is:",fact)


print("task13")
p=0
q=1
sum=0
a=int(input("enter the range"))
if a>0:
    print(q)
    for i in range(2,a):
        sum=p+q
        print(sum)
        p=q
        q=sum
else:
    print("invalid range")
    

g=int(input("enter the number"))
for ch in range(1,g):
    print(ch)
    if ch==7 or ch==9:
        break
print("current number",ch)'''


#difference between for and while loop
#for loop is used if we need to print in sequence and range is given
#while is used when range is unknown
i=1
while i<6:
    print(i)
    i+=1

i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
    
print("while loop")
i=1
while i<11:
    print(i)
    i+=1
print("numbers in reverse order")
i=20
while i>0:
    print(i)
    i-=1

print("numbers in even order")
i=0
while i<20:
    print(i)
    i+=2
