import unittest

from Domain.Discipline import Discipline
from Domain.Grade import Grade
from Domain.Student import Student
from Infrastructure.Repostory_Grade import repostory_grade


class TestGradeRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = repostory_grade()

    def test_add_grade(self):
        student1 = Student(10, "Ion A")
        discipline1 = Discipline(1, "Math", "Ion Gabriel")
        grade = Grade(10,student1,discipline1)
        self.__repo.add_grade(grade)
        self.assertEqual(len(self.__repo.get_all_grades()),1)

    def test_delete_grade(self):
        student1 = Student(10, "Ion A")
        discipline1 = Discipline(1, "Math", "Ion Gabriel")
        grade = Grade(10,student1,discipline1)
        self.__repo.add_grade(grade)
        self.assertEqual(len(self.__repo.get_all_grades()),1)