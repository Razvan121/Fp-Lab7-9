class GradeDto:
    def __init__(self, grade,id_student,id_discipline):
        self.__grade = grade
        self.__id_student = id_student
        self.__id_discipline = id_discipline


    def get_grade(self):
        return self.__grade
    def get_id_student(self):
        return self.__id_student
    def get_id_discipline(self):
        return self.__id_discipline

    def __repr__(self):
        return f"Grade :{self.__grade}"

    def __eq__(self, other):
        if isinstance(other, GradeDto):
            return (
                self.__grade == other.__grade and
                self.__id_student == other.__id_student and
                self.__id_discipline == other.__id_discipline
            )
        return False
