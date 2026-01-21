class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        s1 = set(nums)
        for i in range(len(nums)):
            if i+1 in s1:
                continue
            else:
                result.append(int(i+1))
        return result

# Pesudo code
# 1. 리스트를 집합으로 변환한 후 숫자를 확인한다
# 2. 집합 안에 없으면 새로운 리스트에 넣는다
# 3. 새로운 리스트를 반환한다