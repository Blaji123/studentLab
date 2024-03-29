from domain.validator import ValidatorError
class Console:
    """
    clasa consola de unde se apeleaza meniurile aplicatiei
    """
    def __init__(self, student_controller, laborator_controller, student_lab_controller):
        self.__student_controller = student_controller
        self.__laborator_controller = laborator_controller
        self.__student_lab_controller = student_lab_controller

    def __printStudents(self):
        list = self.__student_controller.printStudents()
        if len(list) == 0:
            print("Nu exista niciun student_lab.txt")
        else:
            self.printStudentsRecursive(list,0)

    def printStudentsRecursive(self, s, i):
        if i < len(s):
            print(s[i])
            self.printStudentsRecursive(s, i + 1)

    def __printProblems(self):
        list = self.__laborator_controller.printProblems()
        if len(list) == 0:
            print("Nu exista nicio problema")
        else:
            for e in list:
                print(e)

    def __addStudents(self):
        try:
            id = int(input("Introduceti id-ul: "))
            name = input("Introduceti numele: ")
            grupa = int(input("Introduceti grupa: "))
            self.__student_controller.addStudent(id, name, grupa)
        except ValidatorError as se:
            print(se.getErrors())

    def __addProblems(self):
        try:
            num = int(input("Introduceti numarul laboratorului: "))
            prblm = int(input("Introduceti numarul problemei: "))
            desc = input("Introduceti descrierea: ")
            deadline = input("Introduceti deadline-ul: ")
            self.__laborator_controller.addProblema(num,prblm,desc,deadline)
        except ValidatorError as se:
            print(se.getErrors())

    def __deleteStudents(self):
        try:
            id = int(input("Introduceti id-ul: "))
            self.__student_controller.deleteStudent(id)
        except ValidatorError as se:
            print(se.getErrors())

    def __deleteProblems(self):
        try:
            num = int(input("Introduceti numarul laboratorului: "))
            prblm = int(input("Introduceti numarul problemei: "))
            self.__laborator_controller.deleteProblem(num, prblm)
        except ValidatorError as se:
            print(se.getErrors())

    def __changeStudents(self):
        try:
            id = int(input("Introduceti id-ul unui student_lab.txt existent: "))
            nume = input("Introduceti noul nume: ")
            grupa = int(input("Introduceti noua grupa: "))
            self.__student_controller.changeStudent(id, nume, grupa)
        except ValidatorError as se:
            print(se.getErrors())

    def __changeProblems(self):
        try:
            num = int(input("Introduceti numarul unui laborator existent : "))
            prblm = int(input("Introduceti numarul problemei laboratorului existent: "))
            desc = input("Introduceti descrierea: ")
            deadline = input("Introduceti deadline-ul: ")
            self.__laborator_controller.changeProblem(num,prblm,desc,deadline)
        except ValidatorError as se:
            print(se.getErrors())

    def __printStudentWithLabAndGrade(self):
        list = self.__student_lab_controller.printStudentLab()
        if len(list) == 0:
            print("Nu exista niciun student_lab.txt cu laboratorul asignat")
        else:
            for e in list:
                print(e)

    def __assignLab(self):
        try:
            student_lab_id = int(input("Introduceti id-ul studentului si labului: "))
            student_id = int(input("Introduceti id-ul studentului caruia vreti sa-i asignati labul: "))
            num = int(input("Introduceti numarul labului: "))
            prblm = int(input("Introduceti numarul problemei: "))
            grade = int(input("Introduceti nota: "))
            self.__student_lab_controller.assignLab(student_lab_id,student_id,num,prblm,grade)
        except ValidatorError as se:
            print(se.getErrors())

    def __searchStudent(self):
        try:
            id = int(input("Dati id-ul unui student_lab.txt: "))
            Student = self.__student_controller.searchStudent(id)
            print(Student)
        except ValidatorError as se:
            print(se.getErrors())

    def __searchProblem(self):
        try:
            num = int(input("Introduceti numarul unui laborator existent: "))
            prblm = int(input("Introduceti numarul problemei laboratorului existent: "))
            Lab = self.__laborator_controller.searchProblem(num, prblm)
            print(Lab)
        except ValidatorError as se:
            print(se.getErrors())

    def __generateRandomStudent(self):
        try:
            self.__student_controller.createRandomStudent()
        except ValidatorError as se:
            print(se.getErrors())

    def __generateRandomLab(self):
        try:
            self.__laborator_controller.createRandomLab()
        except ValidatorError as se:
            print(se.getErrors())

    def __students_and_grades_sorted_by_name(self):
        try:
            num = int(input("Introduceti numarul laboratorului: "))
            prblm = int(input("Introduceti numarul problemei: "))
            list = self.__student_lab_controller.students_and_grades_sorted_by_name(num, prblm)
            for e in list:
                print(e)
        except ValidatorError as se:
            print(se.getErrors())

    def __students_and_grades_sorted_by_grade(self):
        try:
            num = int(input("Introduceti numarul laboratorului: "))
            prblm = int(input("Introduceti numarul problemei: "))
            list = self.__student_lab_controller.students_and_grades_sorted_by_grade(num, prblm)
            for e in list:
                print(e)
        except ValidatorError as se:
            print(se.getErrors())

    def __students_with_average_grade_below_5(self):
        list = self.__student_lab_controller.list_with_average_grade_below_5()
        for e in list:
            print(e)

    def __first_20_percent_labs(self):
        list = self.__student_lab_controller.list_with_average_grade_below_5()
        list_labs = self.__student_lab_controller.first_20_percent()
        for e in list_labs:
            print(e)

    def __print_all_options(self):
        print("0. Exit\n"
              "1. Afisare studenti\n"
              "2. Afisare probleme\n"
              "3. Adaugare student_lab.txt\n"
              "4. Adaugare problema\n"
              "5. Stergere student_lab.txt\n"
              "6. Stergere problema\n"
              "7. Modificare student_lab.txt\n"
              "8. Modificare problema\n"
              "9. Asignare laborator unui student_lab.txt\n"
              "10. Cautare student_lab.txt by Id\n"
              "11. Cautare problema by Id\n"
              "12. Generate random student_lab.txt\n"
              "13. Generate random lab\n"
              "14. Print Students with assigned lab and grade\n"
              "15. Print Students and grades sorted by name\n"
              "16. Print Students and grades sorted by grade\n"
              "17. Print Students and grades with average score below 5 at all labs\n"
              "18. Print first 20 percent labs with average score below 5")

    def run(self):
        while True:
            self.__print_all_options()
            options = {1: self.__printStudents, 2: self.__printProblems, 3: self.__addStudents, 4: self.__addProblems,
                       5: self.__deleteStudents, 6: self.__deleteProblems, 7: self.__changeStudents, 8: self.__changeProblems,
                       9: self.__assignLab, 10: self.__searchStudent, 11: self.__searchProblem, 12: self.__generateRandomStudent,
                       13:self.__generateRandomLab, 14:self.__printStudentWithLabAndGrade, 15:self.__students_and_grades_sorted_by_name,
                       16:self.__students_and_grades_sorted_by_grade, 17:self.__students_with_average_grade_below_5,
                       18:self.__first_20_percent_labs}
            try:
                optiune = int(input("Dati optiunea: "))
                if optiune<0 or optiune>len(options):
                    raise ValueError
            except ValueError:
                print("Optiune gresita")
                return
            if optiune == 0:
                break
            options[optiune]()