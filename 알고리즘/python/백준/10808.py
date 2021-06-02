words = list(input())
times = [0]*26

for i in words:
    times[ord(i) - ord('a')] += 1

for i in times:
    print(i, end=' ')