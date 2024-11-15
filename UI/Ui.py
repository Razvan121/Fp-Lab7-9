from UI.Console import console, manageSubject, manageStudent


class Interface():

    def __init__(self, srv_students, srv_discipline, srv_grade):
        self.__srv_students = srv_students
        self.__srv_discipline = srv_discipline
        self.__srv_grade = srv_grade

    def ui_add_student(self):
        while True:
            try:
                ID = int(input("Enter ID for student: "))
                if ID < 0:
                    raise ValueError("ID cannot be negative")

                name = input("Enter name for student: ")
                options = name.split()
                if len(options) < 2 or not name.strip():
                    raise ValueError("Student name cannot be empty or cannot be less than 2 words")

                student = self.__srv_students.addstudent(ID, name)
                print(f"Student details: {student}")

                break

            except ValueError as e:
                print(f"Error: {e}")

    #
    # def ui_add_discipline(self):
    #         ID = int(input("Enter ID for discipline: "))
    #         name = input("Enter name for discipline: ")
    #         teacher = input("Enter teacher for discipline: ")
    #         subject = self.__srv_discipline.adddiscipline(ID,name,teacher)
    #         print(f"Discipline details: {subject}")

    def ui_add_discipline(self):
        while True:
            try:
                ID = int(input("Enter ID for discipline: "))
                if ID < 0:
                    raise ValueError("ID cannot be negative")

                name = input("Enter name for discipline: ")
                if name == "":
                    raise ValueError("Discipline name cannot be empty")

                teacher = input("Enter teacher for discipline: ")
                options = teacher.split()
                if not teacher.strip() or len(options) < 2:
                    raise ValueError("Discipline teacher cannot be or cannot be less than 2 words")

                subject = self.__srv_discipline.adddiscipline(ID, name, teacher)
                print(f"Discipline details: {subject}")
                break
            except ValueError as e:
                print(f"Error: {e}")
                print("Please try again.")

    def ui_add_grade(self):
        id_student = int(input("Enter ID for student: "))
        id_discipline = int(input("Enter ID for discipline: "))
        grade = int(input("Enter grade: "))
        #
        # student = self.__srv_students.search_student(id_student)
        # discipline = self.__srv_discipline.search_discipline(id_discipline)
        #
        # fgrade = self.__srv_grade.add_gradesrv(student, id_discipline, grade)

        try:
            fgrade = self.__srv_grade.add_gradesrv(id_student, id_discipline, grade)
            student = self.__srv_students.search_student(id_student)
            discipline = self.__srv_discipline.search_discipline(id_discipline)
            print(f"Student {student.get_name()} has {grade} grade at {discipline.get_name()}")
        except ValueError as e:
            print(f"Error: {e}")

    def ui_print_all_grades(self):
        student_grades = self.__srv_grade.get_all_gradesrv()

        # for student, disciplines in student_grades.items():
        #     print(f"Grades for {student.get_name()}:")
        #     for discipline, grades in disciplines.items():
        #         grade_values = [grade.get_grade() for grade in grades]
        #         print(f"  {discipline.get_name()}: {', '.join(map(str, grade_values))}")

        for student_id, disciplines in student_grades.items():
            student = self.__srv_students.search_student(student_id)  # Retrieve student object
            print(f"Grades for {student.get_name()}:")
            for discipline_id, grades in disciplines.items():
                discipline = self.__srv_discipline.search_discipline(discipline_id)
                grade_values = [grade.get_grade() for grade in grades]
                print(f"  {discipline.get_name()}: {', '.join(map(str, grade_values))}")

    def run(self):

        console()

        while True:
            command = input("Enter command: ")
            options = command.lower().split()

            if command == "":
                continue

            if command == "help":
                console()

            if command == "exit" or options[0] == "exit":
                break

            #      STUDENT

            if options[0] == "manage" and options[1] == "students":
                manageStudent()

            if options[0] == "add" and options[1] == "student":
                self.ui_add_student()

            if options[0] == "print" and (options[1] == "students" or options[1] == "all"):
                lst_students = self.__srv_students.get_all_students()
                # for stud in lst_students:
                #     print(stud)
                for stud in lst_students:
                    print(f" Student: {stud}")

            if options[0] == "delete" and options[1] == "student":

                if len(options) == 2:

                    ID = int(input("Enter ID for student: "))
                    self.__srv_students.delete_student(ID)
                elif len(options) == 3:

                    self.__srv_students.delete_student(options[2])

            if options[0] == "modify" and options[1] == "student":

                if len(options) == 2:
                    ID = int(input("Enter ID for student: "))
                    name = input("Enter name for student: ")
                    self.__srv_students.modify_student(ID, name)

            if options[0] == "search" and options[1] == "student":
                ID = int(input("Enter ID for student: "))
                student = self.__srv_students.search_student(ID)
                print(f"Student details: {student}")

            #    DISCIPLINE

            if options[0] == "manage" and options[1] == "disciplines":
                manageSubject()

            if options[0] == "add" and options[1] == "discipline":
                self.ui_add_discipline()

            if options[0] == "print" and options[1] == "disciplines":

                lst_disciplines = self.__srv_discipline.get_all_disciplines()
                # for dis in lst_disciplines:
                #     print(dis)
                for dis_id, dis in lst_disciplines.items():
                    print(f"ID: {dis_id}, Subject: {dis}")

            if options[0] == "delete" and options[1] == "discipline":

                if len(options) == 2:

                    ID = int(input("Enter ID for subject: "))
                    self.__srv_discipline.delete_discipline(ID)

                elif len(options) == 3:

                    self.__srv_discipline.delete_discipline(options[2])

            if options[0] == "modify" and options[1] == "discipline":

                if len(options) == 2:

                    ID = int(input("Enter ID for subject that you want to modify: "))
                    command = input("Do you want to modify name or teacher: ")

                    if command == "name":

                        name = input("Enter name for subject: ")
                        self.__srv_discipline.modify_discipline_name(ID, name)

                    elif command == "teacher":

                        teacher = input("Enter teacher for subject: ")
                        self.__srv_discipline.modify_discipline_teacher(ID, teacher)


                elif len(options) == 3:

                    if options[2] == "name":

                        name = input("Enter name for subject: ")
                        ID = int(input("Enter ID for subject that you want to modify: "))
                        self.__srv_discipline.modify_discipline_name(ID, name)

                    elif options[2] == "teacher":

                        teacher = input("Enter teacher for subject: ")
                        ID = int(input("Enter ID for subject that you want to modify: "))
                        self.__srv_discipline.modify_discipline_teacher(ID, teacher)

            if options[0] == "search" and options[1] == "discipline":
                ID = int(input("Enter ID for subject: "))
                subject = self.__srv_discipline.search_discipline(ID)
                print(f"Subject details: {subject}")

            # Assign grade

            if options[0] == "add" and options[1] == "grade":
                self.ui_add_grade()

            if options[0] == "print" and options[1] == "grades":
                self.ui_print_all_grades()


