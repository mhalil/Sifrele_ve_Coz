# =============================================================================
# Oncelikle "Sifre_icin_Sozluk_Olustur.py" dosyasi ile Sifreleme ve Cozme Sozlukleri Olusturuluyor ve olusan bu sozlukller "Sozluk.py" dosyasina kopyalaniyor.
# Kodlarin hatasiz calisabilmesi icin "Dosyayi_Sifrele.py" dosyasi ile Koda dahil edilen "Sozluk.py" dosyasi ayni dizinde bulunmali.
# Sifrelemek istenilen metin, ayni dizindeki "Sifreler.txt" dosyasina yazilmali ya da eklenmeli.
# =============================================================================

import Sozluk

def sifrele(sifrelenecek_metin):
    metnin_sifreli_hali = ""         
    for karakter in sifrelenecek_metin[:-1]:
        metnin_sifreli_hali += Sozluk.Anahtar_Deger[karakter]
    return metnin_sifreli_hali

with open("Sifreler.txt", "r", encoding="UTF-8") as dosya:
    liste = dosya.readlines()

    with open("Sifreli.txt", "w", encoding="UTF-8") as belge:
        for satir in liste:
            belge.write(sifrele(satir)+"\n")

print("Şifreleme İşlemi Tamamlandı.!")
