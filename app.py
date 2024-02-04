from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
import sys 

class Login(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/login.ui", self) # Load UI file for Login
        self.btn_login.clicked.connect(self.ShowMainPage) # Connect button to ShowPage function
        self.btn_creat.clicked.connect(self.ShowRegis) # Connect button to ShowPage function
    def ShowMainPage(self):
        if self.edt_user.text() == temp_user and self.edt_pass.text() == temp_password:
            if self.edt_pass.text()!="":
                self.edt_pass.setText('')
            mainPage.show()# Show window object 
            self.close() # Close current window
        else:
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()
    def ShowRegis(self):
        register.show()# Show window object 
        self.close() # Close current window
        # regis.show()# Show window object 
        # self.close() # Close current window
class PageRegister(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/regis.ui", self)
        self.btn_new.clicked.connect(self.ShowPage)
    def ShowPage(self):
        global temp_user, temp_password # Đặt 2 biến toàn cục để lưu trữ tạm thời tên và  password người dùng nhập vào
        temp_user = self.edt_user_new.text()
        temp_password = self.edt_new_pass.text()
        if self.edt_user_new.text() !="":
            if self.edt_new_pass.text() == self.edt_new_pass_2.text():
                self.edt_user_new.setText('')
                self.edt_new_pass.setText('')
                self.edt_new_pass_2.setText('')
                login.show()
                self.close()
            elif self.edt_new_pass.text() != self.edt_new_pass_2.text():
                msg_box.setText("Mật khẩu không khớp")
                msg_box.exec()
        elif self.edt_user_new.text() =="":
            msg_box.setText("Vui lòng lựa chọn tên đăng nhập")
            msg_box.exec()
        else:
            msg_box.setText("khong duoc")
            msg_box.exec()

class MainPage(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/new.ui", self)
        self.pushButton.clicked.connect(self.LogOut)
    def LogOut(self):
        login.show()
        self.close()    
  
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    login = Login() 
    register = PageRegister()
    mainPage = MainPage()

    msg_box = qtw.QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(qtw.QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    login.show()
    app.exec()