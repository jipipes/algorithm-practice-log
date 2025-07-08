import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))
solution.sort() 

left_index = 0
right_index = N - 1

abnum = abs(solution[left_index] + solution[right_index])
ab_left = left_index
ab_right = right_index

while left_index < right_index:
    mix = solution[left_index] + solution[right_index]

    if abs(mix) < abnum:
        ab_left = left_index
        ab_right = right_index
        abnum = abs(mix)
    
        if abnum == 0:
            break
    
    if mix < 0:
        left_index += 1
    
    else:
        right_index -= 1

print(solution[ab_left], solution[ab_right])