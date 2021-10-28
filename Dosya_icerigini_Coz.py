# =============================================================================
# Oncelikle "Sifre_icin_Sozluk_Olustur.py" dosyasi ile Sifreleme ve Cozme Sozlukleri Olusturuluyor ve olusan bu sozlukller "Sozluk.py" dosyasina kopyalaniyor.
# Kodlarin hatasiz calisabilmesi icin "Dosyayi_Sifrele.py" dosyasi ile Koda dahil edilen "Sozluk.py" dosyasi ayni dizinde bulunmali.
# Kod calistirildigi zaman, Ayni dizinde bulunan "Sifreli.txt" dosya icerigi Cozulerek ekrana yazdirilir.
# =============================================================================

import Sozluk

def coz(cozulecek_metin):
    metnin_sifresiz_hali = ""
    for karakter in cozulecek_metin[:-1]:
        metnin_sifresiz_hali += Sozluk.Deger_Anahtar[karakter]
    return metnin_sifresiz_hali

with open("Sifreli.txt", "r", encoding="UTF-8") as dosya:
    icerik = dosya.readlines()

    for satir in icerik[:-1]:
        print(coz(satir))