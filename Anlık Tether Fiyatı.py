import requests
from bs4 import BeautifulSoup as bs

url = "https://www.doviz.com/kripto-paralar/tether"

# URL'ye GET isteği gönder
yanit = requests.get(url)

# Sayfanın içeriğini BeautifulSoup ile ayrıştır
soup = bs(yanit.content, "html.parser")

# İlgili veriyi bul
veri_listesi = soup.find_all("div", {"class": "flex justify-between mt-8"})

# 'deger' değişkenini başta None olarak tanımlıyoruz
deger = None
arama_isareti = "₺"  # Belirli bir değeri ararken, değer başında genellikle '₺' olduğu için bu şekilde tanımlıyoruz

# Eğer gelen veri varsa
if veri_listesi:
    for veri in veri_listesi:
        metin = veri.text.strip()

        # Eğer aradığınız değer metin içinde varsa
        if arama_isareti in metin:
            # '₺' işaretinin bulunduğu metni al
            satirlar = metin.split("\n")  # Metni satırlara böler
            for satir in satirlar:
                if arama_isareti in satir:
                    deger = satir.strip()  # Belirli değeri ayıkla
                    break
            break

# 'deger' değişkenini yazdır
if deger:
    print("Güncel değer:", deger)
else:
    print("Aradığınız değer bulunamadı.")

print("Son deger:", deger)
