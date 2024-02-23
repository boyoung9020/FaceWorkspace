from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt 

class Ui_carwling(object):
    def setupUi(self, carwling):
        carwling.setObjectName("carwling")
        carwling.setEnabled(True)
        carwling.resize(379, 566)
        self.namelist = QtWidgets.QListWidget(carwling) 
        self.namelist.setGeometry(QtCore.QRect(20, 10, 101, 171))
        self.namelist.setObjectName("namelist")
        self.namelist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.addButton = QtWidgets.QPushButton(carwling)
        self.addButton.setGeometry(QtCore.QRect(210, 19, 75, 23))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.addTextAndScroll)
        self.deleteButton = QtWidgets.QPushButton(carwling)
        self.deleteButton.setGeometry(QtCore.QRect(130, 50, 75, 23))
        self.deleteButton.setObjectName("deleteButton")
        self.crawlingButton = QtWidgets.QPushButton(carwling)
        self.crawlingButton.setGeometry(QtCore.QRect(130, 150, 75, 23))
        self.crawlingButton.setObjectName("crawlingButton")
        self.loglist = QtWidgets.QListWidget(carwling)  
        self.loglist.setGeometry(QtCore.QRect(20, 220, 341, 171))
        self.loglist.setObjectName("loglist") 
        self.detected_image_label = QtWidgets.QLabel(carwling)
        self.detected_image_label.setGeometry(QtCore.QRect(120, 420, 141, 131))
        self.detected_image_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.detected_image_label.setAutoFillBackground(True)
        self.detected_image_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.detected_image_label.setMidLineWidth(0)
        self.detected_image_label.setText("")
        self.detected_image_label.setTextFormat(QtCore.Qt.PlainText)
        self.detected_image_label.setPixmap(QtGui.QPixmap("Person_archive/정국/정국_11.jpg"))
        self.detected_image_label.setScaledContents(True)
        self.detected_image_label.setWordWrap(False)
        self.detected_image_label.setOpenExternalLinks(False)
        self.detected_image_label.setObjectName("detected_image_label")

        self.resetButton = QtWidgets.QPushButton(carwling)
        self.resetButton.setGeometry(QtCore.QRect(280, 470, 75, 23))
        self.resetButton.setObjectName("resetButton")






        self.ScheckBox = QtWidgets.QCheckBox(carwling)
        self.ScheckBox.setGeometry(QtCore.QRect(270, 110, 81, 16))
        font = QtGui.QFont()
        font.setFamily("한컴 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.ScheckBox.setFont(font)
        self.ScheckBox.setAutoRepeat(False)
        self.ScheckBox.setAutoExclusive(False)
        self.ScheckBox.setObjectName("ScheckBox")
        self.GcheckBox = QtWidgets.QCheckBox(carwling)
        self.GcheckBox.setGeometry(QtCore.QRect(270, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("한컴 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.GcheckBox.setFont(font)
        self.GcheckBox.setObjectName("GcheckBox")

        self.buttonGroup = QtWidgets.QButtonGroup(carwling)
        self.buttonGroup.addButton(self.ScheckBox)
        self.buttonGroup.addButton(self.GcheckBox)

        self.buttonGroup.buttonClicked.connect(self.checkBoxClicked)





        self.progressBar = QtWidgets.QProgressBar(carwling)
        self.progressBar.setGeometry(QtCore.QRect(20, 190, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setAlignment(Qt.AlignCenter)


        self.label = QtWidgets.QLabel(carwling)
        self.label.setGeometry(QtCore.QRect(130, 90, 121, 16))
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(carwling)
        self.nameEdit.setGeometry(QtCore.QRect(130, 20, 81, 21))
        self.nameEdit.setObjectName("nameEdit")
        self.imagenumEdit = QtWidgets.QLineEdit(carwling)
        self.imagenumEdit.setGeometry(QtCore.QRect(130, 110, 51, 21))
        self.imagenumEdit.setObjectName("imagenumEdit")
        self.imagenumEdit.setText("20")  
        self.label_2 = QtWidgets.QLabel(carwling)
        self.label_2.setGeometry(QtCore.QRect(150, 400, 91, 16))
        font = QtGui.QFont()
        font.setFamily("한컴 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.deleteallButton = QtWidgets.QPushButton(carwling)
        self.deleteallButton.setGeometry(QtCore.QRect(210, 50, 75, 23))
        self.deleteallButton.setObjectName("deleteallButton")

        self.retranslateUi(carwling)
        QtCore.QMetaObject.connectSlotsByName(carwling)

    def retranslateUi(self, carwling):
        _translate = QtCore.QCoreApplication.translate
        carwling.setWindowTitle(_translate("carwling", "Person Image Crawling"))
        self.addButton.setText(_translate("carwling", "추가"))
        self.deleteButton.setText(_translate("carwling", "삭제"))
        self.resetButton.setText(_translate("carwling", "리셋"))
        self.crawlingButton.setText(_translate("carwling", "실행"))
        self.label.setText(_translate("carwling", "다운로드할 이미지 수"))
        self.label_2.setText(_translate("carwling", "선택된 대표 얼굴"))
        self.deleteallButton.setText(_translate("carwling", "전체 삭제"))
        self.ScheckBox.setText(_translate("carwling", "Selenium"))
        self.GcheckBox.setText(_translate("carwling", "googleCSE"))
        
    def checkBoxClicked(self, checkBox):
        if checkBox == self.ScheckBox:
            print('Selenium 선택됨')
            # Selenium 체크박스가 선택되면 GoogleCSE 체크박스를 해제
            self.GcheckBox.setChecked(False)
        elif checkBox == self.GcheckBox:
            print('GoogleCSE 선택됨')
            # GoogleCSE 체크박스가 선택되면 Selenium 체크박스를 해제

            # imagenumEdit의 텍스트를 가져와서 정수로 변환하여 비교
            if int(self.imagenumEdit.text()) <= 10:
                self.GcheckBox.setChecked(True)  # imagenumEdit의 값이 10 이하일 때만 GcheckBox를 선택함
            else:
                self.GcheckBox.setChecked(False)
                self.ScheckBox.setChecked(True)
            

    # '추가' 버튼 클릭 시 호출되는 함수
    def addTextAndScroll(self):
        text = self.nameEdit.text()
        self.namelist.addItem(text)
        self.nameEdit.clear()
        self.namelist.scrollToBottom()
