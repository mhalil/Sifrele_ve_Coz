# =============================================================================
# "Sifre_icin_Sozluk_Olustur.py" dosyasi ile Olusturulan Sifreleme ve Cozme Sozlukleri Kullanılarak istenilen metinler Sifreleniyor ve Cozuluyor.
# "Sifre_icin_Sozluk_Olustur.py" dosyasi calistirildigi zaman Olusturulan benzersiz "Anahtar_Deger" ve "Deger_Anahtar" Sozluk icerikleri, asagidaki sozluk ile degistirilmeli !!! Ornek Sozlukler asagidadir.
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
    print("Çözülmüş Metin:", metnin_sifresiz_hali)

coz()

