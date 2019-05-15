import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout, QGridLayout, QLabel, QPushButton, \
    QMainWindow
from PyQt5.QtGui import QIcon


# events: source, object, target
# signals and slots


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        x = 0
        y = 0
        self.text = "x:{0},y:{1}".format(x, y)
        self.label = QLabel(self.text, self)
        vbox.addWidget(self.label)

        self.setMouseTracking(True)

        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)
        self.statusBar()
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('pen1.png'))

        self.show()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        text = "x:{0},y:{1}".format(x, y)
        self.label.setText(text)

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + "was pressed")

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
