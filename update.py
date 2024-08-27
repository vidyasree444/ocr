'''Given the names and grades for each student in a class of  students, store them in a nested list
and print the name(s) of any student(s) having the second lowest grade.Note: If there are multiple
students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''

n=int(input("number of students"))
l=[]
for i in range(n):
    name=input("enter name")
    score=input('enter score')
    l.append([name,score])

print(l)
grades = [score for name, score in l]
unique_grades = sorted(set(grades))

second_lowest_grade = unique_grades[1]

names_with_second_lowest = [name for name, score in l if score == second_lowest_grade]

sorted_names = sorted(names_with_second_lowest)

for name in sorted_names:
    print(name)