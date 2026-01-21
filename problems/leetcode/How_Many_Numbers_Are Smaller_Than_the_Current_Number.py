class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
                else: 
                    continue
            result.append(count)    
        return result


# psedo code
# 1. 배열을 돈다
#    1.1. 배열을 돌면서 자신보다 작은 수의 개수를 센다
#    1.2. 개수를 새로운 배열에 넣는다
# 2. 새로운 배열을 반환한다

# 이중 반복문이 꼭 필요할까? 안쓰고 푸는 방법 있을 것 같은대
# 시간복잡도를 줄이는 방향으로 다시 풀어보기