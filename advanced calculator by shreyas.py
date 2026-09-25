from math import sqrt
def dose():
    print(" 16.giving dose")
    print("  Enter the name")
    n=input("  ")
    print("  Enter the age")
    a=int(input("  "))
    print("  Enter the gender,M for male/F for femal")
    g=input("  ").upper()
    if g=='M':
        G='Mr'
    elif g=='F':
        G='Ms'
    else:
        print("  this is not valid gender")
    if a<=5 and a>0:
     d="  you can be dosed 2ml"
    elif a<=10:
     d="  you can be dosed 5ml"
    elif a<=18:
     d="  you can be dosed 10ml"
    elif a<=35:
     d="  you can be dosed 20ml"
    elif a<45:
     d="  you can be dosed 30ml"
    elif a>45 and a==0:
     print("  you cannot be dosed")    
    return d,G,n
def addition():
    p=0
    print(" 1.addition")
    print("  enter the inputs")
    h=int(input("  "))
    for i in range(0,h):
        print("  enter the num")
        n=float(input("  "))
        p+=n
    return p 
def multipl():
    print(" 3.multiplication")
    p=1
    print("  number of digits")
    n=int(input("  "))
    for i in range(0,n):
        print("  enter the num")
        s=int(input("  "))
        p*=s
    return p
def division():
    print(" 4.division")
    print("  Enter the first number")
    a=int(input("  "))
    print("  Enter the second number")
    b=int(input("  "))
    p=a/b
    return p   
def substract():
    print(" 2.substraction")
    print("  Enter the first number")
    a=int(input("  "))
    print("  Enter the second number")
    b=int(input("  "))
    p=a-b
    return p
def Average():
    def average():
        sum,l1=0,[]
        for i in range(0,n):
            print("  Enter the num")
            s=int(input("  "))
            l1.append(s)
            sum=sum+l1[i]
            au=sum/n            
        return au
    print(" 5.Average")
    print("  Enter the number of digits")
    n=int(input("  "))
    A=average()
    return A 
def palindrom():
    print(" 6.palindrom")
    print("  Enter the digit")
    j=int(input("  "))
    n=j
    rnum=0
    while(j>0):
        digit=j%10
        rnum=rnum*10+digit
        j=j//10
    if(n==rnum):
        t='this is a palindrom'
    else:
        t='this is not a palindrom'
    return t  
def sum():
    print(" 7.sum of the digits")
    print("  Enter the digit")
    s=int(input("  "))
    sum=0
    while(s>0):
            r=s%10
            sum=sum+r
            s=s//10
    return sum   
def table():
    print(" 8.tables")
    print("  Enter the num")
    n=float(input("  "))
    i=1
    while i<=10:
        print(" ",n,"x",i,"=",n*i)
        i=i+1     
def lessthan():    
    print(" 9.writing less than the given num")
    print("  Enter the num")
    n=int(input("  "))
    print("  less than",n)
    for i in range(n):
     print(" ",i,end=' ')     
def simple_interest():
    print(" 10.simple interest:")
    print("  Enter the time")
    t=float(input("  "))
    print("  Enter the principle amount")
    p=float(input("  "))
    print("  Enter the rate")
    r=float(input("  "))
    si=p*t*r/100
    return si 
def percantage():
    print(" 11.grade of marks")
    print("  Enter the marks out of 100")
    g=float(input("  "))
    if g>=90:
        j='grade A'
    elif g>=80:
        j='grade B'
    elif g>=70:
        j='grade C'
    elif g>=60:
        j='grade D'
    elif g>=35:
        j='grade E'
    else:
        j='Fail'
    return j
def mini_max():
    print(" 12,minimum max")
    print("  number of digits")
    n=int(input("  "))
    j=[]
    for i in range(0,n):
        print("  Enter the number")
        num=float(input("  "))
        j.append(num)
    M=max(j)
    m=min(j)
    return M,m
def license():
    print(" 13.driving license")
    print("  Enter your name")
    n=input("  ")
    print("  Enter your age")
    a=float(input("  "))
    print("  Enter your gender[M for male/F for female]")
    g=input("  ").upper()
    if(g=='M'):
        G='Mr'
    elif(g=='F'):
        G='Ms'
    else:
        print("  not valid input")
    if(a>=18):
        l='you are eligible for driving license'
    else:
        l='you are not eligible for driving license'
    return G,n,l
def odd_or_even():
    print(" 14.finding the number is odd or even")
    print("  Enter the num")
    n=int(input("  "))
    if n%2==0:
        d="even number"
    else:
        d="odd number"
    return d
def triangle():
    print(" 15.finding Area&perimeter of triangle")
    print("  Enter the lenght")
    l=float(input("  "))
    print("  Enter breath")
    b=float(input("  "))
    a=l*b
    p=2*(l+b)
    return a,p
def square():
    f=[]
    print(" 17.finding roots")
    print("  Enter the number of digits")
    n=int(input("  "))
    for i in range(0,n):
        print("  Enter the num",i+1)
        num=float(input("  "))
        f.append(sqrt(num))
    return f,n
f='yes'
z=(((((100*30000)/10)+200000)+6000)/100)
while(f=='yes'):
    print("  select operation")
    print("  1.addition")
    print("  2.substraction")
    print("  3.multiplication")
    print("  4.division")
    print("  5.finding average")
    print("  6.palindrom")
    print("  7.sum of the digits")
    print("  8.tables")
    print("  9.less than given number")
    print("  10.simple interest")
    print("  11.grade for marks")
    print("  12.minimum maximum")
    print("  13.driving license")
    print("  14.finding a num is odd ro even")
    print("  15.finding Area&perimeter of triangle")
    print("  16.dose giving according to the age")
    print("  17.finding roots")
    print("  18.all operators")
    print("  choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18)")
    n=int(input("  "))
    if n==1:
        p=addition()
        print("  sum of the enterd numbers=",p)
        print("  do you want to repeat[yes/no]")
        f=input("  ")
    elif n==2:
        p=substract()
        print("  difference=",p)
        print("  do you want to repeat[yes/no]")
        f=input("  ")
    elif n==3:
        p=multipl()
        print("  multiple of given number=",p)
        print("  do you want to repeat[yes/no]")
        f=input("  ")
    elif n==4:
        p=division()
        print("  reminder of the given numbers=",p)
        print("  do you want to repeat[yes/no]")
        f=input("  ")
    elif n==18:
        a=addition()
        b=substract()
        c=multipl()
        d=division()
        e=Average()
        g=palindrom()
        h=sum()
        table() 
        lessthan()
        print( ) 
        i=simple_interest()  
        P=percantage()
        M,m=mini_max()   
        G,z,q=license()
        D=odd_or_even()
        A,p=triangle()
        l,s,n=dose()
        Z,T=square()
        df='num'
        print("  1.sum of given num=",a)
        print("  2.difference of given num=",b)
        print("  3.multipl of given number=",c)
        print("  4.reminder of given number=",d)
        print("  5.Average of given digits=",e)
        print("  6.",g)
        print("  7.sum of the digits=",h)
        print("  10.simple interest=",i)
        print("  11.grade of the marks=",P)
        print("  12.minimum maximum")
        print("    minimum=",m)
        print("    maximum=",M)
        print("  13.driving license")
        print("      ",G,z,q)
        print("  14.finding a num is odd or even")
        print("  this is a",D)
        print("  15.area&perimeter of triangle")
        print("  Area of triangle=",A)
        print("  Perimeter of triangle=",p)
        print("  ",s,n,l)
        for B in range(0,T):
            s=B+1
            df+=str(s)
            print("  ",df,Z[B])
            df=df[0:3]
        print("  do you want  repeat  [yes/no]")
        f=input("  ")
    elif n==5:
        A=Average()
        print("  Average of given inputs=",A)
        print("  do you want to repeat[yes/no]")
        f=input("  ")
    elif n==6:
        p=palindrom()
        print(" ",p)
        print("  do you want to repeat[yes/no]")
        f=input("  ")
    elif n==7:
        x=sum()
        print("  sum of the digits=",x)
        
        print("  do you want to repeat [yes/no]")
        f=input("  ")
    elif n==8:
            print("  table")
            print("  enter the num")
            num=float(input("  "))
            i=1
            while i<=10:
                print(" ",num,"x",i,"=",num*i)
                i=i+1
            print("  do you want to repeat [yes/no]")
            f=input("  ")
    elif n==9:
            lessthan()
            print( )
            print("  do you want to repeat [yes/no]")
            f=input("  ")
    elif n==10:
            si=simple_interest()
            print("  simple interest=",si)
            print("  do you want to repeat [yes/no]")
            f=input("  ")   
    elif n==11:
        j=percantage()
        print("  grade of marks=",j)
        print("  do you want to repeat [yes/no]")
        f=input("  ") 
    elif n==12:
        M,m=mini_max()
        print("  minimum number=",m)
        print("  Maximum number=",M)
        print("  do you want to repeat [yes/no]")
        f=input("  ")  
    elif n==13:
        G,n,l=license()
        print(" ",G,n,l)
        print("  do you want to repeat [yes/no]")
        f=input("  ")   
    elif n==14:
        d=odd_or_even()
        print("  this is a",d)
        print("  do you want to repeat [yes/no]")
        f=input("  ")  
    elif n==15:
        print(" 15.finding area&perimeter of triangle")
        a,p=triangle()
        print("  area of the triangle=",a)
        print("  perimeter of triangle=",p)
        print("  do you want to repeat[yes/no]")
        f=input("  ") 
    elif n==16:
        d,g,n=dose()
        print("  ",g,n,d)
        print("  do you want to repeat[yes/no]")
        f=input("  ")
    elif n==17:
        n=0
        num='num'
        l,t=square()
        for i in range(0,len(l)):
            s=i+1
            num+=str(s)
            print("  ",num)
            print("  ",l[i])
            num=num[0:3]
        print("  do you want to repeat[yes/no]")    
        f=input("  ")         