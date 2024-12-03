import unittest

from Domain.Discipline import Discipline
from Domain.Student import Student
from Exceptions.Exceptions import ValidatorException
from Validation.Validators import Validator


class TestStudentValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = Validator()

    def test_valid(self):
        student = Student(1,"Ana Maria")
        self.__validator.validate_student(student)
        student2 = Student(-1,"Ana Maria")
        self.assertRaises(ValidatorException,self.__validator.validate_student,student2)
        student3 = Student(1,"Ana ")
        self.assertRaises(ValidatorException,self.__validator.validate_student,student3)

    def run_all_tests(self):
        unittest.main()

class TestDiscipline(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = Validator()

    def test_valid(self):
        discipline = Discipline(1,"math","Ana Maria")
        self.__validator.validate_discipline(discipline)
        discipline2 = Discipline(-1,"math","Ana Maria")
        self.assertRaises(ValidatorException,self.__validator.validate_discipline,discipline2)
        discipline3 = Discipline(2,"","Ana Maria")
        self.assertRaises(ValidatorException,self.__validator.validate_discipline,discipline3)


    def run_all_tests(self):
        unittest.main()

