import math

from Domain.Grade import Grade
from Sorting.BubbleSort import BubbleSort
from Sorting.ShellSort import shellSort


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
        listCopy = BubbleSort(result,key=lambda grade: grade.get_grade(),reverse=True)
        # return sorted(result, key=lambda grade: grade.get_grade(), reverse=True)
        return listCopy


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
        # sorted_students = sorted(students, key=lambda student: student.get_name())
        sorted_students = BubbleSort(students,key = lambda student: student.get_name())

        sort_grades = []

        for student in sorted_students:
            grades = [
                grade
                for disciplines in self.__grade_repo.get_all_grades().get(student.get_id(), {}).values()
                for grade in disciplines
            ]

            sort_grades.append((student,sorted(grades, key=lambda grade: grade.get_grade(), reverse=True)))

        return sort_grades

    # def get_average_grade_for_student(self,id_student):
    #     """
    #     Get an average grades for every student
    #     :param id_student: The unique id of the student.
    #     :return average_grade: The average grade of the student with 2 decimal
    #
    #     """
    #
    #     student = self.__stud_repo.search_student_by_ID(id_student)
    #
    #     if student is None:
    #         raise ValueError(f"Student with ID {id_student} not found")
    #
    #     disciplines = self.__grade_repo.get_all_grades().get(id_student, {})
    #
    #     average_grade = 0
    #     grade_count = 0
    #
    #     for discipline in disciplines.values():
    #         for grade in discipline:
    #             average_grade += grade.get_grade()
    #             grade_count +=1
    #
    #     if grade_count >0:
    #         average_grade /= grade_count
    #     else:
    #         average_grade = 0
    #
    #
    #     return round(average_grade,2)

    def get_average_grade_for_student(self, id_student):
        """
        Get an average grade for a specific student using recursion.
        :param id_student: The unique ID of the student.
        :return average_grade: The average grade of the student rounded to 2 decimals.
        """

        student = self.__stud_repo.search_student_by_ID(id_student)
        if student is None:
            raise ValueError(f"Student with ID {id_student} not found")

        disciplines = self.__grade_repo.get_all_grades().get(id_student, {})

        def recursive_calculate(grades_list, index=0, total_sum=0, count=0):
            if index == len(grades_list):
                return total_sum, count

            return recursive_calculate(grades_list, index + 1, total_sum + grades_list[index].get_grade(), count + 1)


        total_sum = 0
        grade_count = 0

        for grades in disciplines.values():
            partial_sum, partial_count = recursive_calculate(grades)
            total_sum += partial_sum
            grade_count += partial_count


        if grade_count > 0:
            return round(total_sum / grade_count, 2)
        else:
            return 0

    def sort_grades_by_student(self):
        """
        Get 20% of first students with the highest average grades
        :return: list of sorted grades by student
        """
        
        lst_avg_grades = []
        
        students = self.__stud_repo.get_all_students()
        # Complexitate: O(n), unde n este numărul de studenți din sistem.
        
        for student in students:
            id_student = student.get_id()
            avg = self.get_average_grade_for_student(id_student)
            
            lst_avg_grades.append((student,avg))
        # Complexitate: O(n * m), unde n este numărul de studenți și m este numărul de discipline.
        # Dacă numărul de discipline variază, atunci complexitatea este O(n * m).
        # Dacă este un număr fix de discipline, poate fi considerată O(n).



        BubbleSort(lst_avg_grades,key=lambda x: x[1],reverse=True)
        # Complexitate: O(n^2), deoarece BubbleSort are o complexitate de O(n^2) în cel mai rău caz.

        cutoff = math.ceil(len(lst_avg_grades) * 0.2)

        return lst_avg_grades[:cutoff]
        # Complexitate: O(k), unde k este numărul de studenți care au medii sub top 20%.

    # def grades_under_five(self):
    #     """
    #     Get a list un all students with all average grades under five
    #     :return: list of average grades under five
    #     """
    #     lst_grades_under_five = []
    #     students = self.__stud_repo.get_all_students()
    #     for student in students:
    #         id_student = student.get_id()
    #         avg = self.get_average_grade_for_student(id_student)
    #
    #         if avg <=5 :
    #             lst_grades_under_five.append((student,avg))
    #
    #     return lst_grades_under_five
    def grades_under_five(self):
        """
        Get a list of all students with all average grades under five (recursive version).
        :return: list of average grades under five
        """
        students = self.__stud_repo.get_all_students()

        def recursive_filter(lst_students, index=0, result=[]):

            if index == len(lst_students):
                return result

            student = lst_students[index]
            id_student = student.get_id()
            avg = self.get_average_grade_for_student(id_student)

            if avg <= 5:
                result.append((student, avg))

            return recursive_filter(lst_students, index + 1, result)

        return recursive_filter(students)

    def get_all_gradesrv(self):
        """
        Get the list with all grades
        :return: list of all grades
        """

        return self.__grade_repo.get_all_grades()

