# Write a function that accepts a dictionary(one argument)
# return the name of the course the student scored worst on
def worst_course(d):
    new_key = ""
    low_val = 100
    for key, value in studentGrades.items():
        if value < low_val:
            low_val = value
            new_key = key
    return new_key


# Write a function that takes the same student info as an argument(one argument)
# return the average grade of the students's courses
def average_grade(d):
    total_grade = 0
    num_courses = len(d)
    for value in d.values():
        total_grade += value
    avg_grade = total_grade / num_courses
    return avg_grade


# define a function with one argument
# base on the grading standard of gpa4, convert the score into a grade (A,B,C,D) for each courses
# A: 100-90 B: 89-80 C: 79-70 D:69-66 F: below 65
def grade_to_letter(number):
    if number >= 97:
        return "A+"
    elif number in range(93, 97):
        return "A"
    elif number in range(90, 93):
        return "A-"
    elif number in range(87, 90):
        return "B+"
    elif number in range(83, 87):
        return "B"
    elif number in range(80, 83):
        return "B-"
    elif number in range(77, 80):
        return "C+"
    elif number in range(73, 77):
        return "C"
    elif number in range(70, 73):
        return "C-"
    elif number in range(67, 70):
        return "D+"
    elif number in range(65, 67):
        return "D"
    else:
        return "F"


# write a function called "get_letter_grades(d)" that takes one argument(the dictionary of grades - the same one as before
# and returns a new dictionary. The result dictionary should have course names as keys & letters as values
# make sure to use the function you just made"letter_grade(number)" inside this new function - it will make your job much easier.
# for example if the input dictionary was{'math':85} then the output should be {'math':'B'}
def grades_to_letters(grades_dictionary):
    new_dic = {}  # Put new values into the dictionary
    for key, value in grades_dictionary.items():
        new_dic[key] = grade_to_letter(value)
    return new_dic


# create a function that takes one argument(a letter grade) and returns a number grade on the 4.0 scale
# example: 3.0 < letter_to_4_0('B)
def letter_to_4_0(letter):
    letter_grade_dic = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
                        'D+': 1.3, 'D': 1.0, 'F': 0.0}
    # for key, value in letter_grade_dic.items():
    #     if letter == key:
    #         return value
    # return
    return letter_grade_dic[letter]


# write a function, takes in a dictionary, input value = letter grade
# output is a new dictionary, value = 4.0 SCALE
def letters_to_4_dic(four_scale_dictionary):
    new_dic = {}
    for key, value in four_scale_dictionary.items():
        new_dic[key] = letter_to_4_0(value)
    return new_dic


# Write a function called calculate_gpa() that takes in one argument (a dict of grades (out of 100))
# and returns one number representing the GPA on a 4.0 scale.
# for example, if the input is:
# {'science': 100,
#  'math': 85}
# output should be: 3.5
def calculate_gap(grade_dictionary):
    # 1. grades to letters
    letter_dic = grades_to_letters(grade_dictionary)
    # 2. letters to 4.0
    converted_4_dic = letters_to_4_dic(letter_dic)
    # 3. get the average grade
    avg_g = average_grade(converted_4_dic)
    avg_g = round(avg_g, 2)
    return avg_g


# Write a Class
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def favorite_class(self):
        best_course = 0
        b_c_name = ""
        for key, value in self.grades.items():
            if value > best_course:
                best_course = value
                b_c_name = key
        return b_c_name

    def least_favorite_class(self):
        return worst_course(self.grades)

    def calculate_gpa(self):
        return calculate_gap(self.grades)

    def classes(self):
        return list(self.grades.keys())

    def print_student_info(self):
        print("--------------------------------------------------------------------------------")
        print(self.name + " final grades report: ")
        print("Favorite class is: " + self.favorite_class())
        print("Has to improve in: " + self.least_favorite_class())
        print("Final GPA(4.0 Scale): " + str(self.calculate_gpa()))


###############################################################################
# Program starts here
###############################################################################


studentGrades = {
    'Physics': 82,
    'Calculus 1': 65,
    'history': 75,
    'Algebra 2': 80,
    'Earth Science': 94,
    'English': 87,
    'Physical Edu': 96,
    'Biology': 73,
    'European History': 98,
    'Social Studies': 89,
    'Chemistry': 81
}
studentGrades2 = {
    'Physics': 85,
    'Calculus 1': 65,
    'history': 95,
    'Algebra 2': 88,
    'Earth Science': 94,
    'English': 87,
    'Physical Edu': 96,
    'Biology': 73,
    'European History': 78,
    'Social Studies': 69,
    'Chemistry': 89
}

student1 = Student("Jack", studentGrades)
student2 = Student("Huining", studentGrades2)
students = [student1, student2]

print("--------------------------------------------------------------------------------")
print("I'm a teacher and my students are:")
for student in students:
    print("      " + str(student.name))
print("School curriculum: ")
print(student.classes())

for student in students:
    student.print_student_info()
