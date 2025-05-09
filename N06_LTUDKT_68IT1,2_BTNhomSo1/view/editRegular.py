from PyQt6 import QtWidgets, uic

from dao.studentDAO import StudentDAO
from model.ManagerStudent import ManagerStudent
class EditRegular(QtWidgets.QDialog):
    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id
        uic.loadUi("view/editRegular.ui", self)
        self.setWindowTitle("Edit Regular Student")
        self.saveBtn.clicked.connect(self.editStudent)
        self.cancelBtn.clicked.connect(self.close)
        
        
        data = StudentDAO().selectById(student_id)
        self.txtId.setText(data[0])
        self.txtId.setReadOnly(True)
        self.txtName.setText(data[1])
        self.txtDob.setDate(data[2]) 
        self.txtDepartment.setText(data[3])
        self.txtDepartment.setReadOnly(True)
        self.spinnerGpa.setValue(float(data[5]))
        self.spinnerCredits.setValue(int(data[6]))

    def editStudent(self):
        
        if QtWidgets.QMessageBox.question(self, "Edit Confirmation", "Are you sure you want to edit this student?", 
                                          QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No) == QtWidgets.QMessageBox.StandardButton.No:
            return
        manager = ManagerStudent()
        manager.edit_student(self.student_id, [self.txtName.text(), self.txtDob.date().toString("yyyy-MM-dd"), self.txtDepartment.text(), "In-Service", self.spinnerGpa.value(), self.spinnerCredits.value(), None, None])
        QtWidgets.QMessageBox.information(self, "Success", "Student information updated successfully.")
        self.close()
