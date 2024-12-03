import unittest

from Business.Services import ServiceDiscipline
from Domain.Discipline import Discipline
from Exceptions.Exceptions import SerivceException
from Infrastructure.Repostory_Discipline import repostory_discipline

from Validation.Validators import Validator


class TestDisciplineService(unittest.TestCase):
    def setUp(self)->None:
        repo = repostory_discipline()
        validator = Validator()
        self.__discipline_service = ServiceDiscipline(validator, repo)

    def test_add_discipline(self):
        self.__discipline_service.adddiscipline(1,"Math","A B")
        self.assertEqual(len(self.__discipline_service.get_all_disciplines()),1)
        # self.assertRaises(SerivceException,self.__discipline_service.adddiscipline,1,"","a b")

    def test_delete_discipline(self):
        self.__discipline_service.adddiscipline(1,"Math","A B")
        self.__discipline_service.delete_discipline(1)
        self.assertEqual(len(self.__discipline_service.get_all_disciplines()),0)

    def test_modify_name_discipline(self):
        self.__discipline_service.adddiscipline(1,"Math","A B")
        self.__discipline_service.modify_discipline_name(1,"english")
        disciplines = self.__discipline_service.get_all_disciplines()
        expectedDiscipline = Discipline(1, "english", "A B")
        self.assertTrue(expectedDiscipline, disciplines[1])

    def test_modify_teacher(self):
        self.__discipline_service.adddiscipline(1,"Math","A B")
        self.__discipline_service.modify_discipline_teacher(1,"C D")
        disciplines = self.__discipline_service.get_all_disciplines()
        expectedDiscipline = Discipline(1, "Math", "C D")
        self.assertTrue(expectedDiscipline, disciplines[1])



    def test_search_discipline(self):
        self.__discipline_service.adddiscipline(1,"Math","A B")
        discipline = self.__discipline_service.search_discipline(1)
        expectedDiscipline = Discipline(1, "Math", "A B")
        self.assertTrue(expectedDiscipline, discipline)

    def run_all_tests(self):
        unittest.main()