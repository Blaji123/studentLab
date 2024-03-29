import unittest
from domain.dto import LabStudentAssembler, LabAssembler, StudentAssembler
from domain.entities import StudentLab, Student, Laborator
from domain.validator import StudentLabValidator, LabValidator, StudentValidator
from repository.repository import StudentLabRepository, RepositoryError, StudentRepository, LabRepository
from controller.laborator_controller import LabController
from controller.student_controller import StudentController
from generic_sort.sort import Sorting
from sorting_algorithms.algorithms import Algorithm
class StudentLabController:

    def __init__(self, student_repo, lab_repo, student_lab_repo, validator):
        self.__student_repo = student_repo
        self.__lab_repo = lab_repo
        self.__student_lab_repo = student_lab_repo
        self.__validator = validator

    def printStudentLab(self):
      """
      print students method care returneaza lista cu obiectele de tipul StudentLabDTO
      T(n) =1 + 1 + Suma de la 1 la len(student_lab) din 1
            =1 + 1 + 8( 1 + 1 + 1 + .... + 1) de n ori
      complexitatea de timp este O(n) in cel mai rau caz, cat si in cel mai favorabil
      """
      student_lab = self.__student_lab_repo.getAll()
      list = []
      for item in student_lab:
            student_lab1 = item.getId()
            student = item.get_student_id()
            lab = item.get_lab_id()
            grade = item.get_grade()
            s = self.__student_repo.findById(student)
            l = self.__lab_repo.findById(lab)
            dto = LabStudentAssembler.create_lab_student_dto(student_lab1,s,l,grade)
            list.append(dto)
      return list

    def assignLab(self, student_lab_id, student_id , lab_number, lab_problem, grade):
        """
        assign lab method care primeste student_lab id, id-ul studentului si id-ul labului, impreuna cu nota
        si creeaza un obiect StudentLab pe care il salveaza in memorie dupa ce ne-am asigurat ca obiectul
        este in regula
        """
        lab_id = int(str(lab_number) + str(lab_problem))
        student_lab = StudentLab(student_lab_id, student_id, lab_id, grade)
        self.__student_repo.findById(student_id)
        self.__lab_repo.findById(lab_id)
        self.__student_lab_repo.save(student_lab)
        return student_lab

    """
    def sort_by_name(self, list):
        metoda care sorteaza lista dupa nume
        for i in range(0, len(list)-1):
            for j in range(i+1,len(list)):
                if list[i].getName() > list[j].getName():
                    aux = list[i]
                    list[i] = list[j]
                    list[j] = aux
    def sort_by_grade(self, list):
        metoda care sorteaza lista dupa nota
        for i in range(0, len(list)-1):
            for j in range(i+1,len(list)):
                if list[i].getGrade() > list[j].getGrade():
                    aux = list[i]
                    list[i] = list[j]
                    list[j] = aux
    """

    def students_and_grades_sorted_by_name(self, num, prblm):
        """
        students sorted by name method care primeste doi parametrii num si prblm si creeaza id-ul unui lab
        dupa care creeaza o lista de obiecte de forma ceruta in functie de id-ul student_lab, de id-ul studentului
        si de id-ul labului si apeleaza functia de sort dupa nume
        """
        id = int(str(num)+str(prblm))
        students = self.__student_lab_repo.getAll()
        list = []
        listDTO = []
        for item in students:
            if item.get_lab_id() == id:
                list.append(item)
        for item in list:
            student_lab = item.getId()
            student = item.get_student_id()
            lab = item.get_lab_id()
            grade = item.get_grade()
            s = self.__student_repo.findById(student)
            l = self.__lab_repo.findById(lab)
            dto = LabStudentAssembler.create_lab_student_dto(student_lab, s, l, grade)
            listDTO.append(dto)
        Sorting.sort(listDTO, key = lambda x:x.getName(), algorithm = Algorithm.MERGE_SORT)
        return listDTO

    def students_and_grades_sorted_by_grade(self, num, prblm):
        """
        students sorted by grade method care primeste doi parametrii num si prblm si creeaza id-ul unui lab
        dupa care creeaza o lista de obiecte de forma ceruta in functie de id-ul student_lab, de id-ul studentului
        si de id-ul labului si apeleaza functia de sort dupa nota
        """
        id = int(str(num) + str(prblm))
        students = self.__student_lab_repo.getAll()
        """
        for item in students:
            if item.get_lab_id() == id:
                list.append(item)
        """
        list = self.listCreatorRecursiv(students,[],id,0)
        """
        for item in list:
            student_lab = item.getId()
            student_lab.txt = item.get_student_id()
            lab = item.get_lab_id()
            grade = item.get_grade()
            s = self.__student_repo.findById(student_lab.txt)
            l = self.__lab_repo.findById(lab)
            dto = LabStudentAssembler.create_lab_student_dto(student_lab, s, l, grade)
            listDTO.append(dto)
        """
        listDTO = self.DTOLabCreatorRecursiv(list,[],0)
        Sorting.sort(listDTO, key=lambda x:x.getGrade(), algorithm=Algorithm.BINGO_SORT)
        return listDTO

    def listCreatorRecursiv(self, liststart, listfinish, id, index):
        if index == len(liststart):
            return listfinish
        else:
            if liststart[index].get_lab_id() == id:
                listfinish.append(liststart[index])
            return self.listCreatorRecursiv(liststart,listfinish,id,index+1)


    def DTOLabCreatorRecursiv(self, liststart, listfinish, index):
        if index == len(liststart):
            return listfinish
        else:
            student_lab = liststart[index].getId()
            student = liststart[index].get_student_id()
            lab = liststart[index].get_lab_id()
            grade = liststart[index].get_grade()
            s = self.__student_repo.findById(student)
            l = self.__lab_repo.findById(lab)
            dto = LabStudentAssembler.create_lab_student_dto(student_lab, s, l, grade)
            listfinish.append(dto)
            return self.DTOLabCreatorRecursiv(liststart,listfinish,index + 1)

    def first_20_percent(self):
        """
        first 20 percent method care calculeaza primele 20% de laboratoare la care au toti studentii media peste 5
        """
        aux = []
        listIdAvg, listAvg = self.average_grade_at_all_students()
        listIdUnique = []
        student_lab = self.__student_lab_repo.getAll()
        nr = 0
        for item in student_lab:
            lab = item.get_lab_id()
            student = item.get_student_id()
            if lab in listIdAvg and lab not in listIdUnique:
                nr = nr + 1
                l = self.__lab_repo.findById(lab)
                dto = LabAssembler.create_lab_dto(nr, l,listAvg[student-1])
                aux.append(dto)
                listIdUnique.append(lab)
        aux1 = []
        x = len(aux) // 5
        for i in range(0, x):
            aux1.append(aux[i])
        return aux1

    def average_grade_at_all_labs(self):
        """
        average grade method care calculeaza media notelor unui student_lab.txt dupa id si le pune intr-o lista cu pair-uri
        metoda asigura faptul ca un student_lab.txt este inserat o singura o data in lista finala
        """
        student_lab = self.__student_lab_repo.getAll()
        studentsId = []
        # Lista cu id-urile unice ale studentilor
        for item in student_lab:
            id_curent = item.get_student_id()
            ok = True
            if id_curent in studentsId:
                ok = False
            if ok==True:
                studentsId.append(id_curent)
        studentsIdAvg = []
        studentsAvg = []
        # 2 liste cu id-urile studentilor si media lor la toate materiile
        for id in studentsId:
            suma = 0
            nr = 0
            for j in student_lab:
                if id == j.get_student_id():
                    suma = suma + j.get_grade()
                    nr = nr + 1
            studentsIdAvg.append(id)
            studentsAvg.append(suma/nr)
        studentsIdAvg1 = []
        studentsAvg1 = []
        # eliminarea studentilor care au media peste 5
        for i in range(0,len(studentsIdAvg)):
            if studentsAvg[i]<5:
                studentsIdAvg1.append(studentsIdAvg[i])
                studentsAvg1.append(studentsAvg[i])
        return studentsIdAvg1, studentsAvg1

    def average_grade_at_all_students(self):
        """
        functie copie dupa average grade at all students doar ca pt laburi
        """
        student_lab = self.__student_lab_repo.getAll()
        labId = []
        # Lista cu id-urile unice ale laburilor
        for item in student_lab:
            id_curent = item.get_lab_id()
            ok = True
            if id_curent in labId:
                ok = False
            if ok == True:
                labId.append(id_curent)
        labIdAvg = []
        labAvg = []
        # 2 liste cu id-urile laburile si media studentilor la lab
        for id in labId:
            suma = 0
            nr = 0
            for j in student_lab:
                if id == j.get_lab_id():
                    suma = suma + j.get_grade()
                    nr = nr + 1
            labIdAvg.append(id)
            labAvg.append(suma / nr)
        labIdAvg1 = []
        labAvg1 = []
        # eliminarea laburilor care au media peste 5
        for i in range(0, len(labIdAvg)):
            if labAvg[i] < 5:
                labIdAvg1.append(labIdAvg[i])
                labAvg1.append(labAvg[i])
        return labIdAvg1, labAvg1

    def list_with_average_grade_below_5(self):
        """
        list with average grade below 5 method care creeaza un obiect dto de forma id, nume student_lab.txt, grupa student_lab.txt si nota care este
        media de la toate laboratoarele a studentului, pentru studentii care au media sub 5
        """
        student_lab = self.__student_lab_repo.getAll()
        listIdAvg, listAvg = self.average_grade_at_all_labs()
        listIdUnique = []
        list = []
        for item in student_lab:
            student_lab1 = item.getId()
            student = item.get_student_id()
            if student in listIdAvg and student not in listIdUnique:
                grade = listAvg[student-1]
                s = self.__student_repo.findById(student)
                dto = StudentAssembler.create_student_dto(student_lab1, s, grade)
                listIdUnique.append(student)
                list.append(dto)
        return list

