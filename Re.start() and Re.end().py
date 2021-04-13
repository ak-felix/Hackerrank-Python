import re
string=raw_input()
sybstring=raw_input()
pattern=re.compile(sybstring)
match=pattern.search(string)
if  not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(),match.end() -1))
    match=pattern.search(string,match.start()+1)
