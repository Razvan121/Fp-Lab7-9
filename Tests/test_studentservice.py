import unittest

from Business.Services import ServiceStudents
from Domain.Student import Student
from Exceptions.Exceptions import SerivceException
from Infrastructure.Repostory_Student import repostory_students

from Validation.Validators import Validator


class TestStudentService(unittest.TestCase):
    def setUp(self) -> None:
        repo = repostory_students()
        validator = Validator()
        self.__student_service = ServiceStudents(validator, repo)

    def test_get_students(self):
        self.__student_service.addstudent(1,"Ana Maria")
        students = self.__student_service.get_all_students()
        self.assertTrue(len(students) == 1)
        expectedstudent = Student(1,"Ana Maria")
        self.assertEqual(students[0], expectedstudent)

    def test_add_student(self):
        self.__student_service.addstudent(1,"Ana Maria")
        students = self.__student_service.get_all_students()
        self.assertTrue(len(students) == 1)
        self.assertRaises(SerivceException,self.__student_service.addstudent,-1,"Ana Maria")
        self.assertRaises(SerivceException,self.__student_service.addstudent,1,"Ana ")

    def test_delete_student(self):
        self.__student_service.addstudent(1,"Ana Maria")
        students = self.__student_service.get_all_students()
        self.__student_service.delete_student(1)
        self.assertTrue(len(students) == 0)

    def search_student(self):
        self.__student_service.addstudent(1,"Ana Maria")
        student = self.__student_service.search_student(1)
        self.assertEqual(student, Student(1,"Ana Maria"))


    def test_modify_student(self):
        self.__student_service.addstudent(1,"Ana Maria")
        self.__student_service.modify_student(1,"Razvan Chelariu")
        students = self.__student_service.get_all_students()
        expectedstudent = Student(1,"Razvan Chelariu")

        self.assertEqual(students[0], expectedstudent)






    def run_all_tests(self):
        unittest.main()