class StudentLabControllerTestCase(unittest.TestCase):
    """
    clasa de teste pentru clasa student_lab.txt lab controller
    """
    def setUp(self):
        self.__lab_repo = LabRepository()
        lab1 = Laborator(1,2,"vectori","12.12.2023")
        lab2 = Laborator(1,3,"matrici","15.12.2023")
        self.__lab_repo.save(lab1)
        self.__lab_repo.save(lab2)
        self.__lab_controller = LabController(self.__lab_repo,LabValidator())


        self.__student_repo = StudentRepository()
        student1 = Student(1,"George",211)
        student2 = Student(2,"David",212)
        student3 = Student(3,"Mihai",218)
        self.__student_repo.save(student1)
        self.__student_repo.save(student2)
        self.__student_repo.save(student3)
        self.__student_controller = StudentController(self.__student_repo, StudentValidator())

        self.__student_lab_repo = StudentLabRepository()
        sl1 = StudentLab(1, student1.getId(), lab2.getId(), 3)
        sl2 = StudentLab(2, student2.getId(), lab2.getId(), 6)
        sl3 = StudentLab(3, student3.getId(), lab1.getId(), 5)
        self.__student_lab_repo.save(sl1)
        self.__student_lab_repo.save(sl2)
        self.__student_lab_repo.save(sl3)
        self.__student_lab_controller = StudentLabController(self.__student_repo, self.__lab_repo, self.__student_lab_repo, StudentLabValidator)

    def test_assignLab(self):
        s2l1 = self.__student_lab_controller.assignLab(4,2,1,2,8)
        assert s2l1.getId() == 4
        assert s2l1.get_student_id() == 2
        assert s2l1.get_lab_id() == 12
        assert s2l1.get_grade() == 8

        s1l1 = self.__student_lab_controller.assignLab(5,1,1,3,7)
        assert s1l1.getId() == 5
        assert s1l1.get_student_id() == 1
        assert s1l1.get_lab_id() == 13
        assert s1l1.get_grade() == 7

        try:
            self.__student_lab_controller.assignLab(1,3,1,3,5)
            assert False
        except RepositoryError:
            assert True

    def test_printStudentlab(self):
        list = self.__student_lab_controller.printStudentLab()

        assert len(list) == 3

        assert list[0].getId() == 1
        assert list[0].getName() == "George"
        assert list[0].getGrupa() == 211
        assert list[0].getDesc() == "matrici"
        assert list[0].getDeadline() == "15.12.2023"
        assert list[0].getGrade() == 3

        assert list[1].getId() == 2
        assert list[1].getName() == "David"
        assert list[1].getDesc() == "matrici"

    def test_students_and_grades_sorted_by_name(self):
        list = self.__student_lab_controller.students_and_grades_sorted_by_name(1,3)

        assert len(list) == 2

        assert list[0].getId() == 2
        assert list[0].getName() == "David"
        assert list[0].getGrupa() == 212
        assert list[0].getDesc() == "matrici"
        assert list[0].getDeadline() == "15.12.2023"
        assert list[0].getGrade() == 6

        assert list[1].getId() == 1
        assert list[1].getName() == "George"
        assert list[1].getGrupa() == 211
        assert list[1].getDesc() == "matrici"
        assert list[1].getDeadline() == "15.12.2023"
        assert list[1].getGrade() == 3

    def test_students_and_grades_sorted_by_grade(self):
        student4 = Student(4,"Marius", 215)
        self.__student_repo.save(student4)
        sl4 = StudentLab(6,student4.getId(),12, 3)
        self.__student_lab_repo.save(sl4)
        list = self.__student_lab_controller.students_and_grades_sorted_by_grade(1, 2)

        assert len(list) == 2

        assert list[0].getId() == 6
        assert list[0].getName() == "Marius"
        assert list[0].getGrupa() == 215
        assert list[0].getDesc() == "vectori"
        assert list[0].getDeadline() == "12.12.2023"
        assert list[0].getGrade() == 3

        assert list[1].getId() == 3
        assert list[1].getName() == "Mihai"
        assert list[1].getGrupa() == 218
        assert list[1].getDesc() == "vectori"
        assert list[1].getDeadline() == "12.12.2023"
        assert list[1].getGrade() == 5

    def test_average_grade_at_all_labs(self):
        sl4 = StudentLab(4,1,12,4)
        self.__student_lab_repo.save(sl4)
        sl5 = StudentLab(5,2,12,1)
        self.__student_lab_repo.save(sl5)
        sl6 = StudentLab(6,3,13,7)
        self.__student_lab_repo.save(sl6)

        studentsIdAvg, studentsAvg = self.__student_lab_controller.average_grade_at_all_labs()

        assert len(studentsIdAvg) == 2
        assert studentsIdAvg == [1,2]
        assert studentsAvg == [3.5,3.5]

        lab3 = Laborator(2,1,"oop","1.2.2024")
        self.__lab_repo.save(lab3)
        sl7 = StudentLab(7,2,21,10)
        self.__student_lab_repo.save(sl7)

        studentsIdAvg1, studentsAvg1 = self.__student_lab_controller.average_grade_at_all_labs()

        assert len(studentsIdAvg1) == 1
        assert studentsIdAvg1 == [1]
        assert studentsAvg1 == [3.5]

    def test_list_with_average_grade_below_5(self):
        sl4 = StudentLab(4, 1, 12, 4)
        self.__student_lab_repo.save(sl4)
        sl5 = StudentLab(5, 2, 12, 1)
        self.__student_lab_repo.save(sl5)
        sl6 = StudentLab(6, 3, 13, 7)
        self.__student_lab_repo.save(sl6)

        list = self.__student_lab_controller.list_with_average_grade_below_5()

        assert len(list) == 2

        assert list[0].getId() == 1
        assert list[0].getNume() == "George"
        assert list[0].getGrupa() == 211
        assert list[0].getNota() == 3.5

        assert list[1].getId() == 2
        assert list[1].getNume() == "David"
        assert list[1].getGrupa() == 212
        assert list[1].getNota() == 3.5

    def test_first_20_percent(self):
        lab3 = Laborator(2,1,"oop","1.2.2024")
        lab4 = Laborator(2,2,"dsa","2.1.2024")
        lab5 = Laborator(3,1,"matrici","1.4.2024")
        self.__lab_repo.save(lab3)
        self.__lab_repo.save(lab4)
        self.__lab_repo.save(lab5)
        sl4 = StudentLab(4,1,12,2)
        self.__student_lab_repo.save(sl4)
        sl5 = StudentLab(5,2,lab3.getId(),3)
        self.__student_lab_repo.save(sl5)
        sl6 = StudentLab(6,3,lab3.getId(),2)
        self.__student_lab_repo.save(sl6)
        sl7 = StudentLab(7, 1, lab4.getId(), 1)
        self.__student_lab_repo.save(sl7)
        sl8 = StudentLab(8, 2, lab4.getId(), 2)
        self.__student_lab_repo.save(sl8)
        sl9 = StudentLab(9, 2, lab5.getId(), 3)
        self.__student_lab_repo.save(sl9)
        sl10 = StudentLab(10, 3, lab5.getId(), 2)
        self.__student_lab_repo.save(sl10)

        list = self.__student_lab_controller.first_20_percent()

        assert len(list) == 1
        assert list[0].getId() == 1
        assert list[0].getNumber() == 1
        assert list[0].getProblem() == 3
        assert list[0].getDesc() == "matrici"
        assert list[0].getDeadline() == "15.12.2023"
        assert list[0].getGrade() == 4.5

    def test_listCreatorRecursiv(self):
        student4 = Student(4, "Marius", 215)
        self.__student_repo.save(student4)
        sl4 = StudentLab(6, student4.getId(), 12, 3)
        self.__student_lab_repo.save(sl4)
        list = self.__student_lab_repo.getAll()
        result = self.__student_lab_controller.listCreatorRecursiv(list,[],12,0)
        assert len(result) == 2

    def test_DTOLabCreatorRecursiv(self):
        student4 = Student(4, "Marius", 215)
        self.__student_repo.save(student4)
        sl4 = StudentLab(6, student4.getId(), 12, 3)
        self.__student_lab_repo.save(sl4)
        list = self.__student_lab_repo.getAll()
        result = self.__student_lab_controller.DTOLabCreatorRecursiv(list, [], 0)
        assert len(result) == 4

    def test_BingoSort(self):

        stud1 = Student(1, "David", 211)
        stud2 = Student(2, "George", 212)
        stud3 = Student(3, "Mihai",215)
        stud4 = Student(4, "Marius", 217)

        l = [stud3, stud2, stud1, stud4]
        Sorting.sort(l, key=lambda x: x.getNume(),algorithm = Algorithm.BINGO_SORT)
        assert (l == [stud1, stud2, stud4, stud3])

        l = [stud3, stud2, stud1, stud4]
        Sorting.sort(l, key=lambda x: x.getGrupa(),reverse = True,algorithm = Algorithm.BINGO_SORT)
        assert (l == [stud4, stud3, stud2, stud1])

        l = [stud3, stud2, stud1, stud4]
        Sorting.sort(l, key=lambda x: x.getGrupa(),algorithm = Algorithm.BINGO_SORT)
        assert (l == [stud1, stud2, stud3, stud4])


    def test_MergeSort(self):
        l = [2, 1, 3]
        Sorting.sort(l, algorithm = Algorithm.MERGE_SORT)
        assert (l == [1, 2, 3])

        Sorting.sort(l, reverse=True,algorithm = Algorithm.MERGE_SORT)
        assert (l == [3, 2, 1])

        l = [2, 1, 2, 3, 1]
        Sorting.sort(l,algorithm = Algorithm.MERGE_SORT)
        assert l == [1, 1, 2, 2, 3]

        Sorting.sort(l, reverse=True,algorithm = Algorithm.MERGE_SORT)
        assert l == [3, 2, 2, 1, 1]

        stud1 = Student(1, "David", 211)
        stud2 = Student(2, "George", 212)
        stud3 = Student(3, "Mihai",215)
        stud4 = Student(4, "Marius", 217)

        l = [stud3, stud2, stud1, stud4]
        Sorting.sort(l, key=lambda x: x.getNume(),algorithm = Algorithm.MERGE_SORT)
        assert (l == [stud1, stud2, stud4, stud3])

        l = [stud3, stud2, stud1, stud4]
        Sorting.sort(l, key=lambda x: x.getGrupa(), reverse=True,algorithm = Algorithm.MERGE_SORT)
        assert (l == [stud4, stud3, stud2, stud1])

        l = [stud3, stud2, stud1, stud4]
        Sorting.sort(l, key=lambda x: x.getGrupa(),algorithm = Algorithm.MERGE_SORT)
        assert (l == [stud1, stud2, stud3, stud4])

        l = [stud3, stud2, stud1, stud4]
        Sorting.sort(l, key=lambda x: (x.getNume(), x.getGrupa()), algorithm = Algorithm.MERGE_SORT)
        assert (l == [stud1, stud2, stud4, stud3])

    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(StudentLabControllerTestCase))
        return suite