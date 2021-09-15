#리스트를 복사하는것의 시간복잡도가 O(n)이라서 타임아웃이 된것같다.....

from typing import List
from functools import reduce

def product_except_self(nums : List[int]) -> List[int]:
    result = []
    clone = list(nums)
    sum = 1
    for i in range(len(nums)):
        nums = list(clone)
        nums.remove(nums[i])
        result.append(reduce(lambda x, y: x * y, nums))

    return result

nums = [1,2,3,4]
print(product_except_self(nums))