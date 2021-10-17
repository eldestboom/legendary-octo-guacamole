import math as m
def add(x,y):
    x=int(input('enter the value'))
    y=int(input('enter the value'))
    z=x+y
    print(z)
def subtract(x,y):
    x=int(input('enter the value'))
    y=int(input('enter the value'))
    a=x-y
    print(a)
def product(x,y):
    x=int(input('enter the value'))
    y=int(input('enter the value'))
    c=x*y
    print(c)
def qoutient(x,y):
    x=int(input('enter the value'))
    y=int(input('enter the value'))
    q=x/y
    print(q)
def log(x,y):
    x=int(input('enter the value'))
    y=int(input('enter the value'))
    l=m.log(x,y)
    print(l)
def ceil(x,y):
    x=int(input('enter the value'))
    ceil1=m.ceil(x)
    print(ceil1)
def sqrt(x):
    x=int(input('enter the value'))
    sqt=m.sqrt(x)
    print(sqt)
def fabs(x):
    x=int(input('enter the value'))
    fabs=m.fabs(x)
def pow(x,y):
    x=int(input('enter the value'))
    y=int(input('enter the value'))
    pow=m.pow(x,y)
    print(pow)
def sin(x):
    x=int(input('enter the value'))
    sin=m.sin(x)
    print(x)
def cos(x):
    x=int(input('enter the value'))
    cos=m.cos(x)
    print(cos)
def tan(x):
    x=int(input('enter the value'))
    tan=m.tan(x)
    print(tan)
def factorial(x):
    x=int(input('enter the value'))
    fact=m.factorial(x)
    print(fact)
def gcd(x,y):
    x=int(input('enter the value'))
    y=int(input('enter the value'))
    gcd=m.gcd(x,y)
    print(gcd)
while True:
    print("1.sum","/n",'2.difference','/n','3.product','/n','4.qoutient','/n','5.log','/n'
            ,'6.ceil','/n','7.sqrt','/n','8.fabs','/n','9.pow','/n','10.sin','/n','11.cos','/n','12.tan','/n',
            '13.factorial','/n','14.gcd')
    i=int(input('choose the option :'))
    if i==1:
        add()
    elif i==2:
        subtract()
    elif i==3:
        product()
    elif i==4:
        qoutient()
    elif i==5:
        log()
    elif i==6:
        ceil()
    elif i==7:
        sqrt()
    elif i==8:
        fabs()
    elif i==9:
        pow()
    elif i==10:
        sin()
    elif i==11:
        cos()
    elif i==12:
        tan()
    elif i==13:
        factorial()
    elif i==14:
        gcd()
    elif i==15:
        print('exit')
        break
    else:
        print('invalid')