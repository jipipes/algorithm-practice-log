from itertools import zip_longest

matrix = [input() for _ in range(5)]

result = "".join(char for row in zip_longest(*matrix, fillvalue='') for char in row if char)

print(result)

