i_num_list = range(1,11)
s_num_list = list(map(lambda i: "NO."+ str(i),i_num_list))
print("文字列リスト:",s_num_list)
print("\n")

for s in map(lambda i :"NO."+str(i),range(1,11)):
    print(s,end=" ")
print("\n")

for e in filter(lambda i : i%2==0,range(1,11)):
    print(e,end=" ")
print("\n")
