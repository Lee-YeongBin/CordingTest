from typing import List

## 내가 푼 답
def two_sum(nums : List[int], target: int) -> List[int]:
    i = 0
    while(i < len(nums)):
        j = i+1
        while(j < len(nums)):
            if(nums[i] + nums[j] == target):
                return i,j
            j+=1
        i+=1


## in을 이용한 탐색
def two_sum_in(nums : List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]

