import sys
from PyQt5 import QtWidgets
import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()


def tablo_olusturma():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS degisiklik(degistirme_tarihi TEXT,degistirilenler TEXT)"
    )


con.commit()
con.close()


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.my_ui()

    def my_ui(self):

        # self.socialMedia = QtWidgets.QLineEdit()
        self.userName = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(
            QtWidgets.QLineEdit.Password
        )  # yazılan şifrenin görülmemesi için kullanılır
        self.confirmButton = QtWidgets.QPushButton("Kaydet")
        self.yaziAlani = QtWidgets.QLabel("")
        self.setGeometry(
            1453, 450, 350, 350
        )  # buradaki değerlerin ilk ikisi ekrandaki konumunu ayarlar diğerleri açılan ekranın boyutunu

        verticalBox = QtWidgets.QVBoxLayout()
        verticalBox.addWidget(self.userName)
        verticalBox.addWidget(self.password)
        verticalBox.addWidget(self.confirmButton)
        verticalBox.addStretch()  # layoutlar arasında boşluk vermek için kullanılır
        verticalBox.addWidget(self.yaziAlani)

        horizantalBox = QtWidgets.QHBoxLayout()
        horizantalBox.addStretch()
        horizantalBox.addLayout(verticalBox)
        horizantalBox.addStretch()

        self.setLayout(horizantalBox)

        self.setWindowTitle("Kullanıcı arayüzü giriş programı")
        self.confirmButton.clicked.connect(self.login)
        self.show()

    def login(self):  # kullanicidan aldığımız verileri burda topluyoruz
        adi = self.userName.text()
        sifre = self.password.text()


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())
