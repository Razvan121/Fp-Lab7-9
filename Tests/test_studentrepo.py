import unittest

from Domain.Student import Student

from Infrastructure.Repostory_Student import repostory_students


class TestStudentRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = repostory_students()


    def test_add_student(self):
        student1 = Student(10,"Ion A")
        student2 = Student(15,"Ion B")
        self.__repo.add_student(student1)
        self.__repo.add_student(student2)
        self.assertEqual(self.__repo.get_len_student(),2)

    def test_get_student(self):
        student1 = Student(10,"Ion A")
        student2 = Student(15,"Ion B")
        self.__repo.add_student(student1)
        self.__repo.add_student(student2)
        students = self.__repo.get_all_students()
        self.assertEqual(students[0],student1)
        self.assertEqual(students[1],student2)
        self.assertEqual(self.__repo.get_len_student(),2)

    def test_remove_student(self):
        student1 = Student(10,"Ion A")
        student2 = Student(15,"Ion B")
        self.__repo.add_student(student1)
        self.__repo.add_student(student2)
        self.__repo.delete_student(10)
        students = self.__repo.get_all_students()
        self.assertEqual(self.__repo.get_len_student(),1)
        self.assertEqual(students[0],student2)


    def test_search_student(self):
        student1 = Student(10,"Ion A")
        self.__repo.add_student(student1)
        studentSearch = self.__repo.search_student_by_ID(10)
        assert studentSearch == student1

    def test_modify_student(self):
        student1 = Student(10,"Ion A")
        self.__repo.add_student(student1)
        self.__repo.modify_student(10,"Erika Nicoleta")
        self.assertEqual(student1.get_name(), "Erika Nicoleta")

    def run_all_tests(self):
        unittest.main()