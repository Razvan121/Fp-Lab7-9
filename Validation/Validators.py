
class Validator:

    def validate_student(self, students):

        error= []

        if int(students.get_id()) <0:
            error.append("Student ID cannot be negative")
        if students.get_name() == "" or len(students.get_name().split()) <2 :
            error.append("Student name cannot be empty")

        if len(error):
            raise ValueError(error)


    def validate_discipline(self, disciplines):

        error = []

        if int(disciplines.get_id()) <0:
            error.append("Discipline ID cannot be negative")
        if disciplines.get_name() == "" :
            error.append("Discipline name cannot be empty")
        if disciplines.get_teacher == "" or len(disciplines.get_teacher().split()) <2:
            error.append("Teacher name cannot be empty")


        if len(error):
            raise ValueError(error)







