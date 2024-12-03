from Domain.Discipline import Discipline
from Domain.Grade import Grade
from Domain.GradeDto import GradeDto
from Domain.Student import Student




class GradeRepoFile():
    def __init__(self,fileName):
        self.__fileName = fileName
        self.__grades = {}


    def __load_from_file(self):
        # try:
        #     f = open(self.__fileName,'r')
        # except IOError:
        #     raise FileNotFoundError("File Not Found")
        #
        #
        #
        # f.readline()
        # for line in f:
        #     id_student,id_discipline,thisgrade = [token.strip() for token in line.split(',')]
        #     grade = GradeDto(thisgrade,id_student,id_discipline)
        #     self.__dict_grades.setdefault(id_student,{})
        #     self.__dict_grades[id_student].setdefault(id_discipline,[])
        #     self.__dict_grades[grade.get_id_student()][grade.get_id_discipline()] = thisgrade
        #
        # f.close()

        self.__grades = {}
        try:
            with open(self.__fileName,'r') as file:
                lines = file.readlines()
                for line in lines:
                    try:
                        id_student,id_discipline,thisgrade = [token.strip() for token in line.split(',')]
                        grade = GradeDto(int(thisgrade),int(id_student),int(id_discipline))

                        self.__grades.setdefault(int(id_student),{})
                        self.__grades[grade.get_id_student()].setdefault(int(id_discipline),[])
                        self.__grades[grade.get_id_student()][grade.get_id_discipline()].append(grade)


                    except ValueError as e:
                        print(e)
            return self.__grades
        except IOError:
            raise FileNotFoundError("File Not Found")

    def __save_to_file(self,grades):
        # with open(self.__fileName,'w') as grades_file:
        #     for grade in grades:
        #         grades_string = str(grade.get_id_student()) +','  + str(grade.get_id_discipline()) +  ',' + str(grade.get_grade()) +'\n'
        #         grades_file.write(grades_string)

        with open(self.__fileName, 'w') as grades_file:
            for student_id, disciplines in grades.items():  # Outer dictionary
                for discipline_id, grade_list in disciplines.items():  # Inner dictionary
                    for grade in grade_list:  # List of GradeDto objects
                        grades_string = (
                                str(grade.get_id_student()) + ',' +
                                str(grade.get_id_discipline()) + ',' +
                                str(grade.get_grade()) + '\n'
                        )
                        grades_file.write(grades_string)

    def add_grade(self,grade):
        """
        Function to add grades to the grades list
        :param grade: the grade added to the grades list
        :return:
        """
        id_student = grade.get_id_student()
        id_discipline = grade.get_id_discipline()

        self.__grades.setdefault(id_student,{})
        self.__grades[id_student].setdefault(id_discipline,[])
        self.__grades[id_student][id_discipline].append(grade)
        self.__save_to_file(self.__grades)

    def delete_grade(self,id_student,id_discipline,grade):
        """
        Function to delete grades from the grades list
        :param grade: the grade deleted from the grades list
        :param id_student: The unique identifier for student
        :param id_discipline: The unique identifier for discipline
        :return:
        """
        self.__grades = self.__load_from_file()

        grades = self.__grades[id_student][id_discipline]
        for thisgrade in grades:
            if thisgrade.get_grade() == grade.get_grade():
                grades.remove(thisgrade)

        self.__save_to_file(self.__grades)


    def get_all_grades(self):
        """
        Function that returns all the grades in the grades list
        :return:
        """

        return self.__load_from_file()

    def get_len_student(self):
        """
        Function that returns the number of all the students in the grades list
        :return: an integer representing all students
        """

        return len(self.__load_from_file())











