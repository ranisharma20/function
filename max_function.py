def function_max(list):
    i=0
    c=0
    while i<len(list):
        if (list[i]>c):
            c=list[i]
        i=i+1
    print(c)
function_max([2,4,7,8,9,12,15,16])

