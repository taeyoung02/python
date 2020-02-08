from PyQt5 import QtWidgets#c로만든 파이썬프로그램
import sys
class MyWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬GUI")
        self.resize(400,300)
        self.show()


app=QtWidgets.QApplication([])
win=MyWindows()
sys.exit(app.exec_())#윈도우가 닫히면 프로그램 종료