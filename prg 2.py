def slection_sort(L1):
    p=len(L1)
    for i in range(0,p-1):
        min=i
        for j in range(i+1,p):
            if(L1[j]<L1[min]):
                min=j
        temp=L1[i]
        L1[i]=L1[min]
        L1[min]=temp
    print("Elements i ascending order:")
    for i in range(0,p):
        print(L1[i],sep="")

def bubble_sort(L1):
    print("Elements of the list",L1)
    p = len(L1)
    for i in range (0, p):
        for j in range(0, (p-1-i)):
            if(L1[j] > L1[j+1]):
                temp = L1[j]
                L1[j] = L1[j+1]
                L1[j+1] = temp
    print("Elements in ascending order")
    for i in range(0,p):
        print(L1[i],sep="")

def insertion_sort(L1):
    print("List elements:",L1)
    p = len(L1)
    for i in range(1, p):
        temp = L1[i]
        ptr = i-1
        while(L1[ptr] > temp and ptr >= 0):
            L1[ptr+1] = L1[ptr]
            ptr = ptr - 1
        else:
            L1[ptr + 1] = temp
    print("List elements in ascending order:")
    for i in range(1, p):
        print(L1[i])

while True:
    L1=[]
    x=int(input("enter the limit:"))
    for i in range(x):
        dat=int(input("enter the number:"))
        L1.append(dat)
    print("1.)selection sort,2.)bubbble sort,3.)insertion sort")
    y=int(input("enter your option:"))
    if y==1:
        slection_sort(L1)
    elif y==2:
        bubble_sort(L1)
    elif y==3:
        insertion_sort(L1)
    else:
        print("error")
    
    
    
