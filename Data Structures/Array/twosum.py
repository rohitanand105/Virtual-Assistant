# a = int(input())
def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target - nums[i] == nums[j]:
                return[i,j]
    
    return None

text = [2,7,11,15, 24]
target = 9
print(twosum(text, target))



