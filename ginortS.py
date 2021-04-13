def sortt(s):
    l=[]
    u=[]
    o=[]
    e=[]
    for char in s:
        if char.islower():
            l.append(char)
        elif char.isupper():
            u.append(char)
        elif char.isdigit():
            if int(char)%2==0:
                e.append(char)
            else:
                o.append(char)
    return (''.join(sorted(l)+sorted(u)+sorted(o)+sorted(e)))
if __name__=='__main__':
    S=raw_input()
    print(sortt(S))
