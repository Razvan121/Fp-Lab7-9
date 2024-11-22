from UI.Console import console, manageSubject, manageStudent, Statistics


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

    def random_stude(self):
        x = int(input("Enter number of entities: "))
        self.__srv_students.student_random(x)
            

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
        while True:
            try:
                id_student = int(input("Enter ID for student: "))
                id_discipline = int(input("Enter ID for discipline: "))
                grade = int(input("Enter grade: "))
                if grade < 0 or grade > 10:
                    raise ValueError("Grade must be between 0 and 10")

                fgrade = self.__srv_grade.add_gradesrv(id_student, id_discipline, grade)
                student = self.__srv_students.search_student(id_student)
                discipline = self.__srv_discipline.search_discipline(id_discipline)
                print(f"Student {student.get_name()} has {grade} grade at {discipline.get_name()}")
                break
            except ValueError as e:
                print(f"Error: {e}")
                print("Please try again.")

    def ui_print_all_grades(self):
        student_grades = self.__srv_grade.get_all_gradesrv()

        # for student, disciplines in student_grades.items():
        #     print(f"Grades for {student.get_name()}:")
        #     for discipline, grades in disciplines.items():
        #         grade_values = [grade.get_grade() for grade in grades]
        #         print(f"  {discipline.get_name()}: {', '.join(map(str, grade_values))}")

        for student_id, disciplines in student_grades.items():
            student = self.__srv_students.search_student(student_id)  
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

            if options[0] == "random":
                self.random_stude()

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

            if options[0] == "delete" and options[1] == "grade":
                ID_student = int(input("Enter ID for student: "))
                ID_discipline = int(input("Enter ID for discipline: "))
                Grade = int(input("Enter grade: "))
                self.__srv_grade.delete_gradesrv(ID_student, ID_discipline,Grade)

            if options[0] == "statistics":
                Statistics()

            if options[0] == "sort" and options[1] == "grades" :
                id_discipline = int(input("Enter ID for discipline: "))
                sorted_list = self.__srv_grade.get_sorted_students_with_grades(id_discipline)
                for student, grades in sorted_list:
                    grade_values = [grade.get_grade() for grade in grades]
                    print(f"Student {student.get_name()} has {', '.join(map(str, grade_values))} grades")

            if options[0] == "average" :
                id_student = int(input("Enter ID for student: "))
                average = self.__srv_grade.get_average_grade_for_student(id_student)
                print(f"Average grade for student {id_student} is {average}")


            if options[0] == "sort" and options[1] == "average":
                for student,avg in self.__srv_grade.sort_grades_by_student():
                    print(f"Student {student.get_name()} has average grade {avg}")



