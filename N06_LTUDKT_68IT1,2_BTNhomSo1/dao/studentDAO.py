
from model import Student
from db.dbconnect import get_connection


class StudentDAO:
    def __init__(self):
        pass

    def insert(self, student):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO student (student_id, name, birthday, department, type) VALUES (%s, %s, %s, %s, %s)"
            values = (student.get_student_id(), student.get_name(), student.get_birthday(), student.get_department(), student.get_type())
            cursor.execute(sql, values)
            conn.commit()
            if (student.get_type() == "Regular"):
                sql = "INSERT INTO regularstudent (student_id, GPA, credit) VALUES (%s, %s, %s)"
                values = (student.get_student_id(), 0, 0)
                cursor.execute(sql, values)
                conn.commit()
            elif (student.get_type() == "InService"):
                sql = "INSERT INTO inservicestudent (student_id, scores, job) VALUES (%s, %s, %s)"
                values = (student.get_student_id(), 0, None)
                cursor.execute(sql, values)
                conn.commit()
        except Exception as e:
            print("Error during insert:", e)
        finally:
            cursor.close()
            conn.close()

    def update(self, student_id, updated_student):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = "UPDATE student SET name = %s, birthday = %s, department = %s WHERE student_id = %s"
            values = (updated_student[0], updated_student[1], updated_student[2],  student_id)
            cursor.execute(sql, values)
            conn.commit()

            if (updated_student[3] == "Regular"):
                sql = "UPDATE regularstudent SET GPA = %s, credit = %s WHERE student_id = %s"
                values = (updated_student[5], updated_student[6], student_id)
                cursor.execute(sql, values)
                conn.commit()
            elif (updated_student[3] == "InService"):
                sql = "UPDATE inservicestudent SET scores = %s, job = %s WHERE student_id = %s"
                values = (updated_student[6], updated_student[7], student_id)
                cursor.execute(sql, values)
                conn.commit()

            
        except Exception as e:
            print("Error during update:", e)
        finally:
            cursor.close()
            conn.close()

    def delete(self, student_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM student WHERE student_id = %s"
            cursor.execute(sql, (student_id,))
            conn.commit()
        except Exception as e:
            print("Error during delete:", e)
        finally:
            cursor.close()
            conn.close()
    def selectAll(self):
        list_student = []
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            result = cursor.fetchall()

            for row in result:
                student = Student.Student(row[0], row[1], row[2], row[3], row[4])
                list_student.append(student)

        except Exception as e:
            print("Error during query:", e)
        
        return list_student
    

    def selectById(self, student_id):
        # Lấy tất cả thông tin của 1 sinh viên
        conn = get_connection()
        student = None
        try:
            cursor = conn.cursor()
            sql = "SELECT s.student_id, s.name, s.birthday, s.department, s.type, r.gpa, r.credit, i.scores, i.job FROM student s LEFT JOIN regularstudent r ON s.student_id = r.student_id LEFT JOIN inservicestudent i ON s.student_id = i.student_id where s.student_id = %s;"
            cursor.execute(sql, (student_id,))
            result = cursor.fetchone()

            if result:
                return [result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]]

        except Exception as e:
            print("Error during query:", e)
        
        return student

    def search_by_id(self, student_id):
        conn = get_connection()
        list_student = []
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM student WHERE LOWER(student_id) LIKE LOWER(%s)"  
            cursor.execute(sql, ('%' + student_id + '%',))
            result = cursor.fetchall()
            
            for row in result:
                student = Student.Student(row[0], row[1], row[2], row[3], row[4])
                list_student.append(student)
        except Exception as e:
            print("Error during search by ID:", e)

        return list_student
    
    def search_by_name(self, name):
        conn = get_connection()
        list_student = []
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM student WHERE LOWER(name) LIKE LOWER(%s)"  
            cursor.execute(sql, ('%' + name + '%',))
            result = cursor.fetchall()
            
            for row in result:
                
                student = Student.Student(row[0], row[1], row[2], row[3], row[4])
                list_student.append(student)
        except Exception as e:
            print("Error during search by name:", e)

        return list_student
    
    def search_by_department(self, department):
        conn = get_connection()
        list_student = []
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM student WHERE LOWER(department) LIKE LOWER(%s)"  
            cursor.execute(sql, ('%' + department + '%',))
            result = cursor.fetchall()
            
            for row in result:
                student = Student.Student(row[0], row[1], row[2], row[3], row[4])
                list_student.append(student)
        except Exception as e:
            print("Error during search by department:", e)

        return list_student
    
    def search_by_department_and_name(self, department, name):
        conn = get_connection()
        list_student = []
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM student WHERE LOWER(department) LIKE LOWER(%s) AND LOWER(name) LIKE LOWER(%s)"  
            cursor.execute(sql, ('%' + department + '%', '%' + name + '%'))
            result = cursor.fetchall()
            
            for row in result:
                student = Student.Student(row[0], row[1], row[2], row[3], row[4])
                list_student.append(student)
        except Exception as e:
            print("Error during search by department and name:", e)

        return list_student