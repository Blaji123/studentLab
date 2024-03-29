from domain.entities import Laborator
from repository.repository import LabRepository
import os
import unittest
class LabFileRepository(LabRepository):

    def __init__(self, file_name):
        LabRepository.__init__(self)
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
            lab = Laborator(int(attrs[0]), int(attrs[1]), attrs[2],attrs[3])
            LabRepository.save(self, lab)
            line = f.readline().strip()
        f.close()

    def save(self, lab):
        LabRepository.save(self, lab)
        self.__storeToFile()

    def delete(self, id):
        LabRepository.delete(self, id)
        self.__storeToFile()

    def change(self,lab):
        LabRepository.change(self, lab)
        self.__storeToFile()

    def findById(self, id):
        return LabRepository.findById(self, id)

    def size(self):
        return LabRepository.size(self)

    def getAll(self):
        return LabRepository.getAll(self)

    def __storeToFile(self):
        f = open(self.__file_name,"w")
        labs = LabRepository.getAll(self)
        for lab in labs:
            lrf = str(lab.getNumber()) + "," + str(lab.getProblem()) + "," + lab.getDesc() + "," + lab.getDeadline() + "\n"
            f.write(lrf)
        f.close()

class LabFileRepositoryTestCase(unittest.TestCase):
    """
    clasa de teste pentru repository
    """
    def setUp(self):
        # You may want to use a temporary file for testing
        self.file_name = "test_labs.txt"
        self.repo = LabFileRepository(self.file_name)
        self.lab1 = Laborator(1, 101, "Lab 1", "2023-01-01")
        self.lab2 = Laborator(2, 102, "Lab 2", "2023-02-01")

    def tearDown(self):
        # Clean up the temporary file after testing
        try:
            os.remove(self.file_name)
        except FileNotFoundError:
            pass

    def test_load_from_file(self):
        with open(self.file_name, "w") as f:
            f.write("1,101,Lab 1,2023-01-01\n2,102,Lab 2,2023-02-01")

        repo = LabFileRepository(self.file_name)
        result = repo.getAll()
        self.assertEqual(result, [self.lab1, self.lab2])

    def test_save(self):
        self.repo.save(self.lab1)
        self.repo.save(self.lab2)
        self.repo = LabFileRepository(self.file_name)  # Reinitialize repo to load from file
        result = self.repo.getAll()
        self.assertEqual(result, [self.lab1, self.lab2])

    def test_delete(self):
        self.repo.save(self.lab1)
        self.repo.save(self.lab2)
        self.repo.delete(1101)
        self.repo = LabFileRepository(self.file_name)  # Reinitialize repo to load from file
        result = self.repo.getAll()
        self.assertEqual(result, [self.lab2])

    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LabFileRepositoryTestCase))
        return suite