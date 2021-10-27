
# =============================================================================
# Asagidaki 97 adet karakter bulunan Alfabeden, Rastgele secim yapılarak Key ve Value içeren sozluk üretilecek. 
# Sifreleme ve cozme isleminde oluşturulacak Sozluk Üretiminde Kullanilacak olan (izin verilen) Karakterler
# alf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'q', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'Q', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z', '+', '-', '*', '/', '!', "'", '^', '%', '&', '(', ')', '=', '?', '#', '$', '{', '}', '[', ']', '\\', '_', '|', ' ']
# =============================================================================

import random

alf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'q', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'Q', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z', '+', '-', '*', '/', '!', "'", '^', '%', '&', '(', ')', '=', '?', '#', '$', '{', '}', '[', ']', '\\', '_', '|', ' ']

keys = ""
values = ""

sozluk_key = {}     # Metin şifrelerken kullanılacak sözlük
sozluk_value = {}   # Şifreli metin çözülürken kullanılacak sözlük

while len(keys) < len(alf):     # Rastgele seçimler yaparak, benzersiz (tekrarlamasiz) karakterleri "keys" stingine ekle.
    secim = random.choice(alf)
    if secim not in keys:
        keys += secim

while len(values) < len(alf):   # Rastgele seçimler yaparak, benzersiz (tekrarlamasiz) karakterleri "values" stingine ekle.
    secim = random.choice(alf)
    if secim not in values:
        values += secim

for indis in range(len(alf)):   # rastgele oluşturulan "keys" ve "values" stringlerindeki ayni indisteki karakterleiri eşleyerek sozluk yapılarını olustur.
    sozluk_key[keys[indis]] = values[indis]
    sozluk_value[values[indis]] = keys[indis]
    
#print("Anahtar_Deger =", sozluk_key)    
#print("Deger_Anahtar =", sozluk_value)    

# =============================================================================
# Yukarıdaki kodlar ile Oluşturulan Şifreleme ve Çözme Sözlükleri Kullanılarak istenilen metinler Şifreleniyor ve çözülüyor.
# =============================================================================

Anahtar_Deger = {'h': 'k', 'W': '$', 'ş': '_', 'Ş': 'A', 'F': ' ', 'L': '#', '-': '&', '|': 'Ü', '*': '^', 'Z': 'T', '%': 'B', ']': '/', 't': '+', 'X': '-', '2': '2', 'M': 'ö', 'g': 'c', '9': 'H', 'P': 'z', '[': 'r', ' ': 'D', 'y': 'i', '$': ']', '5': 'n', '6': 'Ş', 'I': 'a', '/': 'Ç', 'Y': '=', 'S': 'K', 'Q': "'", 'ö': 'F', '\\': 'v', 'Ö': 'W', 'T': 'x', 'Ü': 'p', 'o': '1', 'ı': 'S', 'a': '\\', 'R': 'P', 'l': 'ç', '+': 'm', 'J': 'E', '7': '3', '3': 'j', '(': '0', 'C': 't', 'Ç': 'I', 'B': 'Ö', 'N': '8', 'k': 'Y', 'f': '5', '^': 'q', 'r': '9', '_': 'G', 's': '{', '8': 'Q', 'ü': 'e', '1': 'N', '4': '|', 'K': 'l', 'ç': 'u', 'q': '!', 'H': 'Ğ', 'j': 'U', '!': '*', '&': 'y', 'c': '}', '}': '[', '0': 'X', 'O': 'o', 'x': 'İ', 'd': '?', 'E': 'M', 'b': 'g', 'Ğ': 'ı', 'İ': '6', 'G': 'J', ')': 'ğ', 'p': 'w', '?': '%', 'V': 'O', 'i': 'ş', 'w': 's', 'A': '7', 'z': 'ü', 'n': 'd', '{': 'h', '#': 'L', 'ğ': '(', 'm': 'Z', 'U': 'b', 'e': 'R', '=': '4', "'": ')', 'v': 'V', 'u': 'C', 'D': 'f'}
             
Deger_Anahtar = {'k': 'h', '$': 'W', '_': 'ş', 'A': 'Ş', ' ': 'F', '#': 'L', '&': '-', 'Ü': '|', '^': '*', 'T': 'Z', 'B': '%', '/': ']', '+': 't', '-': 'X', '2': '2', 'ö': 'M', 'c': 'g', 'H': '9', 'z': 'P', 'r': '[', 'D': ' ', 'i': 'y', ']': '$', 'n': '5', 'Ş': '6', 'a': 'I', 'Ç': '/', '=': 'Y', 'K': 'S', "'": 'Q', 'F': 'ö', 'v': '\\', 'W': 'Ö', 'x': 'T', 'p': 'Ü', '1': 'o', 'S': 'ı', '\\': 'a', 'P': 'R', 'ç': 'l', 'm': '+', 'E': 'J', '3': '7', 'j': '3', '0': '(', 't': 'C', 'I': 'Ç', 'Ö': 'B', '8': 'N', 'Y': 'k', '5': 'f', 'q': '^', '9': 'r', 'G': '_', '{': 's', 'Q': '8', 'e': 'ü', 'N': '1', '|': '4', 'l': 'K', 'u': 'ç', '!': 'q', 'Ğ': 'H', 'U': 'j', '*': '!', 'y': '&', '}': 'c', '[': '}', 'X': '0', 'o': 'O', 'İ': 'x', '?': 'd', 'M': 'E', 'g': 'b', 'ı': 'Ğ', '6': 'İ', 'J': 'G', 'ğ': ')', 'w': 'p', '%': '?', 'O': 'V', 'ş': 'i', 's': 'w', '7': 'A', 'ü': 'z', 'd': 'n', 'h': '{', 'L': '#', '(': 'ğ', 'Z': 'm', 'b': 'U', 'R': 'e', '4': '=', ')': "'", 'V': 'v', 'C': 'u', 'f': 'D'}

def sifrele():
    metnin_sifreli_hali = ""
    sifrelenecek_metin = input("Şifrelenecek Metni yazın: ")          

    for karakter in sifrelenecek_metin:
        metnin_sifreli_hali += Anahtar_Deger[karakter]
    print("Şifreli Metin:", metnin_sifreli_hali)
    
sifrele()
    
def coz():
    metnin_sifresiz_hali = ""
    cozulecek_metin = input("Cozulecek Metni yazın: ")          

    for karakter in cozulecek_metin:
        metnin_sifresiz_hali += Deger_Anahtar[karakter]
    print("Çözülmüş Metin", metnin_sifresiz_hali)

coz()