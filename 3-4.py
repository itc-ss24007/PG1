for i in range(10):
    if i % 2 == 0:
        continue
        print(i * 10)
    print(i)

print("break")

for i in range(10):
    if i % 2 == 0:
        print(i+100)
        break
    print(i)
