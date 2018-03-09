# -*- coding: utf-8 -*-
import sql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_fornecedor(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(655, 473)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(655, 473))
        Form.setMaximumSize(QtCore.QSize(655, 473))
        Form.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 231, 21))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 631, 361))
        self.tabWidget.setMaximumSize(QtCore.QSize(631, 371))
        self.tabWidget.setStyleSheet("background: rgb(200, 200,200);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget_18 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget_18.setGeometry(QtCore.QRect(10, 30, 561, 101))
        self.layoutWidget_18.setObjectName("layoutWidget_18")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_18)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_10.addWidget(self.label_26)
        self.codigo = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.codigo.setEnabled(True)
        self.codigo.setObjectName("codigo")
        self.horizontalLayout_10.addWidget(self.codigo)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_10.addWidget(self.label_27)
        self.nome = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.nome.setEnabled(True)
        self.nome.setObjectName("nome")
        self.horizontalLayout_10.addWidget(self.nome)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_11.addWidget(self.label_29)
        self.descricao = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.descricao.setEnabled(True)
        self.descricao.setObjectName("descricao")
        self.horizontalLayout_11.addWidget(self.descricao)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_11.addWidget(self.label_28)
        self.endereco = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.endereco.setEnabled(True)
        self.endereco.setObjectName("endereco")
        self.horizontalLayout_11.addWidget(self.endereco)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_12.addWidget(self.label_30)
        self.telefone = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.telefone.setEnabled(True)
        self.telefone.setObjectName("telefone")
        self.horizontalLayout_12.addWidget(self.telefone)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_12.addWidget(self.label_31)
        self.site = QtWidgets.QLineEdit(self.layoutWidget_18)
        self.site.setEnabled(True)
        self.site.setObjectName("site")
        self.horizontalLayout_12.addWidget(self.site)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setFocusPolicy(QtCore.Qt.TabFocus)
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_9)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 50, 551, 26))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(26)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.otimo = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.otimo.setChecked(True)
        self.otimo.setObjectName("otimo")
        self.horizontalLayout_2.addWidget(self.otimo)
        self.bom = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.bom.setObjectName("bom")
        self.horizontalLayout_2.addWidget(self.bom)
        self.regular = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.regular.setObjectName("regular")
        self.horizontalLayout_2.addWidget(self.regular)
        self.ruim = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.ruim.setObjectName("ruim")
        self.horizontalLayout_2.addWidget(self.ruim)
        self.verticalLayout.addWidget(self.groupBox_9)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.Cadastro = QtWidgets.QWidget()
        self.Cadastro.setObjectName("Cadastro")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Cadastro)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 591, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.observacao = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.observacao.setGeometry(QtCore.QRect(10, 30, 551, 231))
        self.observacao.setObjectName("observacao")
        self.tabWidget.addTab(self.Cadastro, "")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(450, 430, 191, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setStyleSheet("image: url(:/img/img/icons8-ok-filled.svg);\n"
"background-color:   rgb(200,200,200);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/icons8-ok-filled.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setStyleSheet("background-color:   rgb(200,200,200);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/icons8-cancelar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 658, 41))
        self.label_6.setStyleSheet("background-color:  rgba(255, 207, 183, 200);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(490, 0, 141, 81))
        self.label.setStyleSheet("image: url(:/img/img/hotel-supplier.svg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_6.raise_()
        self.label_3.raise_()
        self.tabWidget.raise_()
        self.splitter.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.observacao, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.tabWidget)
        Form.setTabOrder(self.tabWidget, self.pushButton)
        self.eventos()
    def eventos(self):
        self.pushButton.clicked.connect(self.cadastrar)

    def cadastrar(self):        
        otimo = bom = regular = ruim = 0

        if(self.otimo.isChecked() == True):
            otimo = 1
        elif(self.bom.isChecked() == True):
            bom = 1 
        elif(self.regular.isChecked() == True):
            regular = 1
        elif(self.ruim.isChecked() == True):
            ruim = 1

            
        lista = [self.codigo.text(),self.descricao.text(),
        self.nome.text(),self.endereco.text(),self.telefone.text(),self.site.text(),otimo,bom,regular,ruim,self.observacao.toPlainText()]

        if(not lista[0] or not lista[1] or not lista[2] or not lista[3]or not lista[4] or not lista[5]):            
            print("Preencha")
        else:
            sql.inserir_fornecedor2(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],
            lista[6],lista[7],lista[8],lista[9],lista[10])

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastrar Fornecedor"))
        self.label_3.setText(_translate("Form", "Cadastrar Fornecedor"))
        self.groupBox_3.setTitle(_translate("Form", "Caracteristicas"))
        self.label_26.setText(_translate("Form", "Codigo"))
        self.label_27.setText(_translate("Form", "Nome"))
        self.label_29.setText(_translate("Form", "Descrição"))
        self.label_28.setText(_translate("Form", "Endereço"))
        self.label_30.setText(_translate("Form", "Telefone"))
        self.label_31.setText(_translate("Form", "Site"))
        self.groupBox_9.setTitle(_translate("Form", "Prioridade"))
        self.label_2.setText(_translate("Form", "Classificação:"))
        self.otimo.setText(_translate("Form", "Ótimo"))
        self.bom.setText(_translate("Form", "Bom"))
        self.regular.setText(_translate("Form", "Regular"))
        self.ruim.setText(_translate("Form", "Ruím"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Page"))
        self.groupBox_2.setTitle(_translate("Form", "Observações"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cadastro), _translate("Form", "Tab 1"))
        self.pushButton.setText(_translate("Form", "Cadastrar"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_fornecedor()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
