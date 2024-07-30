import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ch = random.choice(alphabet)
print(ch)
first = "NG"
while first == "NG":
    val = input()
    if val == ch:
        first = "OK"
        print(first)
        break
    print(first)

