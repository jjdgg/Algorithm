# [Programmers Lv.1] 체육복

## 문제 링크  
[https://school.programmers.co.kr/learn/courses/30/lessons/42862](https://school.programmers.co.kr/learn/courses/30/lessons/42862)  
📌 분류: `Greedy`, `Implementation` | 난이도: 레벨 1

---

## 문제 설명  

전체 학생 수 `n`, 도난당한 학생 번호 배열 `lost`, 여벌 체육복을 가져온 학생 번호 배열 `reserve`가 주어졌을 때,  
체육수업을 들을 수 있는 학생 수의 **최댓값**을 구하는 문제입니다.

- 여벌이 있는 학생이 도난당한 경우, 본인이 입는 것을 우선시
- 여벌 체육복은 바로 앞번호나 뒷번호 학생에게만 빌려줄 수 있음

---

## 제한사항  
- 전체 학생 수: 2 ≤ n ≤ 30  
- 체육복을 도난당한 학생 수: 1 ≤ lost ≤ n  
- 여벌 체육복을 가져온 학생 수: 1 ≤ reserve ≤ n  
- 여벌 가져온 학생과 도난당한 학생이 겹칠 수 있음

---

## 입출력 예  

| n | lost | reserve | return |
|---|------|---------|--------|
| 5 | [2, 4] | [1, 3, 5] | 5 |
| 5 | [2, 4] | [3] | 4 |
| 3 | [3] | [1] | 2 |

---

## 입출력 예 설명  

- 예제 1: 여벌을 가진 학생들이 도난당한 학생 모두에게 체육복을 빌려줄 수 있음 → 전원 참여
- 예제 2: 3번이 2번 또는 4번 중 1명에게만 빌려줄 수 있으므로 1명은 수업 못 들음

---

## 풀이 후기

처음에는 여벌 배열과 도난 배열을 순서대로 비교했지만,  
**여벌+도난 중복 처리**를 먼저 해주지 않으면 오답이 나올 수 있습니다.

1. 여벌과 도난 배열의 **교집합** 먼저 제거
2. 앞뒤 번호를 순회하며 체육복을 빌려줄 수 있는 경우 처리
3. 전체 인원에서 아직도 체육복이 없는 인원을 빼면 정답

---

## 최종 코드 –  그리디 알고리즘
```python
def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    return n - len(lost_set)
```

## 핵심 아이디어
- 여벌이 있지만 도난당한 학생은 우선적으로 자신이 입도록 처리
- 여벌이 있는 학생은 앞 → 뒤 순서로 도난 학생에게 체육복을 빌려줌
- 집합(Set) 연산을 통해 교집합 제거 및 탐색 효율화

## 🏁 결과 요약
| 항목 | 값 |
|------|----|
| 결과 | 정확성 100% |
| 언어 | Python 3 |
| 채점 | 통과 O |
| 유형 | 그리디, 구현 |
