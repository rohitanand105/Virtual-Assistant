a = [28,56,44,128,22,85,46,48,552,182]
b = []

while a:
    min = a[0]
    for x in a:
        if x < min:
            min = x
    b.append(min)
    a.remove(min)

print(b)


    

