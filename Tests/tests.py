from Business.ServiceGrade import ServiceGrade
from Business.Services import ServiceStudents
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

def test_create_grade():

    student = Student("1","Ana Maria")
    discipline = Discipline("1","Fizica","Lionel Messi")

    validator = Validator()

    validator.validate_student(student)
    validator.validate_discipline(discipline)


    grade = Grade(10,student,discipline)
    assert grade.get_grade() == 10
    assert grade.get_name_discipline() == "Fizica"
    assert grade.get_name_student() == "Ana Maria"
    print("Grade created successfully")

def test_assign_grade():
    student = Student("1","Ana Maria")
    repo_stud = repostory_students()
    repo_stud.add_student(student)

    discipline = Discipline("1","Fizica","Lionel Messi")
    repo_discipline = repostory_discipline()
    repo_discipline.add_discipline(discipline)

    grade = Grade(10,student,discipline)
    assert grade.get_grade() == 10
    assert grade.get_name_discipline() == "Fizica"
    assert grade.get_name_student() == "Ana Maria"

def test_random():
    repo_stud = repostory_students()
    validator = Validator()
    stud_srv = ServiceStudents(validator, repo_stud)
    # student = stud_srv.student_random()
    nr = 5
    stud_srv.student_random(nr)

    assert len(repo_stud.get_all_students()) == nr

def test_sort_list():

    repo_stud = repostory_students()
    validator = Validator()

    stud_srv = ServiceStudents(validator, repo_stud)

    student1 = Student("1","Ana Maria")
    repo_stud.add_student(student1)

    student2 = Student("2","Mihai Gabriel")
    repo_stud.add_student(student2)
    student3 = Student("3","Ion Gabriel")
    repo_stud.add_student(student3)

    discipline = Discipline("1","Fizica","Lionel Messi")

    repo_discipline = repostory_discipline()
    repo_discipline.add_discipline(discipline)
    repo_grade = repostory_grade()

    grade = Grade(6,student1,discipline)

    repo_grade.add_grade(grade)

    grade_1 = Grade(7,student1,discipline)

    repo_grade.add_grade(grade_1)

    grade1 = Grade(10,student2,discipline)
    repo_grade.add_grade(grade1)

    grade2 = Grade(10,student3,discipline)
    repo_grade.add_grade(grade2)

    grade_srv = ServiceGrade(validator,repo_stud,repo_discipline,repo_grade)

    id_discipline = discipline.get_id()

    lst_sorted = grade_srv.get_sorted_students_with_grades(id_discipline)
    assert lst_sorted[0][0].get_name() == "Ana Maria"
    assert lst_sorted[1][0].get_name() == "Ion Gabriel"
    assert lst_sorted[2][0].get_name() == "Mihai Gabriel"



def test_get_average_grade_for_student():
    student = Student("1","Ana Maria")
    repo_stud = repostory_students()
    repo_stud.add_student(student)

    discipline = Discipline("1","Fizica","Lionel Messi")
    repo_discipline = repostory_discipline()
    repo_discipline.add_discipline(discipline)

    discipline2 = Discipline("2","Matematica","Ion Gabriel")
    repo_discipline.add_discipline(discipline2)

    grade = Grade(6,student,discipline)
    repo_grade = repostory_grade()
    repo_grade.add_grade(grade)

    grade1 = Grade(7,student,discipline2)
    repo_grade.add_grade(grade1)

    grade2 = Grade(10,student,discipline)
    repo_grade.add_grade(grade2)

    grade_srv = ServiceGrade(Validator(),repo_stud,repo_discipline,repo_grade)

    id_student = student.get_id()

    average = grade_srv.get_average_grade_for_student(id_student)
    assert average == 7.67
    print("Average grade for student successfully")


def test_sort_grades_by_student():
    student = Student("1","Ana Maria")
    repo_stud = repostory_students()
    repo_stud.add_student(student)

    student1 = Student("2","Mihai Gabriel")
    repo_stud.add_student(student1)

    student2 = Student("3","Ion Gabriel")
    repo_stud.add_student(student2)

    discipline = Discipline("1","Fizica","Lionel Messi")
    repo_discipline = repostory_discipline()
    repo_discipline.add_discipline(discipline)

    discipline2 = Discipline("2","Matematica","Ion Gabriel")
    repo_discipline.add_discipline(discipline2)

    grade = Grade(6,student,discipline)
    repo_grade = repostory_grade()
    repo_grade.add_grade(grade)

    grade1 = Grade(7,student,discipline2)
    repo_grade.add_grade(grade1)

    grade2 = Grade(10,student,discipline)
    repo_grade.add_grade(grade2)

    grade3 = Grade(8,student1,discipline)
    repo_grade.add_grade(grade3)

    grade4 = Grade(5,student2,discipline)
    repo_grade.add_grade(grade4)

    grade_srv = ServiceGrade(Validator(),repo_stud,repo_discipline,repo_grade)

    lst = grade_srv.sort_grades_by_student()

    assert lst[0][1] == 8.0
    assert len(lst) == 1
    print("Sort grades by student successfully")


def test_grades_under_five():
    student = Student("1", "Ana Maria")
    repo_stud = repostory_students()
    repo_stud.add_student(student)

    student1 = Student("2", "Mihai Gabriel")
    repo_stud.add_student(student1)

    student2 = Student("3", "Ion Gabriel")
    repo_stud.add_student(student2)

    discipline = Discipline("1", "Fizica", "Lionel Messi")
    repo_discipline = repostory_discipline()
    repo_discipline.add_discipline(discipline)

    discipline2 = Discipline("2", "Matematica", "Ion Gabriel")
    repo_discipline.add_discipline(discipline2)

    grade = Grade(5, student, discipline)
    repo_grade = repostory_grade()
    repo_grade.add_grade(grade)

    grade1 = Grade(4, student, discipline2)
    repo_grade.add_grade(grade1)

    grade2 = Grade(5, student, discipline)
    repo_grade.add_grade(grade2)

    grade3 = Grade(8, student1, discipline)
    repo_grade.add_grade(grade3)

    grade4 = Grade(5, student2, discipline)
    repo_grade.add_grade(grade4)

    grade_srv = ServiceGrade(Validator(), repo_stud, repo_discipline, repo_grade)

    lst = grade_srv.grades_under_five()

    assert lst[0][1] == 4.67
    assert lst[0][0].get_name() == "Ana Maria"
    assert lst[1][1] == 5
    assert lst[1][0].get_name() == "Ion Gabriel"
    assert len(lst) == 2

    print("Grades under five successfully")





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
    test_create_grade()
    test_assign_grade()
    test_random()
    test_sort_list()
    test_get_average_grade_for_student()
    test_sort_grades_by_student()
    test_grades_under_five()

run_all_tests()