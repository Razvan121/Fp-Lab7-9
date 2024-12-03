import math

from Domain.Grade import Grade




class ServiceGrade:
    def __init__(self, validator, stud_repo, dis_repo, grade_repo):
        """
        :param validator: An instance responsible for validating the business rules.
        :type validator: Validator

        :param stud_repo: Repository for storing and managing student data.
        :type stud_repo: StudentRepository

        :param dis_repo: Repository for storing and managing discipline data.
        :type dis_repo: DisciplineRepository

        :param grade_repo: Repository for storing and managing grade data.
        :type grade_repo: GradeRepository


        """
        self.__validator = validator
        self.__stud_repo = stud_repo
        self.__dis_repo = dis_repo
        self.__grade_repo = grade_repo

    def add_gradesrv(self, id_student, id_discipline, value):
        """
        Add a grade in list of grades
        :param id_student: The unique id of the student.
        :param id_discipline: The unique id of the discipline.
        :param value: The grade.
        :return:
        """
        student = self.__stud_repo.search_student_by_ID(id_student)
        if student is None:
            raise ValueError(f"Student with ID {id_student} not found")
        discipline = self.__dis_repo.search_discipline_by_ID(id_discipline)
        if discipline is None:
            raise ValueError(f"Discipline with ID {id_discipline} not found")
        self.__validator.validate_student(student)
        self.__validator.validate_discipline(discipline)
        grade = Grade(value, student, discipline)
        self.__grade_repo.add_grade(grade)
        return grade


    def delete_gradesrv(self, id_student,id_discipline,grade_value):
        """
        Delete a grade from list of grades
        :param id_student: The unique id of the student.
        :param id_discipline: The unique id of the discipline.
        :param grade_value: The grade that would be deleted
        :return:
        """
        student = self.__stud_repo.search_student_by_ID(id_student)
        discipline = self.__dis_repo.search_discipline_by_ID(id_discipline)
        grade = Grade(grade_value, student, discipline)
        self.__grade_repo.delete_grade(id_student,id_discipline,grade)


    def get_grades_discipline(self,id_discipline):
        """
        Get a list of sorted grades from a given discipline
        :param id_discipline: The unique id of the discipline.
        :return: a list of sorted grades
        """
        result =  self.__grade_repo.get_grades_for_discipline(id_discipline)
        return sorted(result, key=lambda grade: grade.get_grade(), reverse=True)

    def get_sorted_students_with_grades(self,id_discipline):
        """
        Get a sorted list with all average grades from all discipline
        :param id_discipline: The unique id of the discipline.
        :return: a list o sorted grades by student name
        """
        discipline = self.__dis_repo.search_discipline_by_ID(id_discipline)
        if discipline is None:
            raise ValueError(f"Discipline with ID {id_discipline} not found")

        students = self.__stud_repo.get_all_students()
        sorted_students = sorted(students, key=lambda student: student.get_name())

        sort_grades = []

        for student in sorted_students:
            grades = [
                grade
                for disciplines in self.__grade_repo.get_all_grades().get(student.get_id(), {}).values()
                for grade in disciplines
            ]

            sort_grades.append((student,sorted(grades, key=lambda grade: grade.get_grade(), reverse=True)))

        return sort_grades

    def get_average_grade_for_student(self,id_student):
        """
        Get an average grades for every student
        :param id_student: The unique id of the student.
        :return average_grade: The average grade of the student with 2 decimal

        """

        student = self.__stud_repo.search_student_by_ID(id_student)

        if student is None:
            raise ValueError(f"Student with ID {id_student} not found")

        disciplines = self.__grade_repo.get_all_grades().get(id_student, {})

        average_grade = 0
        grade_count = 0

        for discipline in disciplines.values():
            for grade in discipline:
                average_grade += grade.get_grade()
                grade_count +=1

        if grade_count >0:
            average_grade /= grade_count
        else:
            average_grade = 0


        return round(average_grade,2)


    def sort_grades_by_student(self):
        """
        Get 20% of first students with the highest average grades
        :return: list of sorted grades by student
        """
        
        lst_avg_grades = []
        
        students = self.__stud_repo.get_all_students()
        
        for student in students:
            id_student = student.get_id()
            avg = self.get_average_grade_for_student(id_student)
            
            lst_avg_grades.append((student,avg))

        lst_avg_grades.sort(key=lambda x: x[1], reverse=True)
        cutoff = math.ceil(len(lst_avg_grades) * 0.2)

        return lst_avg_grades[:cutoff]

    def grades_under_five(self):
        """
        Get a list un all students with all average grades under five
        :return: list of average grades under five
        """
        lst_grades_under_five = []
        students = self.__stud_repo.get_all_students()
        for student in students:
            id_student = student.get_id()
            avg = self.get_average_grade_for_student(id_student)

            if avg <=5 :
                lst_grades_under_five.append((student,avg))

        return lst_grades_under_five


    def get_all_gradesrv(self):
        """
        Get the list with all grades
        :return: list of all grades
        """

        return self.__grade_repo.get_all_grades()

