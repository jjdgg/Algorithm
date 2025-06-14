[Silver 3] 모든 순열 - 10974
문제 링크

성능 요약
메모리: 31256 KB, 시간: 72 ms

구분
백트래킹 > 순열

채점결과
정확성: 100.0<br/>합계: 100.0 / 100.0

제출 일자
2025년 06월 14일

문제 설명
1부터 N까지의 수로 이루어진 순열을 사전 순으로 출력하는 프로그램을 작성하시오.

예를 들어, N=3일 때 가능한 모든 순열은 다음과 같다:

복사
편집
1 2 3  
1 3 2  
2 1 3  
2 3 1  
3 1 2  
3 2 1
이와 같이, 중복 없이, 사전 순으로 정렬된 모든 순열을 출력해야 한다.

입력
첫째 줄에 정수 N이 주어진다. (1 ≤ N ≤ 8)

출력
N!개의 줄에 걸쳐, 각 줄에 1부터 N까지의 순열 하나를 출력한다.

입출력 예
입력	출력
3	1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

해결 방법
이 문제는 백트래킹 또는 itertools.permutations를 이용해서 풀 수 있다.
직접 구현할 경우 used 배열을 사용하여 중복 없이 순열을 생성하면 된다.

파이썬 코드 예시 1: itertools 사용
from itertools import permutations

n = int(input())
for p in permutations(range(1, n+1)):
    print(*p)
파이썬 코드 예시 2: 백트래킹 직접 구현
n = int(input())
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

dfs()
