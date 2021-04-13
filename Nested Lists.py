students=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])
students=sorted(students,key=lambda x:x[1])
second=sorted(list(set([x[1] for x in students])))[1]
desired=[]
for stu in students:
    if stu[1]==second:
        desired.append(stu[0])
print("\n".join(sorted(desired)))
