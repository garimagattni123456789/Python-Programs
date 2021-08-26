'''import time
def add():
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    print(a+b)
    time.sleep(1)
add()
print("first time call function")
add()
print("2nd time call function")
add()
print("3rd time call function")'''

'''def login():
    username=input("enter the username")
    password= input("enter the password")
    if (username==password):
        print("login succesfully")
     else:
            print("not successfull")

login()'''

'''num1=int(input("enter the number"))
num2=int(input("enter the number"))
def add(num1,num2):
    return num1+num2

result=add(num1,num2)
print(result)
print("addition result",add(num1,num2))'''

'''number=int(input("enter the number"))
def chk_even_odd(number):
    if number%2==0:
        print("enter number is even")
    else:
        print("enter number is odd")
chk_even_odd(number)'''

'''num=int(input("enter the number"))
def fac(num):
    fact=1
    for i in range (1,num+1):
        fact=fact*i
    return fact
print("factorial",fac(num))'''





'''num=int(input("enter the number"))
def fibo(num):
    p=0
    q=1
    for i in range (1,num+1):
            sum=p+q
            print(sum)
            p=q
            q=sum
    return sum
print(fibo(num))'''

    
'''num=int(input("enter the number"))
def addition(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum
print(addition(num))'''

'''name=input("enter the name")
def func(name):
    i=0
    for i in name:
        if name=='n':
            print("the charatar present at index no",i,"value is :",name)
            break
        i=i+1
           
print(func(name))'''

def func(name):
    for i in name:
        print(i)

name=["aaaa","bbbb","cccc"]
func(name)

def func(name):
    for i in name:
        print(i)

name="aaaa"
func(name)

    









    