from itertools import permutations

N = int(input())
arr = [i for i in range(1, N+1)]

perm = permutations(arr)
for p in perm:
    print(*p)