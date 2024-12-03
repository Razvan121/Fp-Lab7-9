class Student:
    def __init__(self, id_Student, name):
        """
        :param id_Student: The unique identifier for the student
        :param name: The name of the student
        """
        self.__id_Student = id_Student
        self.__name = name

    def get_id(self):
        """
        :return: The unique identifier of the student.
        """
        return self.__id_Student

    def get_name(self):
        """
        :return: The name of the object
        """
        return self.__name

    def set_id(self, ID):
        """
        :param ID: The unique identifier to be set for the student.
        :return: None
        """
        self.__id_Student = ID

    def set_name(self, name):
        """
        :param name: The name to set for the object.
        :return: None
        """
        self.__name = name


    @classmethod
    def from_string(cls, string):
        string = string.split(",")
        return cls(int(string[0]), (string[1]))



    def __str__(self):
        return f"ID student: {self.__id_Student} Name: {self.__name}"

