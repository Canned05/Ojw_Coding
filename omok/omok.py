import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtGui import QPainter, QPen 
from PyQt5.QtCore import Qt, QTimer
# import pyglet

from_class = uic.loadUiType("omok.ui")[0]

class MyApp(QWidget, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('gomoku!!')
        self.show()
        self.btn_restart.clicked.connect(self.restart)

        #global value init
        self.idle =0
        self.black = 1
        self.white = 2
        self.maxLine = 15

        self.map = [[]]
        self.map = [[self.idle] * self.maxLine for _ in range(self.maxLine)]
        self.btnObj = []
        self.draw_btn()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_board(qp)
        qp.end()

    def draw_btn(self):
        xPos = -20
        yPos = -20
        self.xObjList = []
        for y in range(15):
            xPos = -20
            yPos = yPos + 50
            for i in range(15):
                btn = QPushButton(self)
                xPos = xPos + 50
                btn.setGeometry(xPos,yPos,40,40)
                self.xObjList.append(btn)
                btn.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
                btn.clicked.connect(self.btnPush)
                btn.show()
            self.btnObj.append(self.xObjList)
            self.xObjList = []

    def btnPush(self):
        #global xObjList
        obj = self.sender()
        rect = obj.geometry()
        posX = int((rect.x() - 30)/50)
        posY = int((rect.y() - 30)/50)
        print(int((rect.x() - 30)/50), int((rect.y() - 30)/50))

        if self.map[posY][posX] == self.idle:
            self.setDolColor(obj, self.black)
            self.map[posY][posX] = self.black
            self.winnerCheck(posX, posY, self.black)
            self.AIgomoku(self.white)

    def AIgomoku(self,type):
        Cpu = self.GetFavorablePos(type)
        User = self.GetFavorablePos(self.black)

        if (Cpu[2] >= User[2]):
            self.map[Cpu[1]][Cpu[0]] = self.white
            self.setDolColor(self.btnObj[Cpu[1]][Cpu[0]], self.white)
            if self.winnerCheck(Cpu[0],Cpu[1],self.white):
                self.lose()
        else:
            self.map[User[1]][User[0]] = self.white
            self.setDolColor(self.btnObj[User[1]][User[0]], self.white)
            if self.winnerCheck(User[0], User[1], self.white):
                self.lose()
    def GetFavorablePos(self, Type):
        FavorableList = []
        FavorableList = [[self.idle] * self.maxLine for _ in range(self.maxLine)]

        for y in range(self.maxLine):
            for x in range(self.maxLine):
                if self.map[y][x] == 0:
                    FavorableList[y][x] = self.GetFavorableValue(x, y, Type)
                else:
                    FavorableList[y][x] = 0
        max = 0
        FavorX, FavorY = 0, 0
        for y in range(self.maxLine):
            for x in range (self.maxLine):
                if (FavorableList[y][x] > max):
                    max = FavorableList[y][x]
                    FavorX = x
                    FavorY = y
        return [FavorX, FavorY, max]
    def GetFavorableValue(self, nX, nY, Type):
        x = nX
        y = nY
        count = 0
        hazard = 0

        Map = self.map[:]
        for i in range(self.maxLine):
            Map[i] = self.map[i][:]

        Map[nY][nX] = Type

        while (x > 0) and (Map[y][x - 1] == Type):
            x -= 1
        while (x <= self.maxLine-1) and (Map[y][x] == Type):
            count += 1
            x += 1
        if (count > 5):
            count = 2
        hazard += pow(10, count)

        x = nX
        y = nY
        count = 0

        while (y > 0) and (Map[y - 1][x] == Type):
            y -= 1
        while (y <= self.maxLine-1) and (Map[y][x] == Type):
            count += 1
            y += 1
        if (count > 5):
            count = 2
        hazard += pow(10, count)
        x = nX
        y = nY
        count = 0

        while (x > 0) and (y > 0) and (Map[y - 1][x - 1] == Type):
            x -= 1
            y -= 1
        while (x <= self.maxLine-1) and (y <= self.maxLine-1) and (Map[y][x] == Type):
            count += 1
            x += 1
            y += 1
        if (count > 5):
            count = 2
        hazard += pow(10, count)
        x = nX
        y = nY
        count = 0

        while (x < self.maxLine-1) and (y > 0) and (Map[y - 1][x + 1] == Type):
            x += 1
            y -= 1
        while (x >= 0) and (y <= self.maxLine-1) and (Map[y][x] == Type):
            count += 1
            x -= 1
            y += 1
        if (count > 5):
            count = 2
        hazard += pow(10, count)

        return hazard
    def lose(self):
        QMessageBox.warning(self, "GAME SET", "You are Lose!!!")

    def winnerCheck(self,xPos,yPos,type):

        ##Find x Pos
        count = 0
        x = xPos
        y = yPos

        while(x > 0) and (self.map[y][x-1] == type):
            x -= 1
        while(x <= 14) and (self.map[y][x] == type):
            count += 1
            x += 1

        if count ==  5:
            if type == self.white:
                QMessageBox.warning(self, "GAME SET", "White Win!!!")
            else:
                QMessageBox.warning(self, "GAME SET", "Black Win!!!")
            return

        ## Find y Pos
        count = 0
        x = xPos
        y = yPos

        while (y > 0) and (self.map[y - 1][x] == type):
            y -= 1
        while (y <= 14) and (self.map[y][x] == type):
            count += 1
            y += 1

        if count == 5:
            if type == self.white:
                QMessageBox.warning(self, "GAME SET", "White Win!!!")
            else:
                QMessageBox.warning(self, "GAME SET", "Black Win!!!")
            return
        count = 0
        x = xPos
        y = yPos

        while (x > 0 and y > 0) and (self.map[y-1][x-1]  == type):
            x -= 1
            y -= 1
        while (x <= 14 and y <= 14) and (self.map[y][x] == type):
            count += 1
            x += 1
            y += 1

        if count == 5:
            if type == self.white:
                QMessageBox.warning(self,"GAME SET", "White Win!!")
            else:
                QMessageBox.warning(self, "GAME SET" , "Black Win!!")
            return
        count = 0
        x = xPos
        y = yPos
        try:
            while (x > 0 and y > 0) and (self.map[y-1][x+1] == type):
                x += 1
                y -= 1
            while (x <= 14 and y <= 14) and (self.map[y][x] == type):
                count += 1
                x -= 1
                y += 1
        except:
            pass

        if count == 5:
            if type == self.white:
                QMessageBox.warning(self, "GAME SET" ,"White Win!!!")
            else:
                QMessageBox.warning(self, "GAME SET" ,"Black Win!!!")
            return

    def setDolColor(self,obj,typ):
        if typ == self.white:
            obj.setStyleSheet("border-style: solid; border-radius: 20px;"
                              "border-color: #000000; border-width: 2px; "
                              "background-color: #ffffff")
        else:
            obj.setStyleSheet("border-style: solid; border-radius: 20px;"
                              "border-color: #000000; border-width: 2px; "
                              "background-color: #000000")
            self.timer = QTimer(self)
            self.timer.start()
        obj.show()


    def draw_board(self, qp):
        xPos = 0
        yPos = 0
        for i in range(15):
            xPos = xPos + 50
            yPos = yPos + 50
            qp.setPen(QPen(Qt.black,1))
            qp.drawLine(xPos ,50, xPos, 750)
            qp.drawLine(50, yPos, 750, yPos)

    def restart(self, obj):
        print("restart")
        self.map = [[self.idle] * self.maxLine for _ in range(self.maxLine)]
        for obj in self.btnObj:
            for i in obj:
                i.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
                i.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())