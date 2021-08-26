'''try:
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a/b)
except:
    print("enter only integer value ")'''

'''try:
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a/b)

except ZeroDivisionError as message: #division by zero
    print("the description of exception:",message)'''

'''try:
        ch = input("Enter a character: ")
        if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
            print(ch, "is a Vowel")
        elif ord(ch)<32 and ord(ch)>47 and ord(ch)<54 and ord(ch)>64 and ord(ch)<91 and ord(ch)>96 and ord(ch)<123 and ord(ch)>126:
            print(ch, "is a special charactar")
        else:
            print("It is consonant")
        
except:
    print("enter only charactar value ")'''

'''a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if a<c and a<b:
    print("A is smaller")
if b<a and b<c:
    print("B is smaller")
if c<a and c<b:
    print("c is smaller")
else:
    print("all are same")'''

'''a=12
b=10
print(a//b)'''

num=int(input("enter the number"))
a=num%10
num=num//10
print(a)
b=num%10
num=num//10
print(num)
print(b)
c=num%10
num=num//10
print(c)
d=num%10
num=num//10
print(d)
e=num%10
num=num//10
print(e)
f=num%10
num=num//10
print(f)
g=num%10
num=num//10
print(g)
rev=a*1000000+b*100000+c*10000+d*1000+e*100+f*10+g
print("reverse number",rev)

num2=int(input("enter the number"))
a=num2%10
num2=num2//10
v=print(a*a*a)
b=num2%10
num2=num2//10
z=print(b*b*b)
c=num2%10
u=print(c*c*c)
arm=(a*a*a)+(b*b*b)+(c*c*c)
if arm==num2:
    print("armstrom number",arm)
else:
    print("enter number is not a armstrom number")

'''temp=int(input("enter the number"))
sum=0
while(temp!=0):
    rm=temp%10
    sum=sum+(rm*rm*rm)
    temp=temp//10
a=print(sum)
if a==temp:
    print("enter number is armstrom number")
else:
    print("enter the number is not armstrom number")'''





 