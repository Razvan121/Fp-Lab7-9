import unittest

from Tests.test_disciplinerepo import TestDisciplineRepo
from Tests.test_disciplineservice import TestDisciplineService
from Tests.test_entities import TestStudent, TestGrade, TestGradeDTO, TestDiscipline
from Tests.test_graderepo import TestGradeRepo
from Tests.test_gradeservice import TestGradeService
from Tests.test_studentrepo import TestStudentRepo
from Tests.test_studentservice import TestStudentService
from Tests.test_validator import TestStudentValidator


def run_tests():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestStudent))
    suite.addTests(loader.loadTestsFromTestCase(TestDiscipline))
    suite.addTests(loader.loadTestsFromTestCase(TestGrade))
    suite.addTests(loader.loadTestsFromTestCase(TestGradeDTO))
    suite.addTests(loader.loadTestsFromTestCase(TestDisciplineRepo))
    suite.addTests(loader.loadTestsFromTestCase(TestDisciplineService))
    suite.addTests(loader.loadTestsFromTestCase(TestGradeService))
    suite.addTests(loader.loadTestsFromTestCase(TestStudentRepo))
    suite.addTests(loader.loadTestsFromTestCase(TestStudentService))
    suite.addTests(loader.loadTestsFromTestCase(TestStudentValidator))
    suite.addTests(loader.loadTestsFromTestCase(TestDiscipline))
    suite.addTests(loader.loadTestsFromTestCase(TestGradeRepo))
    runner = unittest.TextTestRunner()
    runner.run(suite)