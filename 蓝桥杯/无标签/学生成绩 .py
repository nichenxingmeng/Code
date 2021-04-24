n = int(input().strip())
student = []

class Student:
    def __init__(self, name, gender, age, grade):
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade

for i in range(n):
    a, b, c, d = input().strip().split()
    c, d = int(c), int(d)
    student.append(Student(a, b, c, d))

student.sort(key = lambda x: x.grade)
for i in student:
    print(i.name, i.gender, i.age, i.grade)
