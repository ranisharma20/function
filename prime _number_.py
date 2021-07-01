def prime():
    num=int(input("enter the number"))
    count=0
    i=1
    while i<=num:
        if num%i==0:
            count=count+i
            i=i=+1
        if count==2:
            print("prime number")
    else:
        print("not prime")
prime()