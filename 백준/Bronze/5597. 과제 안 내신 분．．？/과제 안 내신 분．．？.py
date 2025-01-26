student = [i for i in range(1,31)]

for i in range(28):
    input_data = int(input())
    student.remove(input_data)

print(student[0])
print(student[1])