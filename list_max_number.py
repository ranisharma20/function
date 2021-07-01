def max(list):
    i=0
    a=[]
    while i<len(list):
        j=0
        max=0
        while j<len(list[i]):
            if list[i][j]>max:
                max=list[i][j]
            j=j+1
        a.append(max)
        i=i+1
    print(a)
max([[3,5,65,7],[7,9,12,15,28],[6,78,90,98],[9,78,67,56,65],[78,56,45,34,100,200]])

