# -*- coding: utf-8 -*-
import random
import sys
from PyQt5.QtCore import Qt, QTimer, QEventLoop, QRect, QCoreApplication
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QFrame
import time


_RESULT = []


class TestWindow(QWidget):
    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)
        self._current_color = QColor('red')
        self.startbutton = QPushButton(self)
        self.startbutton.setGeometry(QRect(40, 360, 121, 41))
        self.startbutton.clicked.connect(self.change_color)
        self.stopButton = QPushButton(self)
        self.stopButton.setGeometry(QRect(190, 360, 121, 41))
        self.nextButton = QPushButton(self)
        self.nextButton.setGeometry(QRect(340, 360, 121, 41))
        self.font = QFont('Arial', 10)
        self.font.setBold(True)
        self.label = QLabel(self)
        self.label.setFont(self.font)
        self.label1 = QLabel(self)
        self.label1.setGeometry(QRect(145, 15, 191, 31))
        self.label1.setText("Naciśnij START, aby włączyć zegar")
        self.label1.setFont(self.font)
        self.label1.adjustSize()
        self.label2 = QLabel(self)
        self.label2.setGeometry(QRect(40, 455, 191, 31))
        self.label2.setFont(self.font)
        self.startbutton.setText("START")
        self.stopButton.setText("STOP")
        self.nextButton.setText("Dalej>>")
        self.nextButton.setEnabled(False)

    def clicked(self):
        global _RESULT
        self.nextButton.setEnabled(True)
        self.label.setFont(self.font)
        self.end = time.time()
        diff = self.end - self.start - self.t
        _RESULT.append(diff)
        if diff < 0:
            self.label.setGeometry(QRect(215, 430, 191, 31))
            self.label.setText("Za szybko!")
        else:
            self.label.setGeometry(QRect(160, 430, 191, 31))
            self.label.setText("Twój czas reakcji to " + "{:.4f}".format(diff) + "s")
        self.startbutton.setEnabled(False)
        self.stopButton.setEnabled(False)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setPen(QPen(self._current_color, 3, Qt.SolidLine))
        painter.setBrush(QBrush(self._current_color, Qt.SolidPattern))
        painter.drawEllipse(150, 50, 200, 200)

    def change_color(self):
        self.t = random.uniform(1.5, 3.5)
        self.label1.setGeometry(QRect(215, 10, 191, 31))
        self.label1.setText("Zegar ruszył!")
        self.stopButton.clicked.connect(self.clicked)
        loop = QEventLoop()
        QTimer.singleShot(int(self.t * 1000), loop.quit)
        self.start = time.time()
        loop.exec_()
        self._current_color = QColor('green')
        self.label1.setGeometry(QRect(235, 10, 191, 31))
        self.label1.setText("Teraz!")
        self.update()


