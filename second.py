test=int (input())
for i in range (test):
    el1=[]
    el2=[]
    task=int (input())
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    
    el1= list(map(int,input().split()))
    el2=list(map(int,input().split()))
    for j in range  (task):
        
       
        if j%2==0:
            sum1=sum1+el1[j]
        elif j%2!=0:
            sum2=sum2+el1[j]
    for k in range(task):
        
        if k%2==0:
            sum3=sum3+el2[k]
        elif k%2!=0:
            sum4=sum4+el2[k]
    if(sum1+sum4)>=(sum2+sum3):
        print(sum2+sum3)
    elif(sum1+sum4)<=(sum2+sum3):
        print(sum1+sum4)
    
    