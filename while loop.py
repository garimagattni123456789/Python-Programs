
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

a=int(input("enter the range"))
print("numbers in reverse order")
i=a+1
while i>0:
    print(i)
    i-=1

print("numbers in even order")
i=0
while i<20:
    print(i)
    i+=2

    


a=int(input("enter the range"))
print("sum of natural numbers")
i=1
sum=0
while i<a+1:
    sum=sum+i
    i+=1
print(sum)


a=int(input("enter the range"))
print("finonacci series")
i=1
p=0
q=1
sum=0
print(q)
while i<a+1:
    sum=p+q
    print(sum)
    p=q
    q=sum
    i+=1
    

list=[1,2,3,4,5,6,7,8,9,10,55,66]
sum=0
for x in list:
    sum=sum+x
print("the sum of list:",sum)


list=[1,2,3,4,5,6,7,8,9,10,55,66]
i=0
sum=0
lenght=len(list)
while i < lenght:
    sum=sum+list[i]
    print(sum)
    i+=1
print("sum of list",sum)

list = [1, 2,3,4,5,6,7,8,9,10,55,66]
length = len(list)
i = 0
sum=0  
while i < length:
    sum=sum+list[i]
    i += 1
print("sum of list",sum)
    
