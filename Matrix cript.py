import math
import os
import random
import re
import sys




first_multiple_input = raw_input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in xrange(n):
    matrix_item = raw_input()
    matrix.append(matrix_item)

matrix=list(zip(*matrix))
sample=str()
for words in matrix:
    for char in words:
        sample+=char
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)',' ', sample))
