# Form implementation generated from reading ui file 'D:\Uni_Lily\Proyecto\agregar.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
from datetime import datetime
from io import BytesIO


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 657)
        MainWindow.setStyleSheet("background-color: rgb(255, 198, 246);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1131, 101))
        self.label.setStyleSheet(" background-color: rgb(11, 198, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MV Boli\";\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 150, 171, 31))
        self.label_2.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.id_persona = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.id_persona.setGeometry(QtCore.QRect(350, 150, 211, 31))
        self.id_persona.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.id_persona.setObjectName("id_persona")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 101, 571))
        self.label_3.setStyleSheet("background-color: rgb(11, 198, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.Nombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(350, 200, 211, 31))
        self.Nombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Nombre.setObjectName("Nombre")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 200, 101, 31))
        self.label_4.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.Apelli_pa = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Apelli_pa.setGeometry(QtCore.QRect(350, 250, 211, 31))
        self.Apelli_pa.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Apelli_pa.setObjectName("Apelli_pa")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 250, 171, 31))
        self.label_5.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.Imagen = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Imagen.setGeometry(QtCore.QRect(350, 400, 211, 31))
        self.Imagen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Imagen.setObjectName("Imagen")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 400, 91, 31))
        self.label_6.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.Apellid_ma = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Apellid_ma.setGeometry(QtCore.QRect(350, 300, 211, 31))
        self.Apellid_ma.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Apellid_ma.setObjectName("Apellid_ma")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 300, 181, 31))
        self.label_7.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 350, 91, 31))
        self.label_8.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.Placas = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Placas.setGeometry(QtCore.QRect(350, 350, 211, 31))
        self.Placas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Placas.setObjectName("Placas")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(630, 240, 121, 31))
        self.label_9.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.Descripcion = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Descripcion.setGeometry(QtCore.QRect(790, 240, 211, 31))
        self.Descripcion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Descripcion.setObjectName("Descripcion")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(630, 340, 91, 31))
        self.label_10.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_10.setObjectName("label_10")
        self.Direccion = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Direccion.setGeometry(QtCore.QRect(790, 290, 211, 31))
        self.Direccion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Direccion.setObjectName("Direccion")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(630, 390, 141, 31))
        self.label_11.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(630, 140, 101, 31))
        self.label_12.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_12.setObjectName("label_12")
        self.C = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.C.setGeometry(QtCore.QRect(790, 390, 211, 31))
        self.C.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.C.setObjectName("C")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(630, 290, 91, 31))
        self.label_13.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_13.setObjectName("label_13")
        self.Telefono = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Telefono.setGeometry(QtCore.QRect(790, 340, 211, 31))
        self.Telefono.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Telefono.setObjectName("Telefono")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(630, 190, 91, 31))
        self.label_14.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_14.setObjectName("label_14")
        self.Modelo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Modelo.setGeometry(QtCore.QRect(790, 190, 211, 31))
        self.Modelo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Modelo.setObjectName("Modelo")
        self.pb_agregar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pb_agregar.setGeometry(QtCore.QRect(560, 530, 111, 81))
        self.pb_agregar.setStyleSheet("background-color: rgb(0, 255, 127);\n"
"font: 16pt \"MV Boli\";")
        self.pb_agregar.setObjectName("pb_agregar")
        self.pb_agregar.clicked.connect(self.agregar_datos)
        self.Fecha = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Fecha.setGeometry(QtCore.QRect(580, 460, 211, 31))
        self.Fecha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Fecha.setObjectName("Fecha")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(480, 460, 81, 31))
        self.label_15.setStyleSheet("font: 8pt \"MV Boli\";")
        self.label_15.setObjectName("label_15")
        self.Marca = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Marca.setGeometry(QtCore.QRect(790, 140, 211, 31))
        self.Marca.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.Marca.setObjectName("Marca")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">Agregar un registro</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">Agregar datos </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Id de la persona:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre: </span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Apellido paterno:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Imagen:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Apellido materno: </span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Placas: </span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Descripción:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Teléfono:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Codigo Postal:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Marca:</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Dirección:</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Modelo:</span></p></body></html>"))
        self.pb_agregar.setWhatsThis(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MV Boli\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pb_agregar.setText(_translate("MainWindow", "Agregar"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Fecha:</span></p></body></html>"))


    def agregar_datos(self):
        # Conexión a la base de datos
        user='Sofia';
        password='abc';
        host='SOFIA';
        database='lili';
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ host + ';DATABASE='+database + ';UID='+user + ';PWD='+password)

        # Creación de la consulta INSERT
        query = "INSERT INTO Problema (Id_peersona , Nombre , Apellido_pa , Apellido_ma ,Placas , Imagen , Marca , Modelo , Descripcion , Direccion , Telefono , Cp , Fecha ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"


        # Obtención de los valores ingresados por el usuario

        Id_peersona = self.id_persona.text()
        Nombre = self.Nombre.text()
        Apellido_pa = self.Apelli_pa.text()
        Apellido_ma = self.Apellid_ma.text()
        Placas = self.Placas.text()
        Imagen = BytesIO(self.Imagen.text().encode('latin1')).read()        
        Marca =self.Marca.text()
        Modelo =self.Modelo.text()
        Descripcion = self.Descripcion.text()
        Direccion=self.Direccion.text()
        Telefono= self.Telefono.text()
        Cp= int(self.C.text())
        Fecha=datetime.strptime(self.Fecha.text(), '%Y-%m-%d')


        # Ejecución de la consulta INSERT
        cursor = cnxn.cursor()
        cursor.execute(query, Id_peersona , Nombre , Apellido_pa , Apellido_ma ,Placas , Imagen , Marca , Modelo , Descripcion , Direccion , Telefono , Cp , Fecha)
        cnxn.commit()

        # Cierre de la conexión a la base de datos
        cnxn.close()

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
