### List의 인덱스 0 부터 탐색, 음수인 값은 예외처리하고 0이 아닌 숫자를 만나면 그 수를 기준으로 삼는다.
### 그 뒤의 숫자들을 차례로 탐색한다. 기준인 수보다 크거나 같은 숫자를 만나면 정지
### 지나온 숫자들은 기준 수보다 작음, (기준수 - 지나온 수)를 계산한다 ex) (2-1) + (2-0) + (2-1) = 4
### 모든 숫자를 기준으로 이를 계산하여 더한값을 리턴한다.

# 풀이실패
from typing import List

def Trapping(height : List[int]) -> int:
    for i, h in enumerate(height):
        water = 0
        for j in range(i + 1, len(height) + 1):
            if(height[i] < height[j]):
                water += 1
                break

he = [0,1,0,2,1,0,1,3,2,1,2,1]
if(he[0] < he[i:]):
    print(1)



