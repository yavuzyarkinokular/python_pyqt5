import sys

from PyQt5 import QtWidgets


def pencere():
    app = QtWidgets.QApplication(sys.argv)
    penc = QtWidgets.QWidget()
    penc.setWindowTitle("Watt Hesaplayıcı")
    penc.show()
    sys.exit(app.exec_())


pencere()
