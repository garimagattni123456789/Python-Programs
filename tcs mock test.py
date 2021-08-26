
def codedmessage():
    i=0
    a=input("enter the coded message") 
    while i!=len(a):
        b=a[i:i+1]
        c=ord(b)+5
        print(chr(c))
        i+=1
 
codedmessage()
    

    

