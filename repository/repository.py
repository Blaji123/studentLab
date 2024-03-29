import unittest
from domain.entities import Student
from domain.validator import ValidatorError
class StudentRepository:

    def __init__(self):
        self.__items = {}

    def getAll(self):
        """
        get all method care retuneaza lista cu toate obiectele
        """
        return list(self.__items.values())

    def save(self, item):
        """
        save method care salveaza obiectele in dictionar
        """
        if item.getId() in self.__items:
            raise RepositoryError("item already exists!")
        self.__items[item.getId()] = item

    def change(self, id, item):
        """
        change method care modifica obiectele din dictionar
        """
        self.delete(id)
        self.save(item)

    def delete(self, id):
        """
        delete method care sterge obiectele din dictionar
        """
        item = self.findById(id)
        self.__items.pop(item.getId())

    def findById(self, id):
        """
        find by id method care cauta si returneaza un obiect dupa id
        """
        if not id in self.__items:
            raise RepositoryError("an item with the given id doesn't exist")
        return self.__items[id]

    def size(self):
        """
        size method care returneaza lungimea dictionarului de obiecte
        """
        return len(self.__items)

class LabRepository:

    def __init__(self):
        self.__items = {}

    def getAll(self):
        """
        get all method care retuneaza lista cu toate obiectele
        """
        return list(self.__items.values())

    def save(self, item):
        """
        save method care salveaza obiectele in dictionar
        """
        if item.getId() in self.__items:
            raise RepositoryError("item already exists!")
        self.__items[item.getId()] = item

    def change(self, item):
        """
        change method care modifica obiectele din dictionar
        """
        self.delete(id)
        self.save(item)

    def delete(self, id):
        """
        delete method care sterge obiectele din dictionar
        """
        item = self.findById(id)
        self.__items.pop(item.getId())

    def findById(self, id):
        """
        find by id method care cauta si returneaza un obiect dupa id
        """
        if not id in self.__items:
            raise RepositoryError("an item with the given id doesn't exist")
        return self.__items[id]

    def size(self):
        """
        size method care returneaza lungimea dictionarului de obiecte
        """
        return len(self.__items)

class StudentLabRepository:

    def __init__(self):
        self.__items = {}

    def getAll(self):
        """
        get all method care retuneaza lista cu toate obiectele
        """
        return list(self.__items.values())

    def save(self, item):
        """
        save method care salveaza obiectele in dictionar
        """
        if item.getId() in self.__items:
            raise RepositoryError("item already exists!")
        self.__items[item.getId()] = item

    def change(self, item):
        """
        change method care modifica obiectele din dictionar
        """
        self.delete(id)
        self.save(item)

    def delete(self, id):
        """
        delete method care sterge obiectele din dictionar
        """
        item = self.findById(id)
        self.__items.pop(item.getId())

    def findById(self, id):
        """
        find by id method care cauta si returneaza un obiect dupa id
        """
        if not id in self.__items:
            raise RepositoryError("an item with the given id doesn't exist")
        return self.__items[id]

    def size(self):
        """
        size method care returneaza lungimea dictionarului de obiecte
        """
        return len(self.__items)

class RepositoryError(ValidatorError):
    pass


class RepositoryTestCase(unittest.TestCase):
    """
    clasa de teste pentru repository
    """
    def setUp(self):
        self.__repo = StudentRepository()
        s1 = Student(1, "David", 211)
        s2 = Student(2, "George", 212)
        s3 = Student(3, "Ion", 211)
        self.__repo.save(s1)
        self.__repo.save(s2)
        self.__repo.save(s3)

    def test_size(self):
        assert (self.__repo.size() == 3)

    def test_save(self):
        s = Student(4, "Mihai", 217)
        self.__repo.save(s)
        assert (self.__repo.size() == 4)

    def test_getAll(self):
        l = self.__repo.getAll()
        assert (len(l) == 3)

    def test_delete(self):
        self.__repo.delete(3)
        assert self.__repo.size() == 2

    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RepositoryTestCase))
        return suite
