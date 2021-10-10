import sqlite3
from typing import List

# ----------------------------------------------------- Özet ve Dipnotlar
# ************** Veri Alma***********
#  SELECT isim,soyisim FROM kullanici dersek eğer veritabanında sadece isim ve soyismi alır
# SELECT*FROM kullanici WHERE soyisim='Okular' dersek veritabanındaki soyismi sadece okular olanları alır
con = sqlite3.connect("library.db")
cursor = con.cursor()  # veritabanı üzerinde işlem yapabilmek için gerekli


def tablo_olustir():
    cursor.execute("CREATE TABLE kullanici(ad TEXT,soyad TEXT,yas INT)")
    con.commit()  # sorgunun veri tabanında geçerli olması için gerekli
    con.close()  # veritabanı bağlantısını koparıyoruz


# def veriEkle():
#     cursor.execute('INSERT INTO kullanici Values("Yavuz Yarkın","Okular",22)')
#     con.commit()
#     con.close()


def kullanicidanAlinan(isim, soyIsim, yas):
    cursor.execute(
        "   ",
        (
            isim,
            soyIsim,
            yas,
        ),  # değerleri fonksiyon içerisindeki parantezde yazdığım gibi ekliyorum
    )  # kullanıcıdan aldığım verileri buraya ekleyeceğim için sorguyu ? olarak bırakıyorum
    con.commit()
    con.close()


def kullaniciVeriAL():
    cursor.execute(
        "SELECT * FROM kullanici"
    )  # veritabanında ki bütün verileri çekiyoruz
    liste = (
        cursor.fetchall()
    )  # üst satırda çekilen verilerin bize döndürülmesi için kullanılıyor return komutu gibi
    print(
        "Veritabanına bağlantı başarılı.."
    )  # normalde con.commit kullanıyorduk ama veritabanı üzerinde işlem yapmacayacğımız için direkt olarak verilere erişebiliyoruz.
    for i in liste:
        print(i)  # görüntüyü daha açık hale getirmek için kullanılıyor


def tabloVeriGüncelle(eski_yas, yeni_yas):
    cursor.execute(
        "UPDATE kullanici set yas = ? WHERE yas = ?", (yeni_yas, eski_yas)
    )  # set dedikten sonra yeni parametreyi girmek istediğimizi belirmiş oluyoruz bu yüzden içerisine atacağımız değerlerin sırası da buna göre belilreniyor
    con.commit()


def veriSilme(soyad):
    cursor.execute("Delete From kullanici where soyad = ?", (soyad,))
    con.commit()


# ********** Kullanıcıdan veri talebi
# isim = input("İsminizi Giriniz:")
# soyIsim = input("Soy isminizi Giriniz:")
# yas = int(input("Yasinizi Giriniz: "))
# ************* Veri yazma
# kullanicidanAlinan(isim, soyIsim, yas)
# veriEkle()
# ---------------- Database den veri alma
kullaniciVeriAL()
# tabloVeriGüncelle(22, 23)
# veriSilme("Okular")
