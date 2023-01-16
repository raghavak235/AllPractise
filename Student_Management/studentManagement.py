# Student Management: A simple project to display, search, add and delete new students.

class studentMangemant:
    student_details = {}

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def displayALL(cls):
        for student in cls.student_details:
            print(student, cls.student_details.get(student))

    def addStudent(self):
        studentMangemant.student_details[self.id] = self.name

    def deleteStudent(self, id):
        del studentMangemant.student_details[id]

    @classmethod
    def search(cls, id):
        if id in cls.student_details:
            print(cls.student_details.get(id))
        print('Requested ID not found')


sm = studentMangemant(1, 'rahul')
sm.addStudent()


sm = studentMangemant(2, 'raju')
sm.addStudent()
sm.displayALL()
