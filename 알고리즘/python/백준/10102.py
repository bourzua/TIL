v = int(input())
vote = input()
a = vote.count("A")
b = v - a

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")