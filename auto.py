import sys
import pyautogui
import time
import keyboard
from pynput import mouse
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 status bar example - pythonspot.com'
        self.left = 50
        self.top = 50
        self.width = 480
        self.height = 480
        self.initMenu()
        self.initUI()


    def initMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
        playButton = QAction(QIcon("play24.png"), "Play", self)
        playButton.setShortcut("Alt+S")
        playButton.setStatusTip("Auto Play")
        playButton.triggered.connect(self.auto_play)
        editMenu.addAction(playButton)
        pauseButton = QAction(QIcon("pause24.png"), "Pause", self)
        pauseButton.setShortcut("Alt+P")
        pauseButton.setStatusTip("Play Pause")
        pauseButton.triggered.connect(self.pause)
        editMenu.addAction(pauseButton)
        openButton = QAction(QIcon("open24.png"), "Open", self)
        openButton.setShortcut("Ctrl+O")
        openButton.setStatusTip('Open File')
        openButton.triggered.connect(self.file_open)
        fileMenu.addAction(openButton)
        saveButton = QAction(QIcon("save24.png"), "Save", self)
        saveButton.setShortcut('Ctrl+S')
        saveButton.setStatusTip('SaveFile')
        saveButton.triggered.connect(self.file_save)
        fileMenu.addAction(saveButton)
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        posButton = QAction(QIcon("position24.png"), "Pos", self)
        posButton.setShortcut("f3")
        posButton.setStatusTip("Mouse Pointer")
        posButton.triggered.connect(self.currentPosition)
        toolsMenu.addAction(posButton)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(50, 50, 480, 480)
        self.statusBar().showMessage('Auto Mouse.')

        self.p = QPlainTextEdit(self)
        self.p.insertPlainText("ML:10:150")
        self.p.move(10, 30)
        self.p.resize(300, 300)

        currentMouseX, currentMouseY = pyautogui.position()
        self.labelX = QLabel("X : " + str(currentMouseX), self)
        self.labelX.move(330, 30)
        self.labelX.resize(50, 20)

        self.textboxX = QLineEdit(self)
        self.textboxX.move(330, 60)
        self.textboxX.resize(50, 20)

        self.labelY = QLabel("Y : " + str(currentMouseY), self)
        self.labelY.move(400, 30)
        self.labelY.resize(50, 20)

        self.textboxY = QLineEdit(self)
        self.textboxY.move(400, 60)
        self.textboxY.resize(50, 20)

        self.labelDe = QLabel("Delay : ", self)
        self.labelDe.move(330, 90)
        self.labelDe.resize(50, 20)

        self.textboxDe = QLineEdit(self)
        self.textboxDe.move(380, 90)
        self.textboxDe.resize(70, 20)

        self.r1 = QRadioButton(self)
        self.r1.setText("Left Click")
        self.r1.setChecked(True)
        self.r1.move(350, 120)
        self.r1.resize(150, 20)

        self.r2 = QRadioButton(self)
        self.r2.setText("Right Click")
        self.r2.setChecked(False)
        self.r2.move(350, 150)
        self.r2.resize(150, 20)

        self.b1 = QPushButton(self)
        self.b1.setText("Insert")
        self.b1.move(330, 180)
        self.b1.resize(120, 20)

        self.labelLo = QLabel("Loop : ", self)
        self.labelLo.move(330, 210)
        self.labelLo.resize(50, 20)

        self.textboxLo = QLineEdit(self)
        self.textboxLo.move(380, 210)
        self.textboxLo.resize(70, 20)
        self.textboxLo.setText('1')

        self.record = QPushButton(self)
        self.record.setText("record")
        self.record.move(210, 440)
        self.record.resize(80, 30)
        self.record.clicked.connect(self.record_play)

        self.play = QPushButton(self)
        self.play.setText("Play")
        self.play.move(300, 440)
        self.play.resize(80, 30)
        self.play.clicked.connect(self.auto_play)

        self.pause = QPushButton(self)
        self.pause.setText("Pause")
        self.pause.move(390, 440)
        self.pause.resize(80, 30)
        self.show()

    def file_open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.p.setPlainText(data)

    def file_save(self):
        filename = QFileDialog.getSaveFileName(self,
                                               "Save Item",
                                               filter="*.txt")
        if filename[0] != "":
            file = open(filename[0], "w")
            file.write(self.p.toPlainText())
            file.close()

    def currentPosition(self):
        currentMouseX, currentMouseY = pyautogui.position()
        self.labelX.setText("X : "+str(currentMouseX))
        self.labelY.setText("Y : " + str(currentMouseY))
        self.textboxX.setText(str(currentMouseX))
        self.textboxY.setText(str(currentMouseY))
        if self.r1.isChecked() :
            self.p.appendPlainText("ML:"+str(currentMouseX)+':'+str(currentMouseY))
        if self.r2.isChecked() :
            self.p.appendPlainText("MR:" + str(currentMouseX) + ':' + str(currentMouseY))
        if self.textboxDe.text() != '' :
            self.p.appendPlainText("DE:"+self.textboxDe.text())

    def auto_play(self):
        count = 0
        maxCnt = int(self.textboxLo.text())
        text = self.p.toPlainText()
        texts = text.split("\n")
        while count < maxCnt :
            for t in texts:
                strs = t.split(":")
                if strs[0] == "DE":
                    time.sleep(float(strs[1]))
                elif strs[0] == "ML":
                    pyautogui.moveTo(int(strs[1]), int(strs[2]))
                    pyautogui.click()
                elif strs[0] == "MR":
                    pyautogui.moveTo(int(strs[1]), int(strs[2]))
                    pyautogui.rightClick()
            maxCnt = maxCnt - 1

    def pause(self):
        self.msg = QMessageBox(self)
        self.msg.question(self, 'Pause Info', '정지 하시겠습니까?',
                        QMessageBox.Yes | QMessageBox.No)

    def record_play(self):
        self.thread = record(parent=self)

class record(QThread) :
    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.working = True
        self.run

    def run(self):
        with mouse.Listener(
                on_move=self.on_move,
                on_click=self.on_click,
                on_scroll=self.on_scroll) as listener:
            listener.join()

    def on_move(s, x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    def on_click(s, x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False

    def on_scroll(s, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    # Collect events until released
    # with mouse.Listener(
    #         on_move=on_move,
    #         on_click=on_click,
    #         on_scroll=on_scroll) as listener:
    #     listener.join()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())