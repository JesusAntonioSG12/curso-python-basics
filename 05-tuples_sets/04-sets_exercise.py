python_course = {'Ana', 'Luis', 'María', 'Pedro'}
java_course = {'Pepito', 'Pedro', 'Carlos', 'Ricardo'}

two_course = python_course.intersection(java_course)

only_python = python_course.difference(java_course)

all_students = python_course.union(java_course)
print(all_students)