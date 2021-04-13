from collections import *
N,students=input(),namedtuple('students',raw_input().split())
stud= [students(*raw_input().split()) for i in range(N)]
print sum([float (i.MARKS) for i in stud])/N
