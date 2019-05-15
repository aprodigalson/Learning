import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QPushButton, QFrame, QColorDialog, \
    QVBoxLayout, QSizePolicy, QLabel, QFontDialog, QFileDialog, QAction, QTextEdit, QMainWindow
from PyQt5.QtGui import QIcon, QColor


# dialog: QInputDialog,QColorDialog,QFontDialog,QFileDialog

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.jpg'), 'Open', self)
        openFile.setShortcut('Ctrl+o')
        openFile.setStatusTip('open new File')
        openFile.triggered.connect(self.showFileDialog)
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        # self.btn.clicked.connect(self.showDialog)
        # self.btn.clicked.connect(self.showColorDialog)
        # self.btn.clicked.connect(self.showFontDialog)
        self.btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 50)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget{background-color:%s}" % col.name())
        self.frm.move(130,70)
        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('pen1.png'))

        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))

    def showColorDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget{background-color:%s}" % col.name())

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, "open file", '/')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
