# 풀이가 느려지는 대표적인 이유
---

## 1. 멤버십 연산(in)의 숨겨진 비용: List vs Set
알고리즘 효율성을 결정하는 흔한 병목 지점 중 하나는 특정 요소가 컬렉션 안에 있는지 확인하는 in 연산이다. 
사용하는 자료형에 따라 전체 시간 복잡도가 O(n)에서 O(n^2)으로 급격히 변할 수 있다.

### 1.1. 자료형별 in 연산의 시간 복잡도
- 리스트: O(n) (Linear Search)처음부터 끝까지 하나씩 비교하므로 데이터 크기에 비례하여 시간이 늘어난다.
- 집합 / 딕셔너리: O(1) (Hash Table)해시 함수를 통해 데이터의 위치를 바로 찾으므로 데이터 크기와 상관없이 거의 즉시 결과를 반환한다.

### 1.2. 중첩 루프에서의 성능 저하 (Case Study)
```python
# ❌ 성능 저하 사례: O(n^2)
# n번 반복하는 loop 내부에서 O(n)인 list 'in' 연산 수행
seen_list = []
for num in nums:
    if num in seen_list: # 여기서 매번 리스트 전체를 스캔
        duplicate = num
    seen_list.append(num)

# ✅ 성능 최적화 사례: O(n)
# n번 반복하는 loop 내부에서 O(1)인 set 'in' 연산 수행
seen_set = set()
for num in nums:
    if num in seen_set: # 즉시 확인
        duplicate = num
    seen_set.add(num)
```
