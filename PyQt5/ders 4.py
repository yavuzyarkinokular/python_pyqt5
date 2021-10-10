import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

# QTGui resim ekleme gibi fonksiyonlar için şarttır


def pencere():
    app = QtWidgets.QApplication(sys.argv)

    # ******************************uygulama verilerini ekleme
    window = QtWidgets.QWidget()

    # *********************************uygulama window settings
    window.setWindowTitle("Watt Hesaplayıcı v2")
    window.setGeometry(
        100, 100, 500, 500
    )  # pencerenin ekrandaki yerini ve boyutlarını ayarlamayı sağlar

    # ********************************* Hesapla buton ayarları
    buttonCalculate = QtWidgets.QPushButton(window)
    buttonCalculate.setText("Hesapla")
    buttonCalculate.move(150, 420)

    # ********************************************************buton ayarları bitiş
    # ********************************* Çıkış buton ayarları
    buttonExit = QtWidgets.QPushButton(window)
    buttonExit.setText("Çıkış")
    buttonExit.move(150, 420)

    # ********************************************************buton ayarları bitiş
    # *****************Horizantal  box ayarlama
    horBox = QtWidgets.QHBoxLayout()
    horBox.addWidget(buttonCalculate)
    horBox.addWidget(buttonExit)
    horBox.addStretch()  # pencere yana doğru açılsa bile butonların sağ veya sola yaslı kalmasını sağlar
    window.setLayout(horBox)

    # ******************************************************Horizantal  box ayarlama bitiş
    # *****************Vertical  box ayarlama
    verBox = QtWidgets.QVBoxLayout()
    verBox.addStretch()
    verBox.addWidget(buttonCalculate)
    verBox.addWidget(buttonCalculate)
    window.setLayout(verBox)

    # ****************************************************** Vertical  box ayarlama bitiş

    # **********************************etiket ayarlama
    header = QtWidgets.QLabel(
        window
    )  # Qlabel içerisine her zaman oluşturduğun parametreyi atıyorsun
    header.setText("Wattage Calculator")
    header.move(200, 0)
    # ******************etiket ayarlama bitiş

    # *********************************diğer
    window.show()  # pencereyi göstermeye yarar
    sys.exit(app.exec_())  # pencerenin sürekli çalışmasını sağlar
    # *********************************diğer bitiş


pencere()
