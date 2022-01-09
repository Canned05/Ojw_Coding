
import sys
import string
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PIL import Image
import cv2

import threading

from PyQt5.uic.properties import QtGui

form_class = uic.loadUiType('mainwindow.ui')[0]

class MyWindow(QMainWindow, form_class):

    filePath = ''
    cheak = 0

    def __init__(self) -> object:
        super().__init__()
        self.setupUi(self)
        self.actionNew_File.setShortcut('Ctrl+o')
        self.actionNew_File.setStatusTip('File Open')
        self.actionNew_File.triggered.connect(self.fileOpen)
        self.pushButton.clicked.connect(self.btn1_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)

        #self.pushButton.clicked.connect(self.IMG_Cheak)





    def fileOpen(self):
        global filePath, cheak
        filePath = QFileDialog.getOpenFileName(self, filter="Img(*.png *.jpg)")
        print(filePath[0])
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(filePath[0])
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(350)
        self.OG.setPixmap(self.qPixmapFileVar)
        self.cheak = 1

    def btn1_clicked(self):
        global filePath
        im = Image.open(filePath[0])

        # 90도 회전
        img3 =  cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
        self.IMG_Show(img3, QImage.Format_RGB32)

    def IMG_Show(self, data, form):
        self.qImage = QImage(data.data, data.shape[1], data.shape[0], data.strides[0], form)

        # self.qImage = self.qImage.scaledToWidth(350)
        self.OG_2.setPixmap(QPixmap.fromImage(self.qImage))
        #QMessageBox.about(self, "90º회전", "변환사진을 확인해주세요")



    def btn2_clicked(self):
        QMessageBox.about(self, '좌우 반전', "변환사진을 확인해주세요")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


