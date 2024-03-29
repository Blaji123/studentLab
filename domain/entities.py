import unittest
class Student:
    """
    clasa Student care creeaza obiecte de tipul student_lab.txt cu un id, nume, grupa
    """
    def __init__(self, student_id, student_nume, student_grupa):
        self.__student_id = student_id
        self.__student_nume = student_nume
        self.__student_grupa = student_grupa

    def getId(self):
        return self.__student_id

    def getNume(self):
        return self.__student_nume

    def getGrupa(self):
        return self.__student_grupa


    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (
            self.__student_id == other.__student_id
            and self.__student_nume == other.__student_nume
            and self.__student_grupa == other.__student_grupa
        )

    def __str__(self):
        return "ID: " + str(self.__student_id) + " nume: " + str(self.__student_nume) + " grupa: " + str(self.__student_grupa)

class Laborator:
    """
    clasa laborator care creeaza obiecte de tipul laborator cu un numar,problema,descriere,deadline
    """
    def __init__(self, lab_number, lab_problem, lab_desc, lab_deadline):
        self.__lab_number = lab_number
        self.__lab_problem = lab_problem
        self.__lab_desc = lab_desc
        self.__lab_deadline = lab_deadline

    def getNumber(self):
        return self.__lab_number

    def getProblem(self):
        return self.__lab_problem

    def getDesc(self):
        return self.__lab_desc

    def getDeadline(self):
        return self.__lab_deadline

    def getId(self):
        return int(str(self.__lab_number) + str(self.__lab_problem))

    def __eq__(self, other):
        if not isinstance(other, Laborator):
            return False
        return (
                self.__lab_number == other.__lab_number
                and self.__lab_problem == other.__lab_problem
                and self.__lab_desc == other.__lab_desc
                and self.__lab_deadline == other.__lab_deadline
        )

    def __str__(self):
        return "Laborator: " + str(self.__lab_number) + " Problema: " + str(self.__lab_problem) + " Descriere: " + str(self.__lab_desc) + " Deadline: " + str(self.__lab_deadline)

class StudentLab:
    """
    clasa student_lab.txt lab care creeaza obiecte de tipul student_lab.txt+lab cu un id propriu, un student_lab.txt id, un lab id si o nota
    """
    def __init__(self, student_lab_id, student_id, lab_id, grade):
        self.__student_lab_id = student_lab_id
        self.__student_id = student_id
        self.__lab_id = lab_id
        self.__grade = grade

    def getId(self):
        return self.__student_lab_id

    def get_student_id(self):
        return self.__student_id

    def get_lab_id(self):
        return self.__lab_id

    def get_grade(self):
        return self.__grade

    def set_grade(self, value):
        self.__grade = value

    def __eq__(self, other):
        if not isinstance(other, StudentLab):
            return False
        return (
                self.__student_lab_id == other.__student_lab_id
                and self.__student_id == other.__student_id
                and self.__lab_id == other.__lab_id
                and self.__grade == other.__grade
        )

    def __str__(self):
        return "Student Lab id: " + str(self.__student_lab_id) + " Student id: " + str(self.__student_id) + " Lab Id: " + str(self.__lab_id) + " nota: " + str(self.__grade)

class StudentTestCase(unittest.TestCase):
    def testStudent(self):
        st = Student("1E","George","212")
        assert st.getId() == "1E"
        assert st.getNume() == "George"
        assert st.getGrupa() == "212"

    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(StudentTestCase))
        return suite

class LaboratorTestCase(unittest.TestCase):
    def testLaborator(self):
        lab = Laborator("1","3","Vectori","12.12.2023")
        assert lab.getNumber() == "1"
        assert lab.getProblem() == "3"
        assert lab.getDesc() == "Vectori"
        assert lab.getDeadline() == "12.12.2023"
    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LaboratorTestCase))
        return suite