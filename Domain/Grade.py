class Grade:
    def __init__(self, grade, student, discipline):
        """
        :param grade: The grade received.
        :param student: The student class received.
        :param discipline: The discipline class receive.
        """
        self.__grade = grade
        self.__student = student
        self.__discipline = discipline


    def get_grade(self):
        """
        :return: An integer representing the grade
        """
        return self.__grade

    def get_id_student(self):
        """
        :return: The ID of the student retrieved from the student object.
        """
        return self.__student.get_id()

    def get_name_student(self):
        """
        :return: The name of the student retrieved from the private student attribute.
        """
        return self.__student.get_name()

    def get_id_discipline(self):
        """
        :return: The unique identifier for discipline
        """
        return self.__discipline.get_id()

    def get_name_discipline(self):
        """
        :return: Name of the discipline
        """
        return self.__discipline.get_name()
    def get_teacher_discipline(self):
        """
        :return: The teacher of the associated discipline.
        """
        return self.__discipline.get_teacher()



    def set_grade(self, grade):
        """
        :param grade: The grade assigned
        """
        self.__grade = grade

    def __repr__(self):
        return f"Grade :{self.__grade})"
