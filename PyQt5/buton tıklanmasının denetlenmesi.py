import sys
from PyQt5 import QtWidgets

# ********************** Özet ******************
# .clear ile direkt olarak o alanı temizleyebiliyoruz
# .text ile yazılan şeyi alabiliyoruz


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # ***********************Qline edit ve butonlar******************************
        self.yazi_alani = (
            QtWidgets.QLineEdit()
        )  # Qt widgets da input almak için kullanıyoruz
        # -----------------------Qline edit ve butonlar------------------------------
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("Yazdır")

        verticalAllignment = QtWidgets.QVBoxLayout()
        verticalAllignment.addWidget(self.yazi_alani)
        verticalAllignment.addWidget(self.temizle)
        verticalAllignment.addWidget(self.yazdir)
        verticalAllignment.addStretch()  # altına boşluk bırakmak için
        self.setLayout(verticalAllignment)  # arayüze eklemek için kullandık

        self.setGeometry(150, 150, 150, 150)

        self.show()  # ekranda göstermek için kullanmak zorunludur

        self.temizle.clicked.connect(
            self.click
        )  # tıklanma fonksiyonu eklemek için kullanıyoruz
        self.yazdir.clicked.connect(
            self.click
        )  # tıklanma fonksiyonu eklemek için kullanıyoruz

    def click(self):
        # 2 tane ayrı tuş ataması yaptığımız için hangisine basıldığını algılamak adına sender adında bir fonksiyonu QWidget içerisinden çağırıyoruz
        sender = self.sender()

        if sender.text() == "Temizle":
            self.yazi_alani.clear()  # böyleylikle yazi alanına ne yazıldıysa temizlemiş oluyoruz.
        elif sender.text() == "Yazdır":
            print(self.yazi_alani.text())  # yazı alanındaki texti al demiş oluyoruz


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
