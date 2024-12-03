import unittest

from Domain.Discipline import Discipline
from Domain.Grade import Grade
from Domain.GradeDto import GradeDto
from Domain.Student import Student
from Main.main import discipline_file


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(1,"Razvan Chelariu")

    def test_get_id_student(self):
        self.assertEqual(self.student.get_id(),1)
    def test_get_name_student(self):
        self.assertEqual(self.student.get_name(),"Razvan Chelariu")

    def test_set_name(self):
        self.student.set_name("Erika Nicoleta")
        self.assertEqual(self.student.get_name(),"Erika Nicoleta")

class TestDiscipline(unittest.TestCase):
    def setUp(self):
        self.discipline = Discipline(1,"Mathematics","Ion Gabriel")

    def test_get_id_discipline(self):
        self.assertEqual(self.discipline.get_id(),1)
    def test_get_name_discipline(self):
        self.assertEqual(self.discipline.get_name(),"Mathematics")
    def test_get_teacher(self):
        self.assertEqual(self.discipline.get_teacher(),"Ion Gabriel")
    def test_set_teacher(self):
        self.discipline.set_teacher("Erika Nicoleta")
        self.assertEqual(self.discipline.get_teacher(),"Erika Nicoleta")

    def test_set_name_discipline(self):
        self.discipline.set_name("English")
        self.assertEqual(self.discipline.get_name(),"English")

class TestGrade(unittest.TestCase):
    def setUp(self):
        student = Student(1,"Razvan Chelariu")
        discipline = Discipline(1,"Mathematics","Ion Gabriel")
        self.grade = Grade(10,student,discipline)


    def test_get_id_student(self):
        self.assertEqual(self.grade.get_id_student(),1)
    def test_get_name_student(self):
        self.assertEqual(self.grade.get_name_student(),"Razvan Chelariu")

    def test_get_id_discipline(self):
        self.assertEqual(self.grade.get_id_discipline(),1)
    def test_get_name_discipline(self):
        self.assertEqual(self.grade.get_name_discipline(),"Mathematics")
    def test_get_teacher(self):
        self.assertEqual(self.grade.get_teacher_discipline(), "Ion Gabriel")


    def test_set_grade(self):
        self.grade.set_grade(7)
        self.assertEqual(self.grade.get_grade(),7)


class TestGradeDTO(unittest.TestCase):
    def setUp(self):
        self.grade = GradeDto(8,1,1)

    def test_get_id_student(self):
        self.assertEqual(self.grade.get_id_student(),1)
    def test_get_id_discipline(self):
        self.assertEqual(self.grade.get_id_discipline(),1)
    def test_get_grade_(self):
        self.assertEqual(self.grade.get_grade(),8)










