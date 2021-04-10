import csv

class_no0 = []
name0 = []
surname0 = []
task0 = []
grade0 = []

with open('students.csv', 'r', encoding='utf-8') as csvfile:
    keys = ['class', 'name', 'surname', 'task', 'grade']
    reader = csv.DictReader(csvfile, fieldnames=keys)
    for col in reader:
        class_no0.append(col['class'])
        name0.append(col['name'] + ' ' + col['surname'])
        task0.append(col['task'])
        grade0.append(col['grade'])


names = name0[1::]
class_no = class_no0[1::]
tasks = task0[1::]
grades = [int(i) for i in grade0[1::]]

due_date = 'the 31st of May 2021'

message = "Hi {},\n\nThis is a reminder that you have {} tasks left to \
submit before you can graduate.\nYou're current grade is {} and can increase \
to {} if you submit all assignments before the due date .\n\n"

for name, task, grade in zip(names, tasks, grades):
    print(message.format(name, task, grade, int(grade) + 1))
