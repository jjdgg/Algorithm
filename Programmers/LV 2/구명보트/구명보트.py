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