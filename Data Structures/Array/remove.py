a= [0,2,4,2,215,2,8,2,26,8,2,9,2]
n = len(a)
val = 2

temp = [0]*n

pivot = 0

for i in range(0,(n)):
    if a[i] != val:
        temp[pivot] = a[i]
        pivot = pivot +1

# temp[pivot] = a[n-1]

print(temp[0:(pivot)])



