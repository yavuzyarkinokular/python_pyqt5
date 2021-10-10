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

    # *********************************buton ayarları
    button = QtWidgets.QPushButton(window)
    button.setText("Hesapla")
    button.setGeometry(150, 500, 200, 80)
    button.move(150, 420)

    # *********************************buton ayarları bitiş

    # **********************************etiket ayarlama
    header = QtWidgets.QLabel(
        window
    )  # Qlabel içerisine her zaman oluşturduğun parametreyi atıyorsun
    header.setText("Wattage Calculator")
    header.move(250, 0)
    # ******************etiket ayarlama bitiş

    # *********************************diğer
    window.show()  # pencereyi göstermeye yarar
    sys.exit(app.exec_())  # pencerenin sürekli çalışmasını sağlar
    # *********************************diğer bitiş


pencere()
