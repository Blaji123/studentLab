import unittest
from ui.console import Console
from controller.student_controller import StudentController, StudentControllerTestCase
from controller.laborator_controller import LabController, LaboratorControllerTestCase
from controller.student_lab_controller import StudentLabController, StudentLabControllerTestCase
from repository.repository import RepositoryTestCase, StudentRepository, LabRepository, StudentLabRepository
from repository.student_file_repo import StudentFileRepository, StudentFileRepositoryTestCase
from repository.lab_file_repo import LabFileRepository, LabFileRepositoryTestCase
from repository.student_lab_repo import StudentLabFileRepository, StudentLabFileRepositoryTestCase
from domain.validator import StudentValidator, LabValidator,StudentLabValidator, ValidatorTestCase
from domain.entities import StudentTestCase, LaboratorTestCase
class App:
    """
    clasa main de unde se creeaza obiecte pentru a porni aplicatia
    """
    def main(self):
        #student_repo = StudentRepository()
        student_file_repo = StudentFileRepository('student.txt')
        sc = StudentController(student_file_repo, StudentValidator())

        #lab_repo = LabRepository()
        lab_file_repo = LabFileRepository('lab.txt')
        lc = LabController(lab_file_repo, LabValidator())

        #student_lab_repo = StudentLabRepository()
        student_lab_file_repo = StudentLabFileRepository('student_lab.txt')
        slc = StudentLabController(student_file_repo, lab_file_repo, student_lab_file_repo, StudentLabValidator())

        console = Console(sc, lc, slc)
        console.run()

all_suites = unittest.TestSuite([StudentControllerTestCase.suite(),LaboratorControllerTestCase.suite(),
                                 RepositoryTestCase.suite(),StudentTestCase.suite(),LaboratorTestCase.suite(),ValidatorTestCase.suite(),StudentLabControllerTestCase.suite(),
                                StudentFileRepositoryTestCase.suite(),LabFileRepositoryTestCase.suite(),StudentLabFileRepositoryTestCase.suite()])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(all_suites)
    try:
        app = App()
        app.main()
    except Exception as ex:
        print("Exceptie in aplicatie: ", ex)