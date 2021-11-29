student1 = input("Student 1 (courses 1-4): ")
student2 = input("Student 2 (courses 1-4): ")
student3 = input("Student 3 (courses 1-4): ")
student4 = input("Student 4 (courses 1-4): ")
student5 = input("Student 5 (courses 1-4): ")


def studentaverage(studentgrades):
    gradestudents = studentgrades.split()
    gradessum = 0

    for i in range (len(gradestudents)):
        grade = int(gradestudents[i])
        gradessum = gradessum + grade

    averagegrade = gradessum /4
    return averagegrade

def courseaverage(coursegrades1,coursegrades2,coursegrades3,coursegrades4,coursegrades5,courseno):
    gradescourses1 = coursegrades1.split()
    gradescourses2 = coursegrades2.split()
    gradescourses3 = coursegrades3.split()
    gradescourses4 = coursegrades4.split()
    gradescourses5 = coursegrades5.split()

    coursegradessum = int(gradescourses1[courseno]) + int(gradescourses2[courseno]) + int(gradescourses3[courseno]) + int(gradescourses4[courseno]) + int(gradescourses5[courseno])
    averagecoursegrade = coursegradessum/5
    return averagecoursegrade

students = [studentaverage(student1),studentaverage(student2),studentaverage(student3),studentaverage(student4),studentaverage(student5)]
students.sort(reverse=True)
print("The highest average mark of students: ", students[0])

course1 = courseaverage(student1,student2,student3,student4,student5,0)
course2 = courseaverage(student1,student2,student3,student4,student5,1)
course3 = courseaverage(student1,student2,student3,student4,student5,2)
course4 = courseaverage(student1,student2,student3,student4,student5,3)
courses = [course1, course2, course3, course4]
courses.sort(reverse=True)
print("The highest average mark of courses: ", courses[0])
