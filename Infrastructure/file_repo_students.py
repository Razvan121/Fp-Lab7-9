from Domain.Student import Student
from Exceptions.Exceptions import RepoException, CorruptedFileException
from Infrastructure.Repostory_Student import repostory_students


class StudentRepoFile:

    def __init__(self,fileName):

        self.__fileName = fileName

    def __load_from_file(self):
        try:
            f = open(self.__fileName,'r')
        except IOError:
            raise CorruptedFileException("File Not Found")

        students = []
        lines = f.readlines()

        for line in lines:
            id_student,name = [token.strip() for token in line.split(',')]
            student = Student(int(id_student),name)
            students.append(student)

        f.close()
        return students

    def __save_to_file(self,students):
        with open(self.__fileName,'w') as file:
            for student in students:
                student_string = str(student.get_id()) + ',' + str(student.get_name()) +'\n'
                file.write(student_string)


    def search_student_by_ID(self,studentId):
        """
        Function that search a student with a given id
        :param studentId: The unique id of the student
        :return:The student with the given id
        """

        allStudents = self.__load_from_file()
        for student in allStudents:
            if student.get_id() == studentId:
                return student
        raise RepoException("Student Not Found")

    def add_student(self,newstudent):
        """
        Function that add a student to the repository
        :param newstudent: the student that will append in list
        :return:
        """

        allStudents = self.__load_from_file()
        for student in allStudents:
            if student.get_id() == newstudent.get_id():
                raise ValueError("Student Already Exists")
        allStudents.append(newstudent)
        self.__save_to_file(allStudents)


    def delete_student(self,studentId):
        """
        Function that remove a student from the repository
        :param studentId: The unique id of the student
        :return:
        """

        allStudents = self.__load_from_file()

        for i in range(len(allStudents)):
            if allStudents[i].get_id() == studentId:
                del allStudents[i]
                self.__save_to_file(allStudents)
                return
        raise RepoException("Student Not Found")

    def modify_student(self,studentId,name):
        """
        Function that update a student with the given name
        :param studentId: The unique id of the student
        :param name: The name that will be modified
        :return:
        """

        allStudents = self.__load_from_file()
        for student in allStudents:
            if student.get_id() == studentId:
                student.set_name(name)
                self.__save_to_file(allStudents)
                return
        raise RepoException("Student Not Found")


    def get_all_students(self):
        """
        Function that returns all the students in the repository
        :return:
        """
        return self.__load_from_file()









