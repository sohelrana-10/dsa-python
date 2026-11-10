def right_shift(arr,k):
    n=len(arr)
    k=k%n

    while(k!=0):
        last=arr[n-1]
        for i in range(n-1,-1,-1):
            arr[i]=arr[i-1]
        arr[0]=last
        k-=1    
    return arr

arr=[1,2,3,4,5]
k=6
#output
#[5,1,2,3,4]
print(right_shift(arr,k))