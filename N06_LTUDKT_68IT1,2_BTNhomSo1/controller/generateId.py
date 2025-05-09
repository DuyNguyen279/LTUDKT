class generateId:
    def __init__(self):
        pass
    def generate_id(self):
        from dao.studentDAO import StudentDAO
        from model.Student import Student
        student_dao = StudentDAO()
        data = student_dao.selectAll()
        if (len(data) == 0):
            return "SV1"
        i = len(data)
        check = 1
        while (check == 1):
            i+= 1
            for x in data:
                if (x.get_student_id() == "SV" + str(i)):
                    check = 0
            
            if (check == 0):
                check = 1
            else:
                return "SV" + str(i)
            
        