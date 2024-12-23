a= [1,8,15,41,82,193,258,522]
n = 258
l = 0
u = len(a) -1

while l<= u:
    mid = (l+u) // 2

    if  a[mid] == n:
        print("Number found", a[mid])
        exit
    else:
        if a[mid] < n:
            l = mid
        else:
            u = mid

    