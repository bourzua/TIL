import sys

words = sys.stdin.readline().rstrip()
wordsList = []

for _ in words:
    wordsList.append(words)
    words = words[1:]

for i in sorted(wordsList):
    print(i)