class ResultWindow(QWidget):
    def __init__(self, parent=None):
        super(ResultWindow, self).__init__(parent)
        self.font1 = QFont('Arial', 10)
        self.font1.setBold(True)
        self.font2 = QFont('Arial', 10)
        self.font2.setBold(False)
        self.label_6 = QLabel(self)
        self.label_6.setGeometry(QRect(210, 10, 101, 41))
        self.line = QFrame(self)
        self.line.setGeometry(QRect(50, 110, 231, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self)
        self.line_2.setGeometry(QRect(50, 145, 231, 31))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self)
        self.line_3.setGeometry(QRect(50, 185, 231, 31))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self)
        self.line_4.setGeometry(QRect(50, 225, 231, 31))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self)
        self.line_5.setGeometry(QRect(113, 90, 61, 231))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self)
        self.line_6.setGeometry(QRect(50, 265, 231, 31))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self)
        self.line_7.setGeometry(QRect(50, 305, 231, 31))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(60, 90, 61, 20))
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(190, 90, 47, 16))
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(70, 130, 47, 13))
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(70, 210, 47, 13))
        self.label_9 = QLabel(self)
        self.label_9.setGeometry(QRect(70, 290, 47, 13))
        self.label_10 = QLabel(self)
        self.label_10.setGeometry(QRect(70, 250, 47, 13))
        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QRect(70, 170, 47, 13))
        self.time1 = QLabel(self)
        self.time1.setGeometry(QRect(190, 130, 47, 13))
        self.time2 = QLabel(self)
        self.time2.setGeometry(QRect(190, 170, 47, 13))
        self.time3 = QLabel(self)
        self.time3.setGeometry(QRect(190, 210, 47, 13))
        self.time4 = QLabel(self)
        self.time4.setGeometry(QRect(190, 250, 47, 13))
        self.time5 = QLabel(self)
        self.time5.setGeometry(QRect(190, 290, 47, 13))
        self.label_11 = QLabel(self)
        self.label_11.setGeometry(QRect(310, 200, 111, 16))
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(170, 390, 141, 31))
        self.srednia = QLabel(self)
        self.srednia.setGeometry(QRect(430, 200, 47, 13))
        self.font3 = QFont('Arial', 18)
        self.font3.setBold(True)
        self.label_6.setText("WYNIKI")
        self.label_6.setFont(self.font3)
        self.label.setText("Podejście")
        self.label.setFont(self.font1)
        self.label_2.setText("Czas")
        self.label_2.setFont(self.font1)
        self.label_3.setText("1.")
        self.label_3.setFont(self.font2)
        self.label_4.setText("3.")
        self.label_4.setFont(self.font2)
        self.label_9.setText("5.")
        self.label_9.setFont(self.font2)
        self.label_10.setText("4.")
        self.label_10.setFont(self.font2)
        self.label_5.setText("2.")
        self.label_5.setFont(self.font2)
        t1, t2, t3, t4, t5, avg_t = self.convert_time()
        self.time1.setText(t1)
        self.time1.setFont(self.font2)
        self.time2.setText(t2)
        self.time2.setFont(self.font2)
        self.time3.setText(t3)
        self.time3.setFont(self.font2)
        self.time4.setText(t4)
        self.time4.setFont(self.font2)
        self.time5.setText(t5)
        self.time5.setFont(self.font2)
        self.label_11.setText("Średnia czasów:")
        self.label_11.setFont(self.font1)
        self.pushButton.setText("POWRÓT")
        self.srednia.setText(avg_t)
        self.srednia.setFont(self.font2)

    def convert_time(self):
        global _RESULT
        times = []
        avg = []
        for result in _RESULT:
            if result > 0:
                times.append(str("%.4f" % result) + "s")
                avg.append(result)
            else:
                times.append("-")
        t1, t2, t3, t4, t5 = times
        avg_value = sum(avg) / len(avg)
        _RESULT=[]
        return t1, t2, t3, t4, t5, str("%.4f" % avg_value) + "s"


class InstructionWindow(QWidget):
    def __init__(self, parent=None):
        super(InstructionWindow, self).__init__(parent)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 80, 501, 201))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton1 = QPushButton(self)
        self.pushButton1.setGeometry(QRect(190, 410, 121, 31))
        self.retranslateUi(self)

    def retranslateUi(self, InstructionWindow):
        _translate = QCoreApplication.translate
        InstructionWindow.setWindowTitle(_translate("InstructionWindow", "InstructionWindow"))
        self.label.setText(_translate("InstructionWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">INSTRUKCJA</span></p><p><br/></p><p align=\"center\"><span style=\" font-size:11pt;\">Podczas testu na ekranie pojawi się czerwone koło, które po kliknięciu przycisku START po losownym czasie zmieni kolor na zielony. Twoim zadaniem jest jak najszybciej nacisnąć przycisk STOP, gdy koło zmieni kolor. Test składa się z fazy próbnej (3 próby) i fazy testowej składającej się z 5 podejść, na podstawie których zostanie wyliczona na koniec średnia.</span></p></body></html>"))
        self.pushButton1.setText(_translate("InstructionWindow", "START"))


