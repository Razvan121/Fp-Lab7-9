class repostory_grade():
    def __init__(self):
        self.__dict_grade = {}

    def add_grade(self, grade):
        """
        :param grade: The grade object
        """
        student_id = grade.get_id_student()
        discipline_id = grade.get_id_discipline()

        # Ensure student and discipline exist in the structure
        self.__dict_grade.setdefault(student_id, {})
        self.__dict_grade[student_id].setdefault(discipline_id, [])

        if grade in self.__dict_grade[student_id][discipline_id]:
            raise ValueError("Grade already assigned")

        self.__dict_grade[grade.get_id_student()][grade.get_id_discipline()].append(grade)

    def delete_grade(self, id_student, id_discipline,grade):
        """
                :param id_student: ID of the student
                :param id_discipline: ID of the discipline
                :param grade: Grade to delete
                """
        # try:
        #     grades = self.__dict_grade[id_student][id_discipline]
        #     for existing_grade in grades:
        #         if existing_grade.get_grade() == grade.get_grade():
        #             grades.remove(existing_grade)
        #             break
        #     else:
        #         raise ValueError("Grade not found")
        # except KeyError:
        #     raise ValueError("Student or discipline not found")

        try:
            grades = self.__dict_grade[id_student][id_discipline]
            grades.remove(grade)  # Remove the grade directly
            # Clean up empty lists or dictionaries
            if not grades:
                del self.__dict_grade[id_student][id_discipline]
            if not self.__dict_grade[id_student]:
                del self.__dict_grade[id_student]
        except (KeyError, ValueError):
            raise ValueError("Student, discipline, or grade not found")


    def get_all_grades(self):
        """
        :return: A dictionary with all grades
        """
        return self.__dict_grade
