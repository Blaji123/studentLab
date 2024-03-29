from domain.entities import Student
from repository.repository import StudentRepository
import unittest
import os
class StudentFileRepository(StudentRepository):

    def __init__(self, file_name):
        StudentRepository.__init__(self)
        self.__file_name = file_name
        self.__loadFromFile()

    def __loadFromFile(self):
        try:
            f = open(self.__file_name, "r")
        except IOError:
            # file not exist
            return
        line = f.readline().strip()
        while line != "":
            attrs = line.split(",")
            student = Student(int(attrs[0]), attrs[1], int(attrs[2]))
            StudentRepository.save(self, student)
            line = f.readline().strip()
        f.close()

    def save(self, student):
        StudentRepository.save(self, student)
        self.__storeToFile()

    def delete(self, id):
        StudentRepository.delete(self, id)
        self.__storeToFile()

    def change(self, id, student):
        StudentRepository.change(self, id, student)
        self.__storeToFile()

    def findById(self, id):
        return StudentRepository.findById(self, id)

    def size(self):
        return StudentRepository.size(self)

    def getAll(self):
        return StudentRepository.getAll(self)

    def __storeToFile(self):
        f = open(self.__file_name, "w")
        students = StudentRepository.getAll(self)
        for student in students:
            strf = str(student.getId()) + "," + student.getNume() + "," + str(student.getGrupa()) + "\n"
            f.write(strf)
        f.close()

class StudentFileRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        # You may want to use a temporary file for testing
        self.file_name = "test_students.txt"
        self.repo = StudentFileRepository(self.file_name)
        self.student1 = Student(1, "John Doe", 123)
        self.student2 = Student(2, "Jane Smith", 456)

    def tearDown(self):
        # Clean up the temporary file after testing
        try:
            os.remove(self.file_name)
        except FileNotFoundError:
            pass

    def test_load_from_file(self):
        with open(self.file_name, "w") as f:
            f.write("1,John Doe,123\n2,Jane Smith,456")

        repo = StudentFileRepository(self.file_name)
        result = repo.getAll()
        self.assertEqual(result, [self.student1, self.student2])

    def test_save(self):
        self.repo.save(self.student1)
        self.repo.save(self.student2)
        self.repo = StudentFileRepository(self.file_name)  # Reinitialize repo to load from file
        result = self.repo.getAll()
        self.assertEqual(result, [self.student1, self.student2])

    def test_delete(self):
        self.repo.save(self.student1)
        self.repo.save(self.student2)
        self.repo.delete(1)
        self.repo = StudentFileRepository(self.file_name)  # Reinitialize repo to load from file
        result = self.repo.getAll()
        self.assertEqual(result, [self.student2])

    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(StudentFileRepositoryTestCase))
        return suite