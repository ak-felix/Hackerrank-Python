def main():
    for i in range(int(raw_input())):
        a=int(raw_input());A=set(raw_input().split())
        b=int(raw_input());B=set(raw_input().split())
        print('True' if A.union(B)==B else 'False')
if __name__=='__main__':
    main()
