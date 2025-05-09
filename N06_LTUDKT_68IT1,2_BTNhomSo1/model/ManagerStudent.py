class ManagerStudent:
    def __init__(self):
        pass

    def add_student(self, student):
        from dao.studentDAO import StudentDAO
        student_dao = StudentDAO()
        student_dao.insert(student)

    def edit_student(self, student_id, updated_student):
        from dao.studentDAO import StudentDAO
        student_dao = StudentDAO()
        student_dao.update(student_id, updated_student)

    def delete_student(self, student_id):
        from dao.studentDAO import StudentDAO
        student_dao = StudentDAO()
        student_dao.delete(student_id)

    def search_student_by_id(self, student_id):
        from dao.studentDAO import StudentDAO
        student_dao = StudentDAO()
        return student_dao.search_by_id(student_id)

    def search_student_by_name(self, name):
        from dao.studentDAO import StudentDAO
        student_dao = StudentDAO()
        return student_dao.search_by_name(name)

    def search_student_by_department(self, department):
        from dao.studentDAO import StudentDAO
        student_dao = StudentDAO()
        return student_dao.search_by_department(department)

    def search_student_by_department_and_name(self, department, name):
        from dao.studentDAO import StudentDAO
        student_dao = StudentDAO()
        return student_dao.search_by_department_and_name(department, name)
        