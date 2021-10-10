import sys

from PyQt5 import QtWidgets, QtGui

# QTGui resim ekleme gibi fonksiyonlar için şarttır


def pencere():
    app = QtWidgets.QApplication(sys.argv)
    # ******************************uygulama verilerini ekleme
    window = QtWidgets.QWidget()
    # *********************************uygulama window settings
    window.setWindowTitle("Watt Hesaplayıcı v2")
    window.setGeometry(
        1100, 100, 500, 500
    )  # pencerenin ekrandaki yerini ve boyutlarını ayarlamayı sağlar
    # **********************************etiket ayarlama
    header = QtWidgets.QLabel(
        window
    )  # Qlabel içerisine her zaman oluşturduğun parametreyi atıyorsun
    header.setText("Wattage Calculator")
    header.move(200, 0)
    # ***************************************Logolar
    vapoLogo = QtWidgets.QLabel(window)
    vapoLogo.setPixmap(QtGui.QPixmap("vapo.jpg"))  # resim ekleme komutu
    vapoLogo.setGeometry(100, 100, 100, 100)
    vapoLogo.move(50, 40)
    smokLogo = QtWidgets.QLabel(window)
    smokLogo.setPixmap(QtGui.QPixmap("smok.jpg"))
    smokLogo.setGeometry(100, 100, 100, 100)
    smokLogo.move(50, 150)
    elLogo = QtWidgets.QLabel(window)
    elLogo.setPixmap(QtGui.QPixmap("el.jpg"))
    elLogo.setGeometry(100, 100, 100, 100)
    elLogo.move(50, 250)
    # ******************etiket ayarlama bitiş
    # *********************************diğer
    window.show()  # pencereyi göstermeye yarar
    sys.exit(app.exec_())  # pencerenin sürekli çalışmasını sağlar


pencere()
