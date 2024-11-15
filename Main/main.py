from Business.ServiceGrade import ServiceGrade
from Business.Services import ServiceStudents, ServiceDiscipline
from Infrastructure.Repostory_Discipline import repostory_discipline
from Infrastructure.Repostory_Grade import repostory_grade
from Infrastructure.Repostory_Student import repostory_students
from Tests.tests import run_all_tests
from UI.Ui import Interface
from Validation.Validators import Validator

validator = Validator()
stud_rep = repostory_students()
dis_rep = repostory_discipline()
grade_rep = repostory_grade()

stud_srv = ServiceStudents(validator, stud_rep)
dis_srv = ServiceDiscipline(validator, dis_rep)
grade_srv = ServiceGrade(validator, stud_rep, dis_rep, grade_rep, stud_srv, dis_srv)
menu = Interface(stud_srv, dis_srv, grade_srv)

run_all_tests()
menu.run()
