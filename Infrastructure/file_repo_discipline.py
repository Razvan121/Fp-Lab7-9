from Domain.Discipline import Discipline
from Exceptions.Exceptions import RepoException


class DisciplineRepoFile:
    def __init__(self,fileName):
        self.__fileName = fileName

    def __load_from_file(self):
        try:
            f = open(self.__fileName,'r')
        except IOError:
            raise FileNotFoundError("File Not Found")

        disciplines = []
        lines = f.readlines()
        for line in lines:
            id_discipline,name,teacher  = [token.strip() for token in line.split(',')]
            discipline = Discipline(int(id_discipline),name,teacher)
            disciplines.append(discipline)

        f.close()
        return disciplines

    def __save_to_file(self,disciplines):
        with open(self.__fileName,'w') as file:
            for discipline in disciplines:
                discipline_string  = str(discipline.get_id()) + ',' + str(discipline.get_name()) + ',' + str(discipline.get_teacher()) +'\n'
                file.write(discipline_string)

    def search_discipline_by_ID(self,id_discipline):
        """
        Search a discipline in lists
        :param id_discipline: The unique id of the discipline
        :return: Discipline
        """

        allDisciplines = self.__load_from_file()
        for discipline in allDisciplines:
            if discipline.get_id() == id_discipline:
                return discipline
        raise RepoException("Discipline Not Found")


    def add_discipline(self,newdiscipline):
        """
        Add a discipline to the list
        :param id_discipline: The unique id of the discipline
        :return:
        """

        allDisciplines = self.__load_from_file()
        for discipline in allDisciplines:
            if discipline.get_id() == newdiscipline.get_name():
                raise RepoException("Discipline Already Exists")

        allDisciplines.append(newdiscipline)
        self.__save_to_file(allDisciplines)

    def delete_discipline(self,id_discipline):
        """
        Remove a discipline from the list
        :param id_discipline: The unique id of the discipline
        :return:
        """

        allDisciplines = self.__load_from_file()
        for i in range( len(allDisciplines)):
            if allDisciplines[i].get_id() == id_discipline:
                allDisciplines.pop(i)
                self.__save_to_file(allDisciplines)
                return
        raise RepoException("Discipline Not Found")

    def modify_discipline_name(self,id_discipline,name):
        """
        Update a discipline in list
        :param id_discipline: The unique id of the discipline
        :param name: The name of the discipline
        :return:
        """

        allDisciplines = self.__load_from_file()
        for discipline in allDisciplines:
            if discipline.get_id() == id_discipline:
                discipline.set_name(name)
                self.__save_to_file(allDisciplines)
                return
        raise RepoException("Discipline Not Found")

    def modify_discipline_teacher(self,id_discipline,teacher):
        """
                Update a discipline in list
                :param id_discipline: The unique id of the discipline
                :param teacher: The teacher name of the discipline
                :return:
                """

        allDisciplines = self.__load_from_file()
        for discipline in allDisciplines:
            if discipline.get_id() == id_discipline:
                discipline.set_teacher(teacher)
                self.__save_to_file(allDisciplines)
                return
        raise RepoException("Discipline Not Found")



    def get_all_disciplines(self):
        """
        Function to get all disciplines in the list
        :return:
        """
        return self.__load_from_file()






