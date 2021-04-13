A=set(map(int,raw_input().split()))
for i in range(int(raw_input())):
    X=set(map(int,raw_input().split()))
    if A.issuperset(X) !=True or len(A)==len(X):
        print(False)
        break
else:
    print(True)




