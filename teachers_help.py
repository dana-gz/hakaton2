import csv

def read_data():
    """function reads the data from file csv"""
    while True:
        filename = 'students.csv'
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                keys = ['class', 'name', 'surname', 'task', 'grade']
                reader = csv.DictReader(csvfile, fieldnames=keys)
                for col in reader:
                    class_no0.append(col['class'])
                    name0.append(col['name'] + ' ' + col['surname'])
                    task0.append(col['task'])
                    grade0.append(col['grade'])
                break
        except FileNotFoundError:
            print('File not found. Try again ;) ')
        break


class_no0 = []
name0 = []
task0 = []
grade0 = []

read_data()

# the table in the csv file has headings and my program cannot mark the headings in the file so I have to cut them
names = name0[1::]
tasks = task0[1::]
grades = grade0[1::]
grades_up = grade0[1::]
# I need 2 lists for grades because 1 of them will be incremented 1 value up

due_date = 'the 31st of May 2021'



# the grades form csv file are introduced as strings to add +1 it is necessary to change them into int format
for i in range(len(grades_up)):
    try:
        grades_up[i] = int(grades_up[i])
        grades_up[i] = grades_up[i] + 1
    except:
        grades_up[i] = 'grade up'
        # not every field in the grade column has the grade introduced




if __name__ == '__main__':
    """the message itself"""
    while True:
        filename = 'message.txt'
        try:
            with open(filename, 'r') as fopen:
                message = fopen.read()
            break
        except FileNotFoundError:
            print('File not found. Try again ;) ')
        break

try:
    for name, task, grade, grade_up in zip(names, tasks, grades, grades_up):
        print(message.format(name, task, grade, grade_up, due_date))
except NameError:
    print('Message not found. Try again ;) ')