class DemoWindow(QWidget):
    def __init__(self, parent=None):
        super(DemoWindow, self).__init__(parent)
        self._current_color = QColor('red')
        self.startbutton = QPushButton(self)
        self.startbutton.setGeometry(QRect(40, 360, 121, 41))
        self.startbutton.clicked.connect(self.change_color)
        self.stopButton = QPushButton(self)
        self.stopButton.setGeometry(QRect(190, 360, 121, 41))
        self.nextButton = QPushButton(self)
        self.nextButton.setGeometry(QRect(340, 360, 121, 41))
        self.font = QFont('Arial', 10)
        self.font.setBold(True)
        self.label = QLabel(self)
        self.label.setFont(self.font)
        self.label1 = QLabel(self)
        self.label1.setGeometry(QRect(145, 15, 191, 31))
        self.label1.setText("Naciśnij START, aby włączyć zegar")
        self.label1.setFont(self.font)
        self.label1.adjustSize()
        self.label2 = QLabel(self)
        self.label2.setGeometry(QRect(40, 455, 191, 31))
        self.label2.setFont(self.font)
        self.startbutton.setText("START")
        self.stopButton.setText("STOP")
        self.nextButton.setText("Dalej>>")
        self.nextButton.setEnabled(False)

    def clicked(self):
        self.nextButton.setEnabled(True)
        self.label.setFont(self.font)
        self.end = time.time()
        diff = self.end - self.start - self.t
        if diff < 0:
            self.label.setGeometry(QRect(215, 430, 191, 31))
            self.label.setText("Za szybko!")
        else:
            self.label.setGeometry(QRect(160, 430, 191, 31))
            self.label.setText("Twój czas reakcji to " + "{:.4f}".format(diff) + "s")
        self.startbutton.setEnabled(False)
        self.stopButton.setEnabled(False)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setPen(QPen(self._current_color, 3, Qt.SolidLine))
        painter.setBrush(QBrush(self._current_color, Qt.SolidPattern))
        painter.drawEllipse(150, 50, 200, 200)

    def change_color(self):
        self.t = random.uniform(1.5, 3.5)
        self.label1.setGeometry(QRect(215, 10, 191, 31))
        self.label1.setText("Zegar ruszył!")
        self.stopButton.clicked.connect(self.clicked)
        loop = QEventLoop()
        QTimer.singleShot(int(self.t * 1000), loop.quit)
        self.start = time.time()
        loop.exec_()
        self._current_color = QColor('green')
        self.label1.setGeometry(QRect(235, 10, 191, 31))
        self.label1.setText("Teraz!")
        self.update()


class IntroductionWindow(QWidget):
    def __init__(self, parent=None):
        super(IntroductionWindow, self).__init__(parent)
        self.font = QFont('Arial', 25)
        self.font.setBold(True)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(130, 210, 291, 50))
        self.label.setFont(self.font)
        self.loop = QEventLoop()
        QTimer.singleShot(1350, self.loop.quit)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon('timer.png'))
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(500, 500)
        self.startInstructionWindow()
        self.count = 0

    def startDemo(self):
        self.Demo = DemoWindow(self)
        self.setCentralWidget(self.Demo)
        self.count += 1
        self.Demo.label2.setText("Próba " + str(self.count) + "/3")
        if self.count < 3:
            self.Demo.nextButton.clicked.connect(self.startDemo)
        else:
            self.count = 0
            self.Demo.nextButton.clicked.connect(self.startIntroductionWindowTest)

    def startTest(self):
        self.Test = TestWindow(self)
        self.setCentralWidget(self.Test)
        self.count += 1
        self.Test.label2.setText("Test " + str(self.count) + "/5")
        if self.count < 5:
            self.Test.nextButton.clicked.connect(self.startTest)
        else:
            self.count = 0
            self.Test.nextButton.clicked.connect(self.startResult)

    def startResult(self):
        self.Result = ResultWindow(self)
        self.setCentralWidget(self.Result)
        self.Result.pushButton.clicked.connect(self.startInstructionWindow)
        self.show()

    def startInstructionWindow(self):
        self.Window = InstructionWindow(self)
        self.setWindowTitle("Pomiar czasu refleksu")
        self.setCentralWidget(self.Window)
        self.Window.pushButton1.clicked.connect(self.startIntroductionWindowDemo)
        self.show()

    def startIntroductionWindowDemo(self):
        self.IntroDemo = IntroductionWindow(self)
        self.IntroDemo.label.setText("FAZA PRÓBNA")
        self.setCentralWidget(self.IntroDemo)
        self.IntroDemo.loop.exec_()
        self.show()
        self.startDemo()

    def startIntroductionWindowTest(self):
        self.IntroTest = IntroductionWindow(self)
        self.IntroTest.label.setText("FAZA TESTOWA")
        self.setCentralWidget(self.IntroTest)
        self.IntroTest.loop.exec_()
        self.show()
        self.startTest()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
