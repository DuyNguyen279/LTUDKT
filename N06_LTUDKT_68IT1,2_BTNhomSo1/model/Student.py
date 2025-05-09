class Student:
    def __init__(self, student_id, name, birthday, department, type):
        self.student_id = student_id
        self.name = name
        self.birthday = birthday
        self.department = department
        self.type = type
    
    def get_student_id(self):
        return self.student_id

    def set_student_id(self, student_id):
        self.student_id = student_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_birthday(self):
        return self.birthday

    def set_birthday(self, birthday):
        self.birthday = birthday

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

class RegularStudent(Student):
    def __init__(self, student_id, name, birthday, department, type, GPA, credit):
        super().__init__(student_id, name, birthday, department,type)
        self.GPA = GPA
        self.credit = credit

    def get_GPA(self):
        return self.GPA

    def set_GPA(self, GPA):
        self.GPA = GPA

    def get_credit(self):
        return self.credit

    def set_credit(self, credit):
        self.credit = credit

class InServiceStudent(Student):
    def __init__(self, student_id, name, birthday, department, type, scores, job):
        super().__init__(student_id, name, birthday, department, type)
        self.scores = scores
        self.job = job

    def get_scores(self):
        return self.scores

    def set_scores(self, scores):
        self.scores = scores

    def get_job(self):
        return self.job

    def set_job(self, job):
        self.job = job

