import unittest
from domain.entities import Student, Laborator
class ValidatorError(Exception):
    """
    clasa validator error care aduna toate erorile
    """
    def __init__(self, errors):
        self.__errors = errors

    def getErrors(self):
        return self.__errors

class StudentValidator:

    def validate(self, st):
        errors = []
        if (st.getId()==""):
            errors.append("Id can not be empty!")
        if (st.getNume()==""):
            errors.append("Name can not be empty!")
        if (st.getGrupa()==""):
                errors.append("Grupa can not be empty!")
        if len(errors)>0:
            raise ValidatorError(errors)

class LabValidator:
    def validate(self,lab):
        errors = []
        if (lab.getNumber()==""):
            errors.append("Lab number can not be empty")
        if(lab.getProblem()==""):
            errors.append("Lab problem can not be empty")
        if(lab.getDesc()==""):
            errors.append("Description can not be empty")
        if(lab.getDeadline()==""):
            errors.append("Deadline can not be empty")
        if len(errors)>0:
            raise ValidatorError(errors)

class StudentLabValidator:
    def validate(self, student_lab):
        errors = []
        if (student_lab.getId() == ""):
            errors.append("student_lab id can not be empty")
        if (student_lab.get_student_id() == ""):
            errors.append("student_lab.txt id can not be empty")
        if (student_lab.get_lab_id() == ""):
            errors.append("lab id can not be empty")
        if (student_lab.get_grade() == ""):
            errors.append("grade can not be empty")

class ValidatorTestCase(unittest.TestCase):
    """
    clasa de teste pentru validatori
    """
    def testStudentValidator(self):
        validator = StudentValidator()

        st = Student("", "", "")
        try:
            validator.validate(st)
            assert False
        except ValidatorError as ex:
            assert len(ex.getErrors()) == 3

        st = Student("1", "", "")
        try:
            validator.validate(st)
            assert False
        except ValidatorError as ex:
            assert len(ex.getErrors()) == 2

        st = Student("2", "Ion", "218")
        try:
            validator.validate(st)
            assert True
        except ValidatorError as ex:
            assert False

    def testLaboratorValidator(self):
        validator = LabValidator()

        st = Laborator("", "", "", "")
        try:
            validator.validate(st)
            assert False
        except ValidatorError as ex:
            assert len(ex.getErrors()) == 4

        st = Laborator("1", "", "", "")
        try:
            validator.validate(st)
            assert False
        except ValidatorError as ex:
            assert len(ex.getErrors()) == 3

        st = Laborator("1", "2", "vectori","12.12.2023")
        try:
            validator.validate(st)
            assert True
        except ValidatorError as ex:
            assert False

    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ValidatorTestCase))
        return suite