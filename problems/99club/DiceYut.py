
# graph = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], 
#         [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], 
#         [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32]
# ]

# score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 
#          0, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35]

n = list(map(int, input().split()))

sc = [0] * 33
bluepath = [[5, 22, 23, 24, 30, 31, 32, 20, 21], 
[10, 25, 26, 30, 31, 32, 20, 21], 
[15, 27, 28, 29, 30, 31, 32, 20, 21]
]

for i in range(21):
    sc[i] = i * 2
sc[22], sc[23], sc[24] = 13, 16, 19
sc[25], sc[26] = 22, 24
sc[27], sc[28], sc[29], sc[30], sc[31], sc[32] = 28, 27, 26, 25, 30, 35

result = 0
yut = [0, 0, 0, 0]

def dfs(i, yut, sum_score):
    global result
    if i == 10:
        result = max(result, sum_score)
        return
    
    for y in range(4):
        temp = yut[y]
        if temp == 21:
            continue
        if temp == 5 or (22 <= temp <= 24):
            index = bluepath[0].index(temp)
            if n[i] + index <= 8:
                go = bluepath[0] [n[i]+index]
            else:
                go = 21
        elif temp == 10 or temp == 25 or temp == 26:
            index = bluepath[1].index(temp)
            if n[i] + index <= 7:
                go = bluepath[1] [n[i]+index]
            else:
                go = 21
        elif temp == 15 or (27 <= temp <= 32):
            index = bluepath[2].index(temp)
            if n[i] + index <= 8:
                go = bluepath[2] [n[i] + index]
            else:
                go = 21
        else:
            if temp + n[i] <= 21:
                go = temp + n[i]
            else:
                go = 21
        
        if go in yut and go!= 21:
            continue
        
        yut[y] = go
        dfs(i+1, yut, sum_score+sc[go])
        yut[y] = temp

dfs(0, yut, 0)
print(result)