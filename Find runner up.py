A=[]
i=int(input())
A=list(map(int,input().split()))[:i]
A.sort(reverse= True)
A 
i=0
while(True):
    if A[i]==A[i+1]:
        i+=1
    
    else:
        print(A[i+1])
        break

