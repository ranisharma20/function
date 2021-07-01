list=[2,3,4,5,6,8] 
i=0
a=[]
while i<len(list):
    j=1
    count=0
    while j<=(list[i]):
        if list[i]%j==0:
            count=count+1
        j=j+1
    if count==2:
        a.append(list[i])
    i=i+1
print(a)