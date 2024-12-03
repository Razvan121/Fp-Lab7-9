class repostory_students:
    def __init__(self):
         self.__lst_students = []

    def check_ID(self, ID):
        """
        :param ID: The identification number to check against the list of students.
        :return: True if a student with the given ID is found, False otherwise.
        """
        for student in self.__lst_students:
            if student.get_id() == ID:
                return True
        return False

        # return ID in self.__dict_students

    def add_student(self, student):
        """
        :param student: The student object to be added to the student list.
        :type student: Student
        :raises ValueError: If the student with the same ID already exists in the list.
        """
        for st in self.__lst_students:
            if st.get_id() == student.get_id():
                raise ValueError("Student already exist")
        self.__lst_students.append(student)

        # student_id = student.get_id()
        # if student_id in self.__dict_students:
        #     raise ValueError("Student already exist")
        #
        # self.__dict_students[student_id] = student

    def delete_student(self, ID):
        """
        :param ID: The identification number of the student to be removed.
        :type ID: int
        :raises ValueError: If the student with the given ID does not exist.
        """
        self.__lst_students = [d for d in self.__lst_students if d.get_id() != ID]
        #
        # del self.__dict_students[ID]


    def modify_student(self, ID,name):
        """
        :param ID: The identification number of the student to be modified.
        :param name: The new name for the student.
        """

        for st in self.__lst_students:
            if st.get_id() == ID:
                st.set_name(name)

        # self.__dict_students[ID].set_name(name)

    def search_student_by_ID(self, ID):
        """
        :param ID: The unique identifier for the student to search for.
        :return: The student object if found, or None if no student with the given ID exists.
        """

        for st in self.__lst_students:
            if st.get_id() == ID:
                return st



    def get_all_students(self):
        return self.__lst_students

    def get_len_student(self):
        """
        Function that returns the number of all the students in the grades list
        :return: an integer representing all students
        """

        return len(self.__lst_students)


