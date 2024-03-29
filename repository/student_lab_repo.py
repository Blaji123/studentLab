from domain.entities import StudentLab
from repository.repository import StudentLabRepository, RepositoryError
import unittest
import os
class StudentLabFileRepository(StudentLabRepository):

    def __init__(self, file_name):
        StudentLabRepository.__init__(self)
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
            student_lab = StudentLab(int(attrs[0]), int(attrs[1]), int(attrs[2]), int(attrs[3]))
            StudentLabRepository.save(self, student_lab)
            line = f.readline().strip()
        f.close()

    def save(self, student_lab):
        try:
            StudentLabRepository.save(self, student_lab)
            self.__storeToFile()
        except RepositoryError as se:
            print(se)

    def delete(self, id):
        StudentLabRepository.delete(self, id)
        self.__storeToFile()

    def change(self,student_lab):
        StudentLabRepository.change(self, student_lab)
        self.__storeToFile()

    def findById(self, id):
        return StudentLabRepository.findById(self, id)

    def size(self):
        return StudentLabRepository.size(self)

    def getAll(self):
        return StudentLabRepository.getAll(self)

    def __storeToFile(self):
        f = open(self.__file_name,"w")
        students_lab = StudentLabRepository.getAll(self)
        for student_lab in students_lab:
            stlrf = str(student_lab.getId()) + "," + str(student_lab.get_student_id()) + "," + str(student_lab.get_lab_id()) + "," + str(student_lab.get_grade()) + "\n"
            f.write(stlrf)
        f.close()

class StudentLabFileRepositoryTestCase(unittest.TestCase):
    """
    clasa de teste pentru repository
    """
    def setUp(self):
        # You may want to use a temporary file for testing
        self.file_name = "test_student_labs.txt"
        self.repo = StudentLabFileRepository(self.file_name)
        self.student_lab1 = StudentLab(1, 101, 201, 10)
        self.student_lab2 = StudentLab(2, 102, 202, 9)

    def tearDown(self):
        # Clean up the temporary file after testing
        try:
            os.remove(self.file_name)
        except FileNotFoundError:
            pass

    def test_load_from_file(self):
        with open(self.file_name, "w") as f:
            f.write("1,101,201,10\n2,102,202,9")

        repo = StudentLabFileRepository(self.file_name)
        result = repo.getAll()
        self.assertEqual(result, [self.student_lab1, self.student_lab2])

    def test_save(self):
        self.repo.save(self.student_lab1)
        self.repo.save(self.student_lab2)
        self.repo = StudentLabFileRepository(self.file_name)  # Reinitialize repo to load from file
        result = self.repo.getAll()
        self.assertEqual(result, [self.student_lab1, self.student_lab2])

    def test_delete(self):
        self.repo.save(self.student_lab1)
        self.repo.save(self.student_lab2)
        self.repo.delete(1)
        self.repo = StudentLabFileRepository(self.file_name)  # Reinitialize repo to load from file
        result = self.repo.getAll()
        self.assertEqual(result, [self.student_lab2])

    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(StudentLabFileRepositoryTestCase))
        return suite