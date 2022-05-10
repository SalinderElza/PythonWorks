a, b = map(int, input().split())
anna, bora = set(), set()
for _ in range(a):
    anna.add(int(input()))
for _ in range(b):
    bora.add(int(input()))
print(len(anna & bora))
print(*sorted(anna & bora))
print(len(anna - bora))
print(*sorted(anna - bora))
print(len(bora - anna))
print(*sorted(bora - anna))
