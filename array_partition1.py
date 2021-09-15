from typing import List

def array_partition(nums : List[int]) -> int:
    n = int(len(nums)/2)
    nums.sort()
    result = 0
    k = 0
    j = 2
    for i in range(n):
        pair = nums[k:j]
        result += min(pair[0] , pair[1])
        k += 2
        j += 2

    return result

nums = [6,2,6,5,1,2]

print(array_partition(nums))

