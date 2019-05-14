from PyQt5.QtCore import QDate, QDateTime, QTime, Qt

now = QDateTime.currentDateTime()
print(now.offsetFromUtc())

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    # every app need an application object
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(400, 400)
    w.setWindowTitle('simple')
    w.show()

    sys.exit(app.exec_())
