# [Silver 3] 모든 순열 - 10974

> 백준 문제 링크: [https://www.acmicpc.net/problem/10974](https://www.acmicpc.net/problem/10974)

## ✅ 성능 요약
- 메모리: 31,256 KB
- 시간: 72 ms

## ✅ 구분
- 백트래킹 > 순열

## ✅ 채점결과
- 정확성: 100.0  
- 합계: 100.0 / 100.0

## ✅ 제출 일자
- 2025년 06월 14일

---

## 📘 문제 설명

1부터 N까지의 수로 이루어진 **모든 순열**을 사전 순으로 출력하는 프로그램을 작성하시오.

예를 들어, N = 3일 경우 가능한 순열은 다음과 같다:


---

## 📥 입력

- 첫째 줄에 정수 **N**이 주어진다. (1 ≤ N ≤ 8)

## 📤 출력

- N!개의 줄에 걸쳐, 각 줄에 1부터 N까지의 순열 하나를 출력한다.

---

## 💡 입출력 예

| 입력 | 출력 |
|------|------|
| `3` | `1 2 3`<br>`1 3 2`<br>`2 1 3`<br>`2 3 1`<br>`3 1 2`<br>`3 2 1` |

---

## 🧠 해결 방법

이 문제는 **백트래킹** 혹은 `itertools.permutations`를 이용해 해결할 수 있습니다.

- 직접 구현 시에는 `visited` 배열과 `path`를 활용하여 중복 없이 순열을 생성하는 **DFS 방식의 백트래킹**을 사용합니다.
- `itertools.permutations`를 활용하면 간결하게 모든 순열을 생성할 수 있습니다.

---

## ✅ 파이썬 코드 예시 1: `itertools` 사용

```python
from itertools import permutations

n = int(input())
for p in permutations(range(1, n+1)):
    print(*p)```
✅ 파이썬 코드 예시 2: 백트래킹 직접 구현
```n = int(input())
visited = [False] * (n + 1)
path = []

def dfs():
    if len(path) == n:
        print(*path)
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            dfs()
            path.pop()
            visited[i] = False

dfs()```
📌 관련 개념
브루트포스 탐색 (완전 탐색)

백트래킹 (가지치기를 통한 효율적 탐색)

순열 생성

