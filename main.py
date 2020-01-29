from PyQt5.QtCore import QByteArray, QBuffer
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication([])
clipboard = app.clipboard()


def getBase64():
    try:
        image = clipboard.image()
        ba = QByteArray()
        buffer = QBuffer(ba)
        buffer.open(QIODevice.WriteOnly)
        image.save(buffer, 'png')
        base64_str = 'data:image/png;base64,' + str(ba.toBase64().data(), 'utf8')
        if len(base64_str<100):
            raise
        return base64_str
    except:
        return 'Error,please make sure you have copy the image into clipboard and  try again!'


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Image to PNG base64")
        Dialog.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 10, 321, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Image to PNG base64", "Image to PNG base64"))
        self.pushButton.setText(_translate("Image to PNG base64", "GetBase64"))


class mainWindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

    def showResult(self):
        base64_str = getBase64()
        self.textBrowser.setText(base64_str)

if __name__ == '__main__':
    w = mainWindow()
    w.pushButton.clicked.connect(w.showResult)
    w.show()
    sys.exit(app.exec_())

