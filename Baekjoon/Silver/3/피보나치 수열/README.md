
# [BOJ 1003] 피보나치 수열

## 문제 링크  
[https://www.acmicpc.net/problem/1003](https://www.acmicpc.net/problem/1003)  
📌 분류: `Dynamic Programming (DP)` | 난이도: 실버 3

---

## 성능 요약  
- 메모리: 32,412 KB  
- 시간: 36 ms  

---

## 구분  
- 백준 온라인 저지 > 동적 계획법

---

## 문제 설명  

다음과 같이 정의된 피보나치 함수를 호출할 때,  
각 호출에서 0과 1이 각각 몇 번 출력되는지를 구하는 문제입니다.

```python
def fibonacci(n):
    if n == 0:
        print("0")
        return 0
    elif n == 1:
        print("1")
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

예를 들어 `fibonacci(3)`을 호출하면 다음과 같이 호출됩니다:

```
fibonacci(3)
 ├─ fibonacci(2)
 │   ├─ fibonacci(1) → 1 출력
 │   └─ fibonacci(0) → 0 출력
 └─ fibonacci(1) → 1 출력
```

→ 이때 `0`은 1번, `1`은 2번 출력됩니다.

---

## 제한사항  
- 0 ≤ n ≤ 40  
- 테스트케이스 수 T는 1 이상 50 이하  
- 각 테스트케이스마다 정수 n (0 ≤ n ≤ 40)

---

## 입출력 예  

| 입력 | 출력 |
|------|------|
| 3<br>0<br>1<br>3 | 1 0<br>0 1<br>1 2 |

---

## 입출력 예 설명  

- `fibonacci(0)`을 호출하면 0만 출력되므로 결과는 `1 0`
- `fibonacci(1)`을 호출하면 1만 출력되므로 결과는 `0 1`
- `fibonacci(3)`은 위 예시처럼 호출되므로 `1 2`

---

## 풀이 후기

처음에는 문제에서 제시한 재귀 함수를 그대로 구현해서 `zero_count`와 `one_count`를 추적하는 방식으로 풀었습니다.

### 1차 시도 – ❌ 재귀 그대로 구현
```python
def fib(n, zero_count, one_count):
    if n == 0:
        zero_count += 1
        return 0, zero_count, one_count
    elif n == 1:
        one_count += 1
        return 1, zero_count, one_count
    else:
        _, z1, o1 = fib(n - 1, zero_count, one_count)
        _, z2, o2 = fib(n - 2, zero_count, one_count)
        return 0, z1 + z2, o1 + o2
```

하지만 이 방식은 답은 나오지만 중복 호출이 너무 많아지면서 결국 **시간 초과**가 발생했습니다.

그래서 **동적 계획법(DP)**으로 전략을 바꿔서 `fib(n)`을 호출할 때 출력되는 0과 1의 개수를 **메모이제이션** 해두었습니다.  
이후 각 테스트케이스에 대해 `dp[n]`을 바로 조회하는 방식으로 최적화했습니다.

### 2차 시도 – ✅ 동적 프로그래밍(DP)
```python
T = int(input())
dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])
```
결과적으로 시간도 빠르고 정확도도 100%를 받을 수 있었습니다.

---

## 핵심 아이디어

- `dp[n] = [fib(n) 호출 시 0 출력 횟수, 1 출력 횟수]` 형태로 저장
- DP 테이블은 미리 0~40까지 채워두고, 테스트케이스마다 O(1)로 출력
- 중복 계산 제거 + 메모이제이션 → 전형적인 피보나치 DP 유형 문제

---

## 🏁 결과 요약

| 항목 | 값 |
|------|----|
| 결과 | 맞았습니다!! |
| 시간 | 36 ms |
| 메모리 | 32,412 KB |
| 제출 번호 | 95363639 |
| 언어 | Python 3 |
| 정확성 | 100.0 / 100.0 |
