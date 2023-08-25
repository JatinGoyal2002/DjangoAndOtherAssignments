


import functools
students = [
	{'name': 'Aman', 'marks': 97},
	{'name': 'Kiran', 'marks': 79},
	{'name': 'Akansha', 'marks': 93},
	{'name': 'Nupur', 'marks': 69},
	{'name': 'Paul', 'marks': 36},
]

def atleastOneStudentPassed(students):
    for student in students:
        if student['marks'] >= 80:
            return True
    return False

def lessThan7Characters(students):
    for student in students:
        if len(student['name']) >= 7:
            return False
    return True

print("whether atleast one student have marks greater than 80, ", atleastOneStudentPassed(students))
print("whether all names have length less than 7, ", lessThan7Characters(students))


# atleast_one_student_passed = functools.reduce(lambda x, y : x or y, list(map(lambda x : x['marks'] >= 80, students)))
# less_than_seven_character = functools.reduce(lambda x, y : x and y, list(map(lambda x : len(x['name']) < 7, students)))
# print("whether atleast one student have marks greater than 80, " ,atleast_one_student_passed)
# print("whether all names have length less than 7, ", less_than_seven_character)

atleastOneStudentPassed = any(list(map(lambda x : x['marks'] >= 80, students)))
print("whether atleast one student have marks greater than 80 ", atleastOneStudentPassed)
less_than_seven_character = all(list(map(lambda x : len(x['name']) < 7, students)))
print("whether all names have length less than 7, ", less_than_seven_character)
