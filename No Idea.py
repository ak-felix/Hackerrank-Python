n,m=(int(i) for i in raw_input().split())
l=map(int, raw_input().strip().split(' '))
a=set(map(int,raw_input().strip().split(' ')))
b=set(map(int,raw_input().strip().split(' ')))
result=0
for i in l:
    if i in a:
        result+=1
    if i in b:
        result+=-1
print(result)
