words = input()
times = [-1]*26

for i in range(len(words)):
    if times[ord(words[i]) - ord('a')] == -1:
        times[ord(words[i]) - ord('a')] = i

for i in times:
    print(i, end=' ')