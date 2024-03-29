import unittest
from repository.repository import LabRepository
from domain.entities import Laborator
from domain.validator import LabValidator
import string
import random
import datetime
from datetime import timedelta
class LabController:

    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator

    def createRandomLab(self):
        """
        create random lab method care creeaza un obiect de tipul laborator cu atrbibute aleatorii
        """
        lab = random.randint(1,100000)
        prblm = random.randint(1,100000)
        letters = string.ascii_letters
        length = random.randint(1, 20)
        desc = ''.join(random.choice(letters) for i in range(length))
        startdate = datetime.datetime.now()
        enddate = startdate + timedelta(days=60)
        randomdate = startdate + (enddate - startdate) * random.random()
        deadline = str(randomdate)
        lab = Laborator(lab,prblm,desc,deadline)
        self.__validator.validate(lab)
        self.__repository.save(lab)

    def printProblems(self):
        """
        print problems method care returneaza lista cu obiectele de tipul laborator
        """
        return self.__repository.getAll()

    def addProblema(self, num, prblm, desc, deadline):
        """
        add problems method care adauga un obiect de tipul laborator in lista
        """
        lab = Laborator(num,prblm,desc,deadline)
        self.__validator.validate(lab)
        self.__repository.save(lab)

    def deleteProblem(self, num, prblm):
        """
        delete problem method care sterge un obiect de tipul laborator din lista
        """
        id = int(str(num) + str(prblm))
        self.__repository.delete(id)

    def changeProblem(self, num, prblm, desc, deadline):
        """
        change problem method care modifica un obiect de tipul laborator din lista
        """
        lab = Laborator(num, prblm, desc, deadline)
        self.__validator.validate(lab)
        self.__repository.change(lab)

    def searchProblem(self, num, prblm):
        """
        search problem method care cauta un obiect de tipul problema dupa id
        """
        id = int(str(num) + str(prblm))
        return self.__repository.findById(id)

class LaboratorControllerTestCase(unittest.TestCase):
    """
    clasa de teste pentru clasa laborator controller
    """
    def setUp(self):
        self.__repo = LabRepository()
        lab1 = Laborator(1, 3, "vectori","12.12.2023")
        lab2 = Laborator(1, 2, "matrici", "11.11.2023")
        lab3 = Laborator(2, 1, "oop", "1.2.2024")
        self.__repo.save(lab1)
        self.__repo.save(lab2)
        self.__repo.save(lab3)
        self.__controller = LabController(self.__repo, LabValidator())

    def testCreateRandomLab(self):
        random.seed(0)
        self.__controller.createRandomLab()
        assert self.__repo.size() == 4
        self.__controller.createRandomLab()
        self.__controller.createRandomLab()
        assert self.__repo.size() == 6
        try:
            random.seed(0)
            self.__controller.createRandomLab()
            assert False
        except:
            assert True

    def test_addProblema(self):
        self.__controller.addProblema(2,2, "vectori", "11.12.2023")
        assert self.__repo.size() == 4

    def test_printProblems(self):
        list = self.__controller.printProblems()
        assert len(list) == 3

    def test_deleteStudent(self):
        self.__controller.deleteProblem(1,2)
        assert self.__repo.size() == 2

    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LaboratorControllerTestCase))
        return suite