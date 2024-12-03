import sys

import Tests.run_tests
from Business.ServiceGrade import ServiceGrade
from Business.Services import ServiceStudents, ServiceDiscipline
from Infrastructure.Repostory_Discipline import repostory_discipline
from Infrastructure.Repostory_Grade import repostory_grade
from Infrastructure.Repostory_Student import repostory_students
from Infrastructure.file_repo_discipline import DisciplineRepoFile
from Infrastructure.file_repo_grade import GradeRepoFile
from Infrastructure.file_repo_students import StudentRepoFile

from UI.Ui import Interface
from Validation.Validators import Validator



validator = Validator()

students_file = "students.txt"
discipline_file = "disciplines.txt"
grade_file = "grades.txt"




stud_rep = StudentRepoFile(students_file)
dis_rep = DisciplineRepoFile(discipline_file)
grade_rep = GradeRepoFile(grade_file)

# stud_rep = repostory_students()
# dis_rep = repostory_discipline()
# grade_rep = repostory_grade()

stud_srv = ServiceStudents(validator, stud_rep)
dis_srv = ServiceDiscipline(validator, dis_rep)
grade_srv = ServiceGrade(validator, stud_rep, dis_rep, grade_rep)
menu = Interface(stud_srv, dis_srv, grade_srv)

if len(sys.argv) == 1:
    menu.run()
else:
    sys.argv = [sys.argv[0]]
    Tests.run_entities_tests.run_tests()
