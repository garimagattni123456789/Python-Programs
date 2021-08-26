p1=int(input("enter the marks of maths"))
p2=int(input("enter the marks of english"))
p3=int(input("enter the marks of science"))
p4=int(input("enter the marks of hindi "))
p5=int(input("enter the marks of chemistry"))
pratical1=int(input("enter the marks of physics pratical"))
pratical2=int(input("enter the marks of biology pratical"))
a=p1+p2+p3+p4+p5+pratical1+pratical2;
b=(a / 700.0) * 100;
#print(b)
#print(a)
print("total marks;",a)
print("total percetage1",b)
    
if p1>40 and p2>40 and p3>40 and p4>40 and p5>40 and pratical1>15 and pratical2>20:
             print("you are pass")
else:
             print("you are fail")

if p1>40 and p2>40 and p3>40 and p4>40 and p5>40 and pratical1>15 and pratical2>20 and b>10 and b<=20:
    print("student got D grade")
elif p1>40 and p2>40 and p3>40 and p4>40 and p5>40 and pratical1>15 and pratical2>20 and b>20 and b<=40:
    print("student got C grade")
elif p1>40 and p2>40 and p3>40 and p4>40 and p5>40 and pratical1>15 and pratical2>20 and  b>40 and b<=60:
    print("student got B grade")
elif p1>40 and p2>40 and p3>40 and p4>40 and p5>40 and pratical1>15 and pratical2>20 and b>60 and b<=80:
    print("student got A grade")
elif p1>40 and p2>40 and p3>40 and p4>40 and p5>40 and pratical1>15 and pratical2>20 and b>80:
    print("student got A+ grade")


