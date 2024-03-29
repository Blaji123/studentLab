class LabStudentAssembler:
    """
    clasa lab student_lab.txt assembler care creeaza instante ale clasei labstudentdto
    """
    def create_lab_student_dto(id, student, lab, grade):
        return LabStudentDTO(id, student.getNume(), student.getGrupa(), lab.getDesc(), lab.getDeadline(), grade)

class LabAssembler:

    def create_lab_dto(id, lab, grade):
        return LabsDTO(id, lab.getNumber(),lab.getProblem(),lab.getDesc(),lab.getDeadline(),grade)

class StudentAssembler:

    def create_student_dto(id, student, grade):
        return StudentDTO(id, student.getNume(), student.getGrupa(), grade)

class LabStudentDTO:
    """
    clasa lab student_lab.txt dto care creeaza obiecte de tipul student_lab.txt + lab cu un id al clasei student_lab, un nume si o grupa
    a studentului si o descriere si un deadline al laboratorului, impreuna cu o nota
    """
    def __init__(self, id, student_name, grupa, desc, deadline, grade):
        self.__id = id
        self.__student_name = student_name
        self.__grupa = grupa
        self.__desc = desc
        self.__deadline = deadline
        self.__grade = grade

    def getId(self):
        return self.__id

    def getName(self):
        return self.__student_name

    def getGrupa(self):
        return self.__grupa

    def getDesc(self):
        return self.__desc

    def getDeadline(self):
        return self.__deadline

    def getGrade(self):
        return self.__grade

    def __str__(self):
        return "Id: " + str(self.__id) + " nume: " + str(self.__student_name) + " grupa: " + str(self.__grupa) + " descriere: " + str(self.__desc) + " deadline: " + str(self.__deadline) + " nota: " + str(self.__grade)

class LabsDTO:
    def __init__(self, id, lab_number, problem_number, desc, deadline, grade):
        self.__id = id
        self.__lab_number = lab_number
        self.__problem_number = problem_number
        self.__desc = desc
        self.__deadline = deadline
        self.__grade = grade

    def getId(self):
        return self.__id

    def getNumber(self):
        return self.__lab_number

    def getProblem(self):
        return self.__problem_number

    def getDesc(self):
        return self.__desc

    def getDeadline(self):
        return self.__deadline

    def getGrade(self):
        return self.__grade

    def __str__(self):
        return  "Id: " + str(self.__id) + " Laborator: " + str(self.__lab_number) + " Problema: " + str(self.__problem_number) + " Descriere: " + str(self.__desc) + " Deadline: " + str(self.__deadline) + " nota: " + str(self.__grade)

class StudentDTO:

    def __init__(self, id, student_name, student_grupa, grade):
        self.__id = id
        self.__student_name = student_name
        self.__student_grupa = student_grupa
        self.__grade = grade

    def getId(self):
        return self.__id

    def getNume(self):
        return self.__student_name

    def getGrupa(self):
        return self.__student_grupa

    def getNota(self):
        return self.__grade

    def __str__(self):
        return "Id: " + str(self.__id) + " nume: " + str(self.__student_name) + " grupa: " + str(self.__student_grupa) + " nota: " + str(self.__grade)