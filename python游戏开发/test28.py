import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon


# layout : absolute positioning, box,grid

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # absolute positioning
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lab2 = QLabel('tutorials', self)
        lab2.move(35, 40)

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        # box layout
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # self.setLayout(vbox)

        # grid layout
        gird = QGridLayout()
        self.setLayout(gird)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            gird.addWidget(button, *position)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('pen1.png'))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
