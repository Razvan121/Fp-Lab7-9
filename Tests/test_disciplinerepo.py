import unittest

from Domain.Discipline import Discipline
from Exceptions.Exceptions import RepoException
from Infrastructure.Repostory_Discipline import repostory_discipline


class TestDisciplineRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo  = repostory_discipline()

    def test_add_discipline(self):
        discipline1 = Discipline(1,"Math","Ion Gabriel")
        discipline2 = Discipline(2,"English","Murariu Sonia")

        self.__repo.add_discipline(discipline1)
        self.__repo.add_discipline(discipline2)
        self.assertEqual(len(self.__repo.get_all_disciplines()),2)

    def test_remove_discipline(self):
        discipline1 = Discipline(1,"Math","Ion Gabriel")
        self.__repo.add_discipline(discipline1)
        discipline2 = Discipline(2,"English","A B")
        self.__repo.add_discipline(discipline2)
        self.__repo.delete_discipline(1)
        disciplines = self.__repo.get_all_disciplines()
        self.assertEqual(len(self.__repo.get_all_disciplines()),1)
        self.assertEqual(disciplines[2],discipline2)

    def test_get_disciplines(self):
        discipline1 = Discipline(1,"Math","Ion Gabriel")
        discipline2 = Discipline(2,"English","A B")
        self.__repo.add_discipline(discipline1)
        self.__repo.add_discipline(discipline2)
        disciplines = self.__repo.get_all_disciplines()
        self.assertEqual(len(self.__repo.get_all_disciplines()),2)


    def test_search_disciplines(self):
        discipline1 = Discipline(1,"Math","Ion Gabriel")
        discipline2 = Discipline(2,"English","A B")
        self.__repo.add_discipline(discipline1)
        self.__repo.add_discipline(discipline2)
        disciplineSearch = self.__repo.search_discipline_by_ID(1)
        assert disciplineSearch == discipline1

    def test_modify_discipline_name(self):
        discipline1 = Discipline(1,"Math","Ion Gabriel")
        self.__repo.add_discipline(discipline1)
        self.__repo.modify_discipline_name(1,"English")
        self.assertEqual(discipline1.get_name(), "English")

    def test_modify_discipline_teacher(self):
        discipline1 = Discipline(1,"Math","Ion Gabriel")
        self.__repo.add_discipline(discipline1)
        self.__repo.modify_discipline_teacher(1,"Mihai B")
        self.assertEqual(discipline1.get_teacher(), "Mihai B")



    def run_all_tests(self):
        unittest.main()

