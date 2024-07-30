with open('sample.txt','r') as f:
    line = f.readline()
print(line)

with open('sample.txt','r') as f:
    lines = f.readlines()
print(lines)

with open('sample1.txt','w') as f:
    f.write('test')

with open('sample1.txt','a') as f:
    f.write('test1')

with open('sample.txt','r') as f:
    for line in f:
        print(line.strip())

with open('numbers.txt','r') as f:
    sum =0
    for data in f:
        num = int(data)
        sum += num
    print(sum)
