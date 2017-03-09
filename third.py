# cook your dish here
test=int(input())
for i in range(test):
    size=int(input())
    el01=list(map(int,input().split()))
    el01.sort()
    for j in range(size):
        if(el01[j]!=el01[j-1]+1 and j!=0):
            if(j!=size-1 and el01[j+1]!=el01[j]+1):
                fault=el01[j]
            elif(j!=size-1 and el01[j+1]==el01[j]+1):
                fault=el01[j-1]
            elif(j==size-1):
                fault=el01[j]
    print(fault)        
            