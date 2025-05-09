from PyQt6 import QtWidgets, uic

from dao.studentDAO import StudentDAO
from model.ManagerStudent import ManagerStudent
class EditInService(QtWidgets.QDialog):
    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id
        uic.loadUi("view/editInService.ui", self)
        self.setWindowTitle("Edit In-Service Student")

        self.saveBtn.clicked.connect(self.editStudent)
        self.cancelBtn.clicked.connect(self.close)
        
        
        
        data = StudentDAO().selectById(student_id)
        self.txtId.setText(data[0])
        self.txtId.setReadOnly(True)
        self.txtName.setText(data[1])
        self.txtDob.setDate(data[2])
        self.txtDepartment.setText(data[3])
        self.spinnerScore.setValue(float(data[7]))
        self.txtJob.setText(data[8])
    
    def editStudent(self):
        
        manager = ManagerStudent()
        manager.edit_student(self.student_id, [self.txtName.text(), self.txtDob.date().toString("yyyy-MM-dd"), self.txtDepartment.text(), "In-Service", None, None, self.spinnerScore.value(), self.txtJob.text()])
        QtWidgets.QMessageBox.information(self, "Success", "Student information updated successfully.")
        self.close()