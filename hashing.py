n = [1, 2, 3, 5, 1, 2, 3, 5, 7, 8, 8, 8, 10]
m = [1, 3, 4, 6, 7, 8, 10, 2, 5]
hash_list={}
for num in n:
    if num in hash_list:
        hash_list[num]+=1
    else:
        hash_list[num]=1
    
for num in m:
    print(f"{num}-> {hash_list.get(num,0)}")

###################################################

for num in n:
    hash_list[num]=hash_list.get(num,0)+1

for num in m:
     print(f"{num}-> {hash_list.get(num,0)}")

########################################################


text = "aAbBcCzZyYxX"   # sample string with lowercase + uppercase
m = ["a", "b", "c", "z", "A", "B", "C", "Z"]
hash_list=[0]*123
for ch in text:
    ascii=ord(ch)
   
    hash_list[ascii]+=1

for ch in m:
    ascii=ord(ch)
    
    print(f"{ch}->{hash_list[ascii]}")

############################################################
#using dict same question
text = "aAbBcCzZyYxX"   # sample string with lowercase + uppercase
m = ["a", "b", "c", "z", "A", "B", "C", "Z"]
hash_list={}
for ch in text:
    hash_list[ch]=hash_list.get(ch,0)+1

for ch in m:
    print(f"{ch}->{hash_list.get(ch,0)}")