from collections import defaultdict

from Domain.Grade import Grade


class ServiceGrade:
    def __init__(self, validator, stud_repo, dis_repo, grade_repo, stud_srv, dis_srv):
        """
        :param validator: An instance responsible for validating the business rules.
        :type validator: Validator

        :param stud_repo: Repository for storing and managing student data.
        :type stud_repo: StudentRepository

        :param dis_repo: Repository for storing and managing discipline data.
        :type dis_repo: DisciplineRepository

        :param grade_repo: Repository for storing and managing grade data.
        :type grade_repo: GradeRepository

        :param stud_srv: Service layer for handling student-related operations.
        :type stud_srv: StudentService

        :param dis_srv: Service layer for handling discipline-related operations.
        :type dis_srv: DisciplineService
        """
        self.__validator = validator
        self.__stud_repo = stud_repo
        self.__dis_repo = dis_repo
        self.__grade_repo = grade_repo
        self.__stud_srv = stud_srv
        self.__dis_srv = dis_srv

    def add_gradesrv(self, id_student, id_discipline, value):
        """

        :param id_student: The unique id of the student.
        :param id_discipline: The unique id of the discipline.
        :param value: The grade.
        :return:
        """
        student = self.__stud_srv.search_student(id_student)
        if student is None:
            raise ValueError(f"Student with ID {id_student} not found")
        discipline = self.__dis_srv.search_discipline(id_discipline)
        if discipline is None:
            raise ValueError(f"Discipline with ID {id_discipline} not found")
        self.__validator.validate_student(student)
        self.__validator.validate_discipline(discipline)
        grade = Grade(value, student, discipline)
        self.__grade_repo.add_grade(grade)
        return grade

    def get_all_gradesrv(self):

        return self.__grade_repo.get_all_grades()

