# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Quan_ly_hoc_vien.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 587)
        MainWindow.setIconSize(QtCore.QSize(25, 25))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 50, 831, 111))
        self.label_2.setStyleSheet("background-color: #C8CBF7;\n"
"               \n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 50, 161, 511))
        self.label_3.setStyleSheet("background-color: #E5E5F4;\n"
"               \n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.nutthem = QtWidgets.QPushButton(self.centralwidget)
        self.nutthem.setGeometry(QtCore.QRect(180, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.nutthem.setFont(font)
        self.nutthem.setStyleSheet("background-color: white;        /* nền trắng */\n"
"                  /* bỏ viền */\n"
"border-radius: 8px;            /* bo góc */\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("giaodien/them.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nutthem.setIcon(icon)
        self.nutthem.setIconSize(QtCore.QSize(20, 20))
        self.nutthem.setObjectName("nutthem")
        self.nuttxoa = QtWidgets.QPushButton(self.centralwidget)
        self.nuttxoa.setGeometry(QtCore.QRect(400, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.nuttxoa.setFont(font)
        self.nuttxoa.setStyleSheet("background-color: white;        /* nền trắng */\n"
"                  \n"
"border-radius: 8px;            /* bo góc */\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("giaodien/xoa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nuttxoa.setIcon(icon1)
        self.nuttxoa.setIconSize(QtCore.QSize(25, 25))
        self.nuttxoa.setObjectName("nuttxoa")
        self.nutsua = QtWidgets.QPushButton(self.centralwidget)
        self.nutsua.setGeometry(QtCore.QRect(290, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.nutsua.setFont(font)
        self.nutsua.setStyleSheet("background-color: white;        /* nền trắng */\n"
"                  /* bỏ viền */\n"
"border-radius: 8px;            /* bo góc */\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("giaodien/capnhat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nutsua.setIcon(icon2)
        self.nutsua.setIconSize(QtCore.QSize(20, 20))
        self.nutsua.setObjectName("nutsua")
        self.nuttimkiem = QtWidgets.QPushButton(self.centralwidget)
        self.nuttimkiem.setGeometry(QtCore.QRect(610, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.nuttimkiem.setFont(font)
        self.nuttimkiem.setStyleSheet("background-color: white;        /* nền trắng */\n"
"                 \n"
"border-radius: 8px;            /* bo góc */\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("giaodien/timkiem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nuttimkiem.setIcon(icon3)
        self.nuttimkiem.setIconSize(QtCore.QSize(20, 20))
        self.nuttimkiem.setObjectName("nuttimkiem")
        self.nguoidung = QtWidgets.QLabel(self.centralwidget)
        self.nguoidung.setGeometry(QtCore.QRect(170, 110, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nguoidung.setFont(font)
        self.nguoidung.setStyleSheet("")
        self.nguoidung.setObjectName("nguoidung")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(160, 160, 831, 401))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: white;\n"
"               \n"
"")
        self.label_12.setText("")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setObjectName("label_12")
        self.nutthoat = QtWidgets.QPushButton(self.centralwidget)
        self.nutthoat.setGeometry(QtCore.QRect(870, 470, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.nutthoat.setFont(font)
        self.nutthoat.setStyleSheet("background-color: #545FAA;        /* nền trắng */\n"
"color: white;  \n"
"border-radius: 10px;            /* bo góc */\n"
"")
        self.nutthoat.setIconSize(QtCore.QSize(18, 18))
        self.nutthoat.setObjectName("nutthoat")
        self.formWidget = QtWidgets.QWidget(self.centralwidget)
        self.formWidget.setGeometry(QtCore.QRect(0, 50, 151, 511))
        self.formWidget.setObjectName("formWidget")
        self.label_13 = QtWidgets.QLabel(self.formWidget)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_4 = QtWidgets.QLabel(self.formWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_4.setObjectName("label_4")
        self.mahocvien = QtWidgets.QTextEdit(self.formWidget)
        self.mahocvien.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.mahocvien.setObjectName("mahocvien")
        self.label_5 = QtWidgets.QLabel(self.formWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 111, 16))
        self.label_5.setObjectName("label_5")
        self.hoten = QtWidgets.QTextEdit(self.formWidget)
        self.hoten.setGeometry(QtCore.QRect(10, 110, 143, 31))
        self.hoten.setObjectName("hoten")
        self.label_6 = QtWidgets.QLabel(self.formWidget)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 131, 16))
        self.label_6.setObjectName("label_6")
        self.ngaysinh = QtWidgets.QDateEdit(self.formWidget)
        self.ngaysinh.setGeometry(QtCore.QRect(10, 170, 131, 31))
        self.ngaysinh.setObjectName("ngaysinh")
        self.label_10 = QtWidgets.QLabel(self.formWidget)
        self.label_10.setGeometry(QtCore.QRect(10, 210, 111, 16))
        self.label_10.setObjectName("label_10")
        self.nu = QtWidgets.QRadioButton(self.formWidget)
        self.nu.setGeometry(QtCore.QRect(20, 230, 61, 16))
        self.nu.setObjectName("nu")
        self.nam = QtWidgets.QRadioButton(self.formWidget)
        self.nam.setGeometry(QtCore.QRect(80, 230, 61, 16))
        self.nam.setObjectName("nam")
        self.label_7 = QtWidgets.QLabel(self.formWidget)
        self.label_7.setGeometry(QtCore.QRect(10, 260, 141, 16))
        self.label_7.setObjectName("label_7")
        self.heDT = QtWidgets.QComboBox(self.formWidget)
        self.heDT.setGeometry(QtCore.QRect(10, 280, 121, 31))
        self.heDT.setObjectName("heDT")
        self.heDT.addItem("")
        self.heDT.addItem("")
        self.heDT.addItem("")
        self.label_8 = QtWidgets.QLabel(self.formWidget)
        self.label_8.setGeometry(QtCore.QRect(10, 320, 141, 16))
        self.label_8.setObjectName("label_8")
        self.Diachi = QtWidgets.QTextEdit(self.formWidget)
        self.Diachi.setGeometry(QtCore.QRect(10, 340, 143, 31))
        self.Diachi.setObjectName("Diachi")
        self.label_9 = QtWidgets.QLabel(self.formWidget)
        self.label_9.setGeometry(QtCore.QRect(10, 380, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.formWidget)
        self.label_11.setGeometry(QtCore.QRect(10, 440, 141, 16))
        self.label_11.setObjectName("label_11")
        self.Khoahoc = QtWidgets.QComboBox(self.formWidget)
        self.Khoahoc.setGeometry(QtCore.QRect(10, 400, 131, 31))
        self.Khoahoc.setObjectName("Khoahoc")
        self.Khoahoc.addItem("")
        self.Khoahoc.addItem("")
        self.Khoahoc.addItem("")
        self.Khoahoc.addItem("")
        self.SDT = QtWidgets.QTextEdit(self.formWidget)
        self.SDT.setGeometry(QtCore.QRect(10, 460, 141, 31))
        self.SDT.setObjectName("SDT")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 991, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #2E3A8D;\n"
"color: #DADAF0;                /* Màu chữ vàng tươi */\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.nutclear = QtWidgets.QPushButton(self.centralwidget)
        self.nutclear.setGeometry(QtCore.QRect(510, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.nutclear.setFont(font)
        self.nutclear.setStyleSheet("background-color: white;        /* nền trắng */\n"
"                  \n"
"border-radius: 8px;            /* bo góc */\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("giaodien/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nutclear.setIcon(icon4)
        self.nutclear.setIconSize(QtCore.QSize(25, 25))
        self.nutclear.setObjectName("nutclear")
        self.bang = QtWidgets.QTableWidget(self.centralwidget)
        self.bang.setGeometry(QtCore.QRect(160, 160, 831, 281))
        self.bang.setStyleSheet("QTableWidget {\n"
"    border: none;                        /* Bỏ viền bảng */\n"
"    gridline-color: #666666;             /* Màu đường kẻ giữa các ô */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: none;                        /* Bỏ viền mỗi ô */\n"
"    padding: 4px;                         /* Cách lề cho nội dung */\n"
"}\n"
"\n"
"/* Tô đậm và thêm nền cho hàng tiêu đề */\n"
"QHeaderView::section {\n"
"    background-color: #545FAA;           /* Màu nền cho hàng tiêu đề */\n"
"    color: white;                        /* Màu chữ trắng */\n"
"    font-weight: bold;                   /* In đậm */\n"
"    padding: 4px;\n"
"    border: 1px solid #999999;           /* Viền tiêu đề */\n"
"}\n"
"")
        self.bang.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.bang.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.bang.setShowGrid(True)
        self.bang.setRowCount(1)
        self.bang.setColumnCount(8)
        self.bang.setObjectName("bang")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bang.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.bang.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bang.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bang.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bang.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bang.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bang.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bang.setHorizontalHeaderItem(7, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nutthem.setText(_translate("MainWindow", "Thêm"))
        self.nuttxoa.setText(_translate("MainWindow", "Xóa"))
        self.nutsua.setText(_translate("MainWindow", "Sửa "))
        self.nuttimkiem.setText(_translate("MainWindow", "Tìm kiếm,Thống kê"))
        self.nguoidung.setText(_translate("MainWindow", "Người dùng:"))
        self.nutthoat.setText(_translate("MainWindow", "Thoát"))
        self.label_13.setText(_translate("MainWindow", "    Thông tin học viên"))
        self.label_4.setText(_translate("MainWindow", "Mã học viên:"))
        self.label_5.setText(_translate("MainWindow", "Họ tên:"))
        self.label_6.setText(_translate("MainWindow", "Ngày sinh:"))
        self.label_10.setText(_translate("MainWindow", "Giới tính:"))
        self.nu.setText(_translate("MainWindow", "Nữ"))
        self.nam.setText(_translate("MainWindow", "Nam"))
        self.label_7.setText(_translate("MainWindow", "Hệ đào tạo:"))
        self.heDT.setItemText(0, _translate("MainWindow", "Chọn hệ đào tạo:"))
        self.heDT.setItemText(1, _translate("MainWindow", "Đại học"))
        self.heDT.setItemText(2, _translate("MainWindow", "Cao đẳng"))
        self.label_8.setText(_translate("MainWindow", "Địa chỉ:"))
        self.label_9.setText(_translate("MainWindow", "Khóa học:"))
        self.label_11.setText(_translate("MainWindow", "Số điện thoại:"))
        self.Khoahoc.setItemText(0, _translate("MainWindow", "Chọn Khóa học:"))
        self.Khoahoc.setItemText(1, _translate("MainWindow", "Công nghệ thông tin"))
        self.Khoahoc.setItemText(2, _translate("MainWindow", "Tin học"))
        self.Khoahoc.setItemText(3, _translate("MainWindow", "Khoa học máy tính"))
        self.label.setText(_translate("MainWindow", "QUẢN LÝ HỌC VIÊN"))
        self.nutclear.setText(_translate("MainWindow", "Clear"))
        item = self.bang.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã học viên"))
        item = self.bang.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ và tên"))
        item = self.bang.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ngày sinh"))
        item = self.bang.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Giới tính"))
        item = self.bang.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Địa chỉ"))
        item = self.bang.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Khóa học"))
        item = self.bang.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Hệ ĐT"))
        item = self.bang.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "SĐT"))
