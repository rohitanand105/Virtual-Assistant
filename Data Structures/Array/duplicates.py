def remove(arr):
    n = len(arr)
    if(n==0 or n == 1):
        return arr
    
    temp = [0]*n
    pivot = 0

    for i in range(0,n-1):
        if arr[i] != arr[i+1]:
            temp[pivot] = arr[i]
            pivot = pivot + 1

    temp[pivot] = arr[n-1]
    return temp[0:pivot+1]



a = [0,1,1,4,4,7,8,15,15,19]
print(remove(a))


 












