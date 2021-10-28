# =============================================================================
# Asagidaki karakterlerden olusan Alfabeden, Rastgele secim yapilarak Key ve Value iceren sozluk uretilecek. 
# Sifreleme ve cozme isleminde oluşturulacak Sozluk Üretiminde Kullanilacak olan (izin verilen) Karakterler
# alf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'q', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'Q', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z', '+', '-', '*', '/', '!', "'", '^', '%', '&', '(', ')', '=', '?', '#', '$', '{', '}', '[', ']', '\\', '_', '|', ' ', ":", ";", "`", "~", "@", "₺", "€", "£", '"']
# =============================================================================

import random

alf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'q', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'Q', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z', '+', '-', '*', '/', '!', "'", '^', '%', '&', '(', ')', '=', '?', '#', '$', '{', '}', '[', ']', '\\', '_', '|', ' ', ":", ";", "`", "~", "@", "₺", "€", "£", '"']

keys = ""
values = ""

sozluk_key = {} # Metin şifrelerken kullanılacak sözlük
sozluk_value = {} # Şifreli metin çözülürken kullanılacak sözlük

while len(keys) < len(alf): # Rastgele seçimler yaparak, benzersiz (tekrarlamasiz) karakterleri "keys" stingine ekle.
    secim = random.choice(alf)
    if secim not in keys:
        keys += secim

while len(values) < len(alf): # Rastgele seçimler yaparak, benzersiz (tekrarlamasiz) karakterleri "values" stingine ekle.
    secim = random.choice(alf)
    if secim not in values:
        values += secim

for indis in range(len(alf)): # rastgele oluşturulan "keys" ve "values" stringlerindeki ayni indisteki karakterleiri eşleyerek sozluk yapılarını olustur.
    sozluk_key[keys[indis]] = values[indis]
    sozluk_value[values[indis]] = keys[indis]
    
print("Anahtar_Deger =", sozluk_key)    
print("Deger_Anahtar =", sozluk_value)    

