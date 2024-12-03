import unittest

from Business.ServiceGrade import ServiceGrade
from Business.Services import ServiceStudents, ServiceDiscipline
from Domain.Discipline import Discipline
from Domain.Grade import Grade
from Domain.GradeDto import GradeDto
from Domain.Student import Student
from Infrastructure.Repostory_Discipline import repostory_discipline
from Infrastructure.Repostory_Grade import repostory_grade
from Infrastructure.Repostory_Student import repostory_students
from Validation.Validators import Validator


class TestGradeService(unittest.TestCase):
    def setUp(self) ->None:
        valid = Validator()
        repo_stude = repostory_students()
        repo_grade = repostory_grade()
        repo_dis = repostory_discipline()
        self.__grades = ServiceGrade(valid, repo_stude, repo_dis, repo_grade)
        self.__student_srv = ServiceStudents(valid, repo_stude)
        self.__discipline_srv = ServiceDiscipline(valid, repo_dis)

        self.student1 = Student(1,"Ana Maria")
        self.student2 = Student(2,"Mihai Gabriel")
        self.student3 = Student(3,"Razvan C")
        repo_stude.add_student(self.student1)
        repo_stude.add_student(self.student2)
        repo_stude.add_student(self.student3)


        self.discipline1 = Discipline(1,"Math","A B")
        self.discipline2 = Discipline(2,"English","C D")
        repo_dis.add_discipline(self.discipline1)
        repo_dis.add_discipline(self.discipline2)



    def test_get_trade(self):
        self.__grades.add_gradesrv(1,1,10)
        self.__grades.add_gradesrv(2,1,20)
        grades = self.__grades.get_all_gradesrv()
        actual_grade = Grade(10, self.student1, self.discipline1)
        self.assertEqual(str(grades[1][1][0]), str(actual_grade))
        actual_grade = Grade(20, self.student2, self.discipline1)
        self.assertEqual(str(grades[2][1][0]), str(actual_grade))

    def test_add_grade(self):
        self.__grades.add_gradesrv(1,1,10)
        self.__grades.add_gradesrv(2,1,20)
        grades = self.__grades.get_all_gradesrv()
        self.assertTrue(len(grades) == 2)

    def test_sorted_students_with_grades(self):
        self.__grades.add_gradesrv(1,1,8)
        self.__grades.add_gradesrv(2,1,9)
        self.__grades.add_gradesrv(1,1,10)

        sorted_list = self.__grades.get_sorted_students_with_grades(1)

        self.assertEqual(len(sorted_list), 3)
        self.assertEqual(sorted_list[0][0].get_name(), "Ana Maria")  # First student by name
        self.assertEqual(sorted_list[1][0].get_name(), "Mihai Gabriel")

        self.assertEqual(sorted_list[0][1][0].get_grade(), 10)  # Highest grade for Ana Maria
        self.assertEqual(sorted_list[0][1][1].get_grade(), 8)

    def test_average_grade_for_student(self):
        self.__grades.add_gradesrv(1, 1, 8)
        self.__grades.add_gradesrv(1, 1, 9)
        self.__grades.add_gradesrv(1, 1, 10)

        avg_grade = self.__grades.get_average_grade_for_student(1)
        self.assertAlmostEqual(avg_grade, 9.0, places=2)  # (8 + 9 + 10) / 3 = 9.0

        # Test student with no grades
        avg_grade = self.__grades.get_average_grade_for_student(3)
        self.assertEqual(avg_grade, 0.0)

    def test_sort_grades_by_student(self):
        """
        Test the method that retrieves the top 20% students with the highest average grades.
        """
        # Add grades for students
        self.__grades.add_gradesrv(1, 1, 9)  # Ana Maria, Math
        self.__grades.add_gradesrv(1, 2, 8)  # Ana Maria, English
        self.__grades.add_gradesrv(2, 1, 10)  # Mihai Gabriel, Math
        self.__grades.add_gradesrv(2, 2, 6)  # Mihai Gabriel, English
        self.__grades.add_gradesrv(3, 1, 4)  # Razvan C, Math
        self.__grades.add_gradesrv(3, 2, 5)  # Razvan C, English

        # Call the method to get the top 20%
        sorted_students = self.__grades.sort_grades_by_student()

        # Debugging
        print("Sorted Students with Average Grades:", sorted_students)

        # Verify that only the top student is returned (top 20% of 3 students = 1 student)
        self.assertEqual(len(sorted_students), 1)

        # Verify the correct student is returned
        self.assertEqual(sorted_students[0][0].get_name(), "Ana Maria")  # Top student
        self.assertAlmostEqual(sorted_students[0][1], 8.5, places=2)  # Average (10+6)/2 = 8.0

    def test_grades_under_five(self):
        """
        Test the method that retrieves students with average grades under 5.
        """
        # Add grades for students
        self.__grades.add_gradesrv(1, 1, 9)  # Ana Maria, Math
        self.__grades.add_gradesrv(1, 2, 8)  # Ana Maria, English
        self.__grades.add_gradesrv(2, 1, 10)  # Mihai Gabriel, Math
        self.__grades.add_gradesrv(2, 2, 6)  # Mihai Gabriel, English
        self.__grades.add_gradesrv(3, 1, 4)  # Razvan C, Math
        self.__grades.add_gradesrv(3, 2, 5)  # Razvan C, English
        self.__grades.add_gradesrv(3, 2, 3)  # Razvan C, English (additional grade)

        # Call the method to get students with grades under five
        under_five = self.__grades.grades_under_five()

        # Debugging
        print("Students with Grades Under 5:", under_five)

        # Verify only one student is returned
        self.assertEqual(len(under_five), 1)

        # Verify the correct student is returned
        self.assertEqual(under_five[0][0].get_name(), "Razvan C")  # Student under 5
        self.assertAlmostEqual(under_five[0][1], 4.0, places=2)  # Average (4+5+3)/3 = 4.0

    def run_all_tests(self):
        unittest.main()