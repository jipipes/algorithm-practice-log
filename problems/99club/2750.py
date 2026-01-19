# 선택정렬, 버블정렬, 삽입정렬, 퀵정렬 각각 활용

n = int(input())
A = list(map(int, input().split()))

def selection_sort(A):
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if (A[j]<A[least]):
                least = j
        A[i], A[least] = A[least], A[i]
        print(A, i+1)

selection_sort(A)