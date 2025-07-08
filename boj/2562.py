#한 줄에 하나씩 숫자가 주어지는 경우 어떻게 처리해야 할까?
import sys

nums = [int(sys.stdin.readline().strip()) for _ in range(9)]
max_index = nums.index(max(nums)) + 1
print(f"{max(nums)}\n{max_index}")
#\n은 문자열 내부에서만 사용가능하고, 지금 코드에서는 연산자로 인식하기 때문에 올바르게 사용하려면 문자열로 감싸야 한다
#더 좋은 방법은 f-string 사용하는 것
