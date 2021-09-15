from typing import List

def three_sum(nums : List[int]):
    nums.sort()
    i = 0
    result = []
    while i < len(nums)-2:
        j = i + 1
        while j <len(nums)-1:
            k = j + 1
            while k < len(nums):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                k += 1
            j+=1
        i+=1
    return result

n = [-1, 0, 1, 2, -1, -4]

print(three_sum(n))







