from Business.ServiceGrade import ServiceGrade
from Domain.Discipline import Discipline
from Domain.Grade import Grade
from Domain.Student import Student
from Infrastructure.Repostory_Discipline import repostory_discipline
from Infrastructure.Repostory_Grade import repostory_grade
from Infrastructure.Repostory_Student import repostory_students
from Validation.Validators import Validator


def test_Create_Student():
    student = Student("1","Ana Maria")

    assert student.get_id() == "1"
    assert student.get_name() == "Ana Maria"
    print("Student created successfully")

def test_Create_Discipline():
    discipline = Discipline("1","Matematica","Ion Gabriel")
    assert discipline.get_id() == "1"
    assert discipline.get_name() == "Matematica"
    assert discipline.get_teacher() == "Ion Gabriel"
    print("Discipline created successfully")



def test_Validator():
    validator = Validator()

    student = Student("1","Ana Maria")
    discipline = Discipline("1","Matematica","Ion Gabriel")

    try:
        validator.validate_student(student)
        validator.validate_discipline(discipline)
        print("Validation passed")
    except ValueError:
        print("Validation failed")
        assert False



def test_add_student():
    validator = Validator()
    student = Student("1","Ana Maria")
    validator.validate_student(student)
    repo = repostory_students()
    repo.add_student(student)


    assert repo.get_all_students()[0].get_name() == "Ana Maria"


    student2 = Student("2","Mihai Gabriel")
    validator.validate_student(student2)
    repo.add_student(student2)
    #
    # students = repo.get_all_students()

    assert repo.get_all_students()[1].get_name() == "Mihai Gabriel"

    # assert students["2"].get_name() == "Mihai Gabriel"

    print("Students added successfully")


def test_delete_student():

    student = Student("1","Ana Maria")
    repo = repostory_students()
    repo.add_student(student)

    student2 = Student("2","Mihai Gabriel")
    repo.add_student(student2)

    repo.delete_student("1")
    # assert len(repo.get_all_students()) == 1
    assert repo.get_all_students()[0].get_name() == "Mihai Gabriel"
    print("Student deleted successfully")


def test_modify_student():
    student = Student("1","Ana Maria")
    repo = repostory_students()
    repo.add_student(student)

    repo.modify_student("1","Mihai Gabriel")
    students = repo.get_all_students()

    assert repo.get_all_students()[0].get_name() == "Mihai Gabriel"
    # assert students["1"].get_name() == "Mihai Gabriel"
    print("Student modified successfully")




def test_add_discipline():
    discipline = Discipline("1","Matematica","Ion Gabriel")
    repo = repostory_discipline()
    repo.add_discipline(discipline)

    discipline2 = Discipline("2","Fizica","Lionel Messi")
    repo.add_discipline(discipline2)

    # assert repo.get_all_disciplines()[0].get_name() == "Matematica"
    # assert repo.get_all_disciplines()[0].get_teacher() == "Ion Gabriel"
    # assert repo.get_all_disciplines()[1].get_name() == "Fizica"
    # assert repo.get_all_disciplines()[1].get_teacher() == "Lionel Messi"

    all_disciplines  = repo.get_all_disciplines()

    assert all_disciplines["1"].get_name() == "Matematica"
    assert all_disciplines["2"].get_name() == "Fizica"

    print("Disciplines added successfully")


def test_delete_discipline():
    discipline = Discipline("1","Matematica","Ion Gabriel")
    repo = repostory_discipline()
    repo.add_discipline(discipline)

    discipline2 = Discipline("2","Fizica","Lionel Messi")
    repo.add_discipline(discipline2)

    repo.delete_discipline("1")
    assert len(repo.get_all_disciplines()) == 1
    # assert repo.get_all_disciplines().get_name() == "Fizica"
    print("Discipline deleted successfully")

def test_modify_discipline():
    discipline = Discipline("1","Matematica","Ion Gabriel")
    repo = repostory_discipline()
    repo.add_discipline(discipline)

    repo.modify_discipline_name("1","Fizica")
    disciplines = repo.get_all_disciplines()
    # assert repo.get_all_disciplines().get_name() == "Fizica"

    assert disciplines["1"].get_name()=="Fizica"
    print("Discipline modified successfully")


def test_search_student_by_id():
    student = Student("1","Ana Maria")
    repo = repostory_students()
    repo.add_student(student)

    studentsearch = repo.search_student_by_ID("1")

    assert studentsearch.get_name() == "Ana Maria"
    print("Student searching successfully")


def test_search_discipline_by_id():
    discipline = Discipline("1","Fizica","Lionel Messi")
    repo = repostory_discipline()
    repo.add_discipline(discipline)

    disciplinesearch = repo.search_discipline_by_ID("1")
    assert disciplinesearch.get_name() == "Fizica"
    print("Discipline searching successfully")

def test_assign_grade():
    student = Student("1","Ana Maria")
    repo_stud = repostory_students()
    repo_stud.add_student(student)

    discipline = Discipline("1","Fizica","Lionel Messi")
    repo_discipline = repostory_discipline()
    repo_discipline.add_discipline(discipline)

    grade = Grade(10,student,discipline)
    repo_grade = repostory_grade()
    repo_grade.add_grade(grade)

    assert repo_grade.get_all_grades()[0].get_grade() == 10
    assert repo_grade.get_all_grades()[0].get_student().get_name() == "Ana Maria"



def run_all_tests():
    test_Create_Student()
    test_Create_Discipline()
    test_Validator()
    test_add_student()
    test_delete_student()
    test_add_discipline()
    test_delete_discipline()
    test_modify_student()
    test_modify_discipline()
    test_search_student_by_id()
    test_search_discipline_by_id()
    test_assign_grade()

run_all_tests()