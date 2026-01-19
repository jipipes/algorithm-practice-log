n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
# scores = [score/m*100 for score in scores]

ave = sum(score / m for score in scores) * 100 /n
print(ave)