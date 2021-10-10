# Artık dersler daha komplike olacağı için pencere classı üretilecek
import sys
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()  # burada artık miras aldığım Qwidgetı çalıştırmış oldum
        self.init_ui()  # bunu yaparak aslında her işimi init ui içerisinde yapacak olduğumu programa bildiriyorum

    def init_ui(self):

        self.yazi_alani = QtWidgets.QLabel("Wattage Calculator")
        self.calculateButton = QtWidgets.QPushButton("Click me!")
        self.say = 0  # butona ne kadar tıklandığını saymak adına ekliyorum

        verticalAllignment = QtWidgets.QVBoxLayout()
        verticalAllignment.addWidget(self.yazi_alani)
        verticalAllignment.addWidget(self.calculateButton)
        verticalAllignment.addStretch()

        horizantalAllignment = QtWidgets.QHBoxLayout()
        horizantalAllignment.addLayout(verticalAllignment)
        horizantalAllignment.addStretch()

        self.setGeometry(500, 500, 500, 500)
        self.setLayout(
            horizantalAllignment
        )  # diğer aşamalarda nasıl ki pencerenin içerisine atıyorsak burda da self.setLayout yaparak pencerenin içerisine dahil ediyoruz
        self.calculateButton.clicked.connect(
            self.click
        )  # bu butona tıklandığında parantez içerisindeki bir fonksiyona bağlan demiş oluyorum
        self.show()

    def click(self):
        self.say += 1
        self.yazi_alani.setText("İşlem Gerçekleşti" + str(self.say) + "defa tıklandı")


# Bunları görebilmek için öncelikle uygulama oluşturmamız gerekiyor
app = QtWidgets.QApplication(sys.argv)  # sys.argv  argümanları yollamak için
pencere = Pencere()
sys.exit(app.exec_())  # uygulamayı döngüye sokmak için app.exec_() kullanıyoruz
