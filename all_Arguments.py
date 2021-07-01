#1 pojaction argument
def add (a,b,c):
    r=a+b+c
    return r
print(add(5,6,7))

#2 arbitry keywords argument
def my_fun(**kwarges):
     print(kwarges)
my_fun(a=10,b=6,c=5)

#3  arbitry argument
def add(*name):
    print(name)
add("rani","tapas","preeti","vicky","shalini")

#4 defult argument
def fun(a,b=5):
    c=a+b
    print(c)
fun()

#5keyword argument
def fum(a,b,c):
    d=a+b+c
    print(d)
fum(a=1,b=4,c=4)
