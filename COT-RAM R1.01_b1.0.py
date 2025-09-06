#this is a system written in python
#this is a system of memory
i=1
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
print("COT-RAM r1.01_b01   have all")
print("please enter 'help' for the first time please enter")
while i==1:
    ch=input(">>>")
    if ch=="help":
        print("1--help   2--about   3--write   4--dir   5--clean")
    elif ch=="about":
        print("COT-RAM r1.01_b01   have all")
    elif ch=="wr":
        print("please be in the range of 1-8 name")
        n=int(input("name:"))
        m=input("content:")
        if n==1:
            a=m
        elif n==2:
            b=m
        elif n==3:
            c=m
        elif n==4:
            d=m
        elif n==5:
            e=m
        elif n==6:
            f=m
        elif n==7:
            g=m
        elif n==8:
            h=m
        else:
            print("command not find!")
    elif ch=="dir":
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        print(h)
    elif ch=="clean":
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        g=0
        h=0 
    else:
        print("command not find!")
i=i+0
#build 250517           2519a