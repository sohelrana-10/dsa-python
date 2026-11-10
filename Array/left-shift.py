def lef_shift(arr,k):
    n=len(arr)
    k=k%n
    while(k!=0):
        first=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=first
        k-=1
    return arr        

arr=[1,2,3,4,5]
k=12
print(lef_shift(arr,k))