class repostory_grade():
    def __init__(self):
        self.__dict_grade = {}

    def add_grade(self,grade):
        """
        :param grade: The grade object
        """
        # for gr in self.__lst_grade:
        #     if gr.get_id_student() == grade.get_id_student() and gr.get_id_discipline() == grade.get_id_discipline():
        #         raise ValueError("Grade already assigned to ")
        #     self.__lst_grade[id_student][id_discipline].append(grade)
        if grade.get_id_student() not in self.__dict_grade:
            self.__dict_grade[grade.get_id_student()] = {}
        if grade.get_id_discipline() not in self.__dict_grade[grade.get_id_student()]:
            self.__dict_grade[grade.get_id_student()][grade.get_id_discipline()] = []

        if grade in self.__dict_grade:
            raise ValueError("Grade already assigned to ")

        self.__dict_grade[grade.get_id_student()][grade.get_id_discipline()].append(grade)

    def get_all_grades(self):
        return self.__dict_grade