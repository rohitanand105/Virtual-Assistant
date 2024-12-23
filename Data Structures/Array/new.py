a = [0,0,2,2,4,4,5,5,6,7,7,8,8,45,45,56,56]

n = len(a)
temp = [0]*n
pivot = 0


for i in range(0, (n-1)):
    if a[i] != a[i +1]:
        temp[pivot] = a[i]
        pivot = pivot + 1

temp[pivot] = a[n-1]

print(temp[0:pivot+1])




