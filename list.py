a = [2,4,6,8]
b = [1,3,5,7]

size_1 = len(a)
size_2 = len(b)

res = []

i,j = 0,0

while i<size_1 and j<size_2:
    if a[i] < b[j]:
        res.append(a[i])
        i+=1
    else:
        res.append(b[j])
        j += 1
res = res +a[i: ] + b[j: ]
print(str(res))

