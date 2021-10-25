
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QGridLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #qbtn = QPushButton('Quit', self) 
        grid = QGridLayout()
        self.setLayout(grid)
        lbl1 = QPushButton('ZetCode', self)
        lbl1.move(15, 10)

        lbl2 = QPushButton('tutorials', self)
        lbl2.move(135, 10)

        lbl3 = QPushButton('for programmers', self)
        lbl3.move(15, 70)

        lbl4 = QPushButton('QUIT',self)
        lbl4.move(135,70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()