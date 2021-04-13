N=int(raw_input())
storage=map(int,raw_input().split())
storage=sorted(storage)

for i in range(len(storage)):
    if(i!=len(storage)-1):
        if(storage[i]!=storage[i-1] and storage[i]!=storage[i+1]):
            print(storage[i])
            break
    else:
        print(storage[i])
            
