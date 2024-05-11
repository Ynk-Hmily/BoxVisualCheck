# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\Desktop\ZhouChuanHong\tongji copy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import opencv_part.CV_Globals as cvglobal
from opencv_part import CVTest_co
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import time
import shutil
import threading


class CATPICUTRE(QtWidgets.QMainWindow):
    def __init__(self):
        super(CATPICUTRE,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 120)
        MainWindow.setMinimumSize(QtCore.QSize(200, 120))
        MainWindow.setMaximumSize(QtCore.QSize(200, 120))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame{\n"
"border-image: url(:/images/images/background.png);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_info = QtWidgets.QWidget(self.frame)
        self.widget_info.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_info.setMaximumSize(QtCore.QSize(200, 200))
        self.widget_info.setStyleSheet("#widget_info{\n"
"    background-color: none;\n"
"     border-radius:8px;\n"
"\n"
"}")
        self.widget_info.setObjectName("widget_info")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_info)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.catch_picture_and_recognize = QtWidgets.QPushButton(self.widget_info)
        self.catch_picture_and_recognize.setMinimumSize(QtCore.QSize(150, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.catch_picture_and_recognize.setFont(font)
        self.catch_picture_and_recognize.setStyleSheet("#catch_picture_and_recognize{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"background-color: rgb(186, 186, 186);\n"
"border:2px solid rgb(150, 150, 150) ;\n"
"}\n"
"\n"
"#catch_picture_and_recognize:hover{\n"
"background-color: rgb(162, 162, 162);\n"
"color:black;\n"
"}\n"
"\n"
"\n"
"\n"
"#catch_picture_and_recognize:pressed{\n"
"background-color:  rgb(120, 120, 120);\n"
"color:black;\n"
"padding-top:3px;\n"
"padding-left:3px;\n"
"}")
        self.catch_picture_and_recognize.setObjectName("catch_picture_and_recognize")
        self.verticalLayout_2.addWidget(self.catch_picture_and_recognize)
        self.horizontalLayout_2.addWidget(self.widget_info)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)







        ########################开始写功能
########################开始写功能
########################开始写功能
########################开始写功能
########################开始写功能
########################开始写功能

###按钮事件绑定
        self.catch_picture_and_recognize.clicked.connect(self.catch_fuc)

    def catch_fuc(self):#
        cvglobal.set_capture_val(True)
        
        time.sleep(1)
        
        #CVTest_co.Test("./opencv_part/test_1.jpg")

        cur_date = QDate.currentDate()
        year=str(cur_date.year())
        month=str(cur_date.month())
        date=cur_date.day()
        cur_time = QTime.currentTime()
        hour=cur_time.hour()
        minute=cur_time.minute()
        sec=cur_time.second()
        curdt=[year,month,date,hour,minute,sec]
        cvglobal.set_timepathlist_val(curdt)
        datetime=list(map(str,curdt))
        timepath=datetime[0]+"."+datetime[1]+"."+datetime[2]+"-"+datetime[3]+"h"+datetime[4]+"m"+datetime[5]+"s"
        cvglobal.set_timepath_val(timepath)
        catchthread=threading.Thread(target= CVTest_co.Test,args=("./Pictures/cachesPic.jpg",))
        
        #CVTest_co.Test("./Pictures/cachesPic.jpg")
        shutil.copyfile(src="./Pictures/cachesPic.jpg",dst="./opencv_part/pic/"+timepath+".jpg")
        
        catchthread.start()
        print("ssdafsa")
        catchthread.join()
        
        print("pathsaved")
        #存到数据库
        #processor.process_image(product_name,image_id,image_path, barcode,year,month,day,hour,minute,shift)
        #print(timepath)
        print(cvglobal.capture)
        return datetime,timepath







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.catch_picture_and_recognize.setText(_translate("MainWindow", "拍照并识别"))
import recources_rc


if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CATPICUTRE()

    


    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
    
