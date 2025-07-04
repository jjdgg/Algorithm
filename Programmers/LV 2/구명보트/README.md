# [Programmers Lv.2] 구명보트

## 문제 링크  
[https://school.programmers.co.kr/learn/courses/30/lessons/42885](https://school.programmers.co.kr/learn/courses/30/lessons/42885)  
📌 분류: `Greedy`, `Two Pointers` | 난이도: 레벨 2

---

## 문제 설명  

사람들의 몸무게가 담긴 배열 `people`과  
한 번에 탈 수 있는 구명보트의 무게 제한 `limit`이 주어집니다.  
**각 구명보트에는 최대 2명까지 탈 수 있으며**, 두 사람의 무게 합이 limit 이하여야 합니다.  

이때, 모든 사람을 구출하기 위한 **최소한의 보트 수**를 구하는 문제입니다.

---

## 제한사항  
- 1 ≤ people.length ≤ 50,000  
- 40 ≤ people[i] ≤ 240  
- 40 ≤ limit ≤ 240  
- 몸무게는 정수

---

## 입출력 예  

| people | limit | return |
|--------|--------|--------|
| [70, 50, 80, 50] | 100 | 3 |
| [70, 80, 50] | 100 | 3 |

---

## 풀이 후기

처음에는 **몸무게가 작은 사람 두 명을 묶는 전략**으로 접근했지만,  
이 방식은 **전체 최적을 보장하지 못해 실패**했습니다.  

예를 들어, 무거운 사람과 가벼운 사람을 묶을 수 있음에도  
가벼운 사람들끼리만 먼저 처리하면 무거운 사람은 혼자 타야 하는 경우가 생겨  
**보트 수가 더 많아지게 됩니다.**

그래서 **정렬 후, 가장 가벼운 사람(i)과 가장 무거운 사람(j)을 비교하는 투포인터 방식**을 적용했습니다.

- 두 사람을 같이 태울 수 있으면 함께 태우고 `i`, `j` 포인터를 모두 이동  
- 안 되면 무거운 사람만 태우고 `j` 포인터만 이동  
- 어쨌든 한 명은 무조건 타기 때문에 반복마다 `보트 수 +1`

---

## 최종 코드 – ✅ 투 포인터 (사용자 구현)
```python
def solution(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    count = 0
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1  # 가벼운 사람 태움
        j -= 1  # 무거운 사람은 무조건 태움
        count += 1  # 보트 사용
    return count
```

---

## 핵심 아이디어

- 정렬 후 양 끝에서 투포인터로 접근
- 가장 무거운 사람은 보트 하나 필요 → 최대한 짝 지어 태우기
- 최적의 그리디 전략: 가벼운 사람 + 무거운 사람을 최대한 짝지음

---

## 🏁 결과 요약

| 항목 | 값 |
|------|----|
| 결과 | 정확성 100% |
| 언어 | Python 3 |
| 채점 통과 | O |
| 유형 | 그리디, 투 포인터 |
