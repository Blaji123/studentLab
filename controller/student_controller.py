import unittest
from repository.repository import StudentRepository
from domain.entities import Student
from domain.validator import  StudentValidator
import random
import string
class StudentController:

    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator

    def createRandomStudent(self):
        """
        create random student_lab.txt method care creeaza un obiect de tipul student_lab.txt cu atrbibute aleatorii
        """
        id = random.randint(1,100000)
        letters = string.ascii_letters
        length = random.randint(1,20)
        nume = ''.join(random.choice(letters) for i in range(length))
        grupa = random.randint(1,300)
        student = Student(id,nume,grupa)
        self.__validator.validate(student)
        self.__repository.save(student)

    def printStudents(self):
        """
        print students method care returneaza lista cu obiectele de tipul student_lab.txt
        """
        return self.__repository.getAll()

    def addStudent(self, id, name, grupa):
        """
        add student_lab.txt method care adauga un obiect de tipul student_lab.txt in lista
        """
        s = Student(id,name,grupa)
        self.__validator.validate(s)
        self.__repository.save(s)

    def deleteStudent(self, id):
        """
        delete student_lab.txt method care sterge un obiect de tipul student_lab.txt din lista
        """
        self.__repository.delete(id)

    def changeStudent(self, id, nume, grupa):
        """
        change student_lab.txt method care modifica un obiect de tipul student_lab.txt din lista
        """
        s = Student(id,nume,grupa)
        self.__validator.validate(s)
        self.__repository.change(id, s)

    def searchStudent(self, id):
        """
        search student_lab.txt method care cauta un obiect de tipul student_lab.txt dupa id
        """
        return self.__repository.findById(id)

class StudentControllerTestCase(unittest.TestCase):
    """
    clasa de teste pentru clasa student_lab.txt controller
    """
    def setUp(self):
        self.__repo = StudentRepository()
        s1 = Student(1, "David", 211)
        s2 = Student(2, "George", 212)
        s3 = Student(3, "Ion", 213)
        self.__repo.save(s1)
        self.__repo.save(s2)
        self.__repo.save(s3)
        self.__controller = StudentController(self.__repo, StudentValidator())

    def testCreateRandomStudent(self):
        random.seed(0)
        self.__controller.createRandomStudent()
        assert self.__repo.size() == 4
        self.__controller.createRandomStudent()
        self.__controller.createRandomStudent()
        assert self.__repo.size() == 6
        try:
            random.seed(0)
            self.__controller.createRandomStudent()
            assert False
        except:
            assert True


    def test_addStudent(self):
        self.__controller.addStudent(4, "Daria", 211)
        assert self.__repo.size() == 4

    def test_printStudent(self):
        list = self.__controller.printStudents()
        assert len(list) == 3

    def test_deleteStudent(self):
        self.__controller.deleteStudent(3)
        assert self.__repo.size() == 2

    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(StudentControllerTestCase))
        return suite