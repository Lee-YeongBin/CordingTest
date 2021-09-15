from typing import List

def max_profit(nums : List[int]) -> int:
    min_value = min(nums)
    difference = []
    for i in range(len(nums)):
        difference.append(nums[i] - min_value)
    print(difference)

    for i in range(len(difference)):
        if difference[i] == 0:
            index = difference.index(difference[i])

    return max(difference[index:])

nums = [7,1,5,3,6,4]
print(max_profit(nums))