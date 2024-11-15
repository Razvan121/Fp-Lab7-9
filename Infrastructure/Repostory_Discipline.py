class repostory_discipline:

    def __init__(self):
        # self.__lst_disciplines = []
        self.__dict_disciplines = {}

    def check_ID(self,ID):
        """
        :param ID: The identifier to be checked.
        :return: True if the ID exists in the list of disciplines, otherwise False.
        """
        # for discipline in self.__lst_disciplines:
        #     if discipline.get_id() == ID:
        #         return True
        # return False

        return ID in self.__dict_disciplines

    def add_discipline(self,discipline):
        """
        :param discipline: The discipline to be added to the list of disciplines.
        :type discipline: Discipline
        :raises ValueError: If the discipline already exists in the list.
        :return: None
        """
        # for dis in self.__lst_disciplines:
        #     if dis.get_id() == discipline.get_id():
        #         raise ValueError("Discipline already exist")
        # self.__lst_disciplines.append(discipline)

        discipline_id = discipline.get_id()
        if discipline_id in self.__dict_disciplines:
            raise ValueError("Discipline already exist")

        self.__dict_disciplines[discipline_id] = discipline

    def delete_discipline(self, ID):
        """
        :param ID: The unique identifier of the discipline to be deleted.
        :return: None
        """
        # self.__lst_disciplines = [d for d in self.__lst_disciplines if d.get_id() != ID]
        del self.__dict_disciplines[ID]


    def modify_discipline_name(self,ID,name):
        """
        :param ID: The unique identifier of the discipline to be modified.
        :param name: The new name to be set for the discipline.
        """
        # for st in self.__lst_disciplines:
        #     if st.get_id() == ID:
        #         st.set_name(name)
        self.__dict_disciplines[ID].set_name(name)
    def modify_discipline_teacher(self,ID,teacher):

        """
        :param ID: The unique identifier of the discipline to be modified.
        :param teacher:  The new teacher to be set for the discipline.
        """
        # for st in self.__lst_disciplines:
        #     if st.get_id() == ID:
        #         st.set_teacher(teacher)

        self.__dict_disciplines[ID].set_teacher(teacher)

    def search_discipline_by_ID(self,ID):
        """
        Searches for a discipline in the dictionary of disciplines by its ID.

        :param ID: The ID of the discipline to be searched.
        :return: The discipline object if found, None otherwise.
        """
        if ID in self.__dict_disciplines:
            return self.__dict_disciplines[ID]
        else: raise ValueError("Discipline does not exist")



    def get_all_disciplines(self):
        # return self.__lst_disciplines
        return self.__dict_disciplines

