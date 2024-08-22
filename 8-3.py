import collections

data = 'すもももももももものうち'
count_dict = {}
for v in data:
    if v in count_dict:
        count_dict[v]+=1
    else:
        count_dict[v]=1
print(count_dict)

count_dic = collections.defaultdict(int)
for v in data:
    count_dic[v] +=1
print(count_dic)

count_dic = collections.defaultdict(list)
for v in data:
    count_dic[v].append(v)
print(count_dic)

counter = collections.Counter(data)
print(counter)

CharCount = collections.namedtuple('CharCount',['char','count'])
mo = CharCount('も',8)
print(mo)

count= collections.Counter(data)
res_dict = collections.defaultdict(list)
for ch,cnt in count.items():
    res_dict[cnt].append(ch)
print(res_dict)
print(res_dict[1])


