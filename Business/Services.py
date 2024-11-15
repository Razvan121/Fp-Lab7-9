from Domain.Discipline import Discipline
from Domain.Student import Student
from Exceptions.Exceptions import RepoException, SerivceException, ValidatorException


class ServiceStudents:
    def __init__(self, valid_student, repo_student):
        self.valid_student = valid_student
        self.__repo_student = repo_student

    def addstudent(self, id_student, name):
        """
        :param id_student: Identifier for the student to be added
        :param name: Name of the student to be added
        :return: The student object that was successfully added
        """
        student = Student(id_student, name)
        self.valid_student.validate_student(student)
        self.__repo_student.add_student(student)
        return student

    def delete_student(self, id_student):
        """
        :param id_student: Identifier for the student to be deleted
        :return: The student object that was successfully deleted
        """
        self.__repo_student.delete_student(id_student)
    def modify_student(self,id_student,name):
        """
        :param id_student: The unique identifier for the student to be modified.
        :param name: The new name for the student.
        """
        self.__repo_student.modify_student(id_student,name)

    def search_student(self,id_student):
        """

        :param id_student: The ID of the student to be searched
        """
        return self.__repo_student.search_student_by_ID(id_student)

    def get_all_students(self):
        """
        :return: A list of all students from the student repository
        """
        return self.__repo_student.get_all_students()


class ServiceDiscipline:
    def __init__(self, valid_discipline, repo_discipline):
        """
        :param valid_discipline: The validator instance for discipline data validation.
        :param repo_discipline: The repository instance for managing discipline data storage and retrieval.
        """
        self.__valid_discipline = valid_discipline
        self.__repo_discipline = repo_discipline

    def adddiscipline(self, id_discipline, name, teacher):
        """
        :param id_discipline: The unique identifier for the discipline.
        :param name: The name of the discipline.
        :param teacher: The teacher responsible for the discipline.
        :return: The newly added discipline object.
        """
        discipline = Discipline(id_discipline, name, teacher)
        self.__valid_discipline.validate_discipline(discipline)
        self.__repo_discipline.add_discipline(discipline)
        return discipline

    def delete_discipline(self, id_discipline):
        """
        :param id_discipline: The identifier of the discipline to be deleted
        """
        self.__repo_discipline.delete_discipline(id_discipline)

    def modify_discipline_name(self,id_discipline,name):
        """
        :param id_discipline: The unique identifier of the discipline to be modified.
        :param name: The new name for the discipline.
        """
        self.__repo_discipline.modify_discipline_name(id_discipline,name)

    def modify_discipline_teacher(self,id_discipline,teacher):
        """
        :param id_discipline: The unique identifier of the discipline to be modified.
        :param teacher: The new teacher for the discipline.

        """
        self.__repo_discipline.modify_discipline_teacher(id_discipline,teacher)

    def search_discipline(self,id_student):
        """
        :param id_student: The unique identifier of a student to search for in the discipline repository.
        :return: The discipline associated with the given student ID if found, otherwise None.
        """
        return self.__repo_discipline.search_discipline_by_ID(id_student)

    def check_new_id(self,id_discipline):
        """
        :param id_discipline: The ID of the discipline to be checked.
        """
        self.__repo_discipline.check_ID(id_discipline)



    def get_all_disciplines(self):
        """
        :return: A list of all disciplines retrieved from the repository
        """
        return self.__repo_discipline.get_all_disciplines()

