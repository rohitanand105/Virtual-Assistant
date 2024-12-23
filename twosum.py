nums = [1,2,3,4,5,6,3,6,9,44,63,32]

target = 8

temp= 0

while temp<= nums[-1]:
    if ((nums[0] + nums[temp]) == target):
        print(nums[0] and nums[temp])
    temp += 1

