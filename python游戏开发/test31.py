import sys
from PyQt5.QtWidgets import QApplication, QWidget,QCheckBox,QPushButton,QFrame,QSlider,QLabel,QProgressBar,QCalendarWidget,QVBoxLayout
from PyQt5.QtGui import QIcon,QColor
from PyQt5.QtCore import Qt

# widgets:QCheckBox, QPushButton,QSlider,QProgressBar,QCalendarWidget
#         QPixmap, QLineEdit,QSplitter,QComboBox

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(10,150,100,30)
        sld.valueChanged[int].connect(self.changeValue)

        cb = QCheckBox('show title',self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.col = QColor(0,0,0)
        redb = QPushButton('red',self)
        redb.setCheckable(True)
        redb.move(20,40)
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(20, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(20, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setStyleSheet("QWidget { background-color: %s }" %self.col.name())
        self.square.move(20,130)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('pen1.png'))

        self.show()
    def changeTitle(self,state):
        if state == Qt.Checked:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle(' ')

    def setColor(self,pressed):
        source = self.sender()
        if pressed:
            val = 255
        else: val = 0
        if source.text()=="red":
            self.col.setRed(val)
        elif source.text()=="Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame { background-color: %s }" %self.col.name())
    def changeValue(self,value):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
