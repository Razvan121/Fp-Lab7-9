class Discipline:
    """
    class Discipline:
        """
    def __init__(self,id_discipline, name, teacher):
        """
        :param id_discipline: Unique identifier for the class
        :type id_discipline: int
        :param name: Name of the class
        :type name: str
        :param teacher: Teacher assigned to the class
        :type teacher: str
        """
        self.__id_discipline = id_discipline
        self.__name = name
        self.__teacher = teacher

    def get_id(self):
        """
        :return: the ID of the object
        """
        return self.__id_discipline

    def get_name(self):
        """
        :return: The name of the object. Returns a string representing the name.
        """
        return self.__name

    def get_teacher(self):
        """
        :return: The teacher associated with this instance.
        """
        return self.__teacher

    def set_id(self, id_discipline):
        """
        :param id_discipline: The identification value to be set for the object
        :return: None
        """
        self.__id_discipline = id_discipline

    def set_name(self, name):
        """
        :param name: The name to be set for the instance.
        :return: None
        """
        self.__name = name

    def set_teacher(self, teacher):
        """
        :param teacher: The new teacher to assign to the instance
        :return: None
        """
        self.__teacher = teacher

    def __str__(self):
        return f"ID: {self.__id_discipline} Name: {self.__name} Teacher: {self.__teacher}"
