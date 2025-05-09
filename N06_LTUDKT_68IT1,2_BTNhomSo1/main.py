import sys
from dao.studentDAO import StudentDAO
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem



app = QtWidgets.QApplication(sys.argv)

model = QStandardItemModel()
model.setHorizontalHeaderLabels(["Id", "Name", "Birthday", "Department", "Type"])

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/finalgui.ui", self)
        self.tableStudent.setModel(model)
        self.tableStudent.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableStudent.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)  # Chọn cả dòng
        self.tableStudent.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)  # Không cho phép chỉnh sửa
        self.setWindowTitle("Main Window")
        self.loadData()


        self.addBtn.clicked.connect(self.openAddStudentForm)
        self.delBtn.clicked.connect(self.deleteStudent)
        self.editBtn.clicked.connect(self.editStudent)
        self.comboBox.currentIndexChanged.connect(self.loadData)
        self.search1Btn.clicked.connect(self.searchStudent1)
        self.search2Btn.clicked.connect(self.searchStudent2)

    def loadData(self):
        model.setRowCount(0)
        data = StudentDAO().selectAll()
        department = set()
        for student in data:
            department.add(student.get_department())
            row = [
                QStandardItem(str(student.get_student_id())),
                QStandardItem(student.get_name()),
                QStandardItem(student.get_birthday().strftime("%Y-%m-%d")),
                QStandardItem(student.get_department()),
                QStandardItem(student.get_type())
            ]
            if (self.comboBox.currentText() == "All" or
                self.comboBox.currentText() == student.get_type()):
                model.appendRow(row)

        self.comboKey2.clear()
        for x in department:
            self.comboKey2.addItem(x)
            

    def openAddStudentForm(self):
        from view.addNewStudentForm import AddNewStudentForm
        form = AddNewStudentForm()
        form.exec()
        self.loadData()

    def deleteStudent(self):
        index = self.tableStudent.currentIndex()
        if not index.isValid():
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a student to delete.")
            return
        if QtWidgets.QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this student?",
                                          QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No) == QtWidgets.QMessageBox.StandardButton.No:
            return
        student_id = model.item(index.row(), 0).text()
        
        from model.ManagerStudent import ManagerStudent
        manager = ManagerStudent()
        manager.delete_student(student_id)
        QtWidgets.QMessageBox.information(self, "Success", "Student deleted successfully.")
        self.loadData()

    def editStudent(self):
        index = self.tableStudent.currentIndex()
        if not index.isValid():
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a student to edit.")
            return
        
        if   model.item(index.row(), 4).text() ==  "InService":
            from view.editInService import EditInService
            form = EditInService(model.item(index.row(), 0).text())
            form.exec()
            self.loadData()
        elif model.item(index.row(), 4).text() == "Regular":
            from view.editRegular import EditRegular
            form = EditRegular(model.item(index.row(), 0).text())
            form.exec()
            self.loadData()

    def searchStudent1(self):
        key1 = self.comboKey1.currentText()
        key2 = self.txtKey1.text()
        from model.ManagerStudent import ManagerStudent
        manager = ManagerStudent()
        if key1 == "ID":
            ListStudent = manager.search_student_by_id(key2)
        elif key1 == "Name":
            ListStudent = manager.search_student_by_name(key2)
        elif key1 == "Department":
            ListStudent = manager.search_student_by_department(key2)
        
        model.setRowCount(0)
        for student in ListStudent:
            row = [
                QStandardItem(str(student.get_student_id())),
                QStandardItem(student.get_name()),
                QStandardItem(student.get_birthday().strftime("%Y-%m-%d")),
                QStandardItem(student.get_department()),
                QStandardItem(student.get_type())
            ]
            if (self.comboBox.currentText() == "All" or
                self.comboBox.currentText() == student.get_type()):
                model.appendRow(row)

    def searchStudent2(self):
        key1 = self.comboKey2.currentText()
        key2 = self.txtKey2.text()
        from model.ManagerStudent import ManagerStudent
        manager = ManagerStudent()
        ListStudent = manager.search_student_by_department_and_name(key1, key2)
        
        model.setRowCount(0)
        for student in ListStudent:
            row = [
                QStandardItem(str(student.get_student_id())),
                QStandardItem(student.get_name()),
                QStandardItem(student.get_birthday().strftime("%Y-%m-%d")),
                QStandardItem(student.get_department()),
                QStandardItem(student.get_type())
            ]
            if (self.comboBox.currentText() == "All" or
                self.comboBox.currentText() == student.get_type()):
                model.appendRow(row)



window = MainWindow()
window.show()
sys.exit(app.exec())
