import cv2
from pyzbar.pyzbar import decode
import pygame
from datetime import datetime
import warnings

# Suppress ZBar alerts
warnings.filterwarnings('ignore')

# Specify the name and path of the audio file (the audio file can be a .wav or .mp3).
ses_dosyasi = 'C:/Users/seths/OneDrive/Masaüstü/Barkod Sistemi/a.mp3'

# Read the .txt file containing product information
with open('C:\\Users\\seths\\PycharmProjects\\pythonProject\\urunler.txt', 'r', encoding='utf-8') as file:
    urunler = {}
    for line in file:
        parts = line.strip().split(' ', 1)
        if len(parts) == 2:
            urun_bilgisi, barkod_fiyat = parts
            barkod, fiyat = barkod_fiyat.split(':')
            urunler[barkod] = {'urun_bilgisi': urun_bilgisi, 'fiyat': float(fiyat)}

# Use a dictionary to monitor the limit of reading each barcode once
okunan_barkodlar = {}
# Start the audio playback library
pygame.mixer.init()

cap = cv2.VideoCapture(0)  # Kameranın bağlantısını açın (0, varsayılan kamera).

# Get from the user how many products you will read
while True:
    try:
        toplam_urun_sayisi = int(input("Toplam kaç ürün okuyacaksınız: "))
        break
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

okunan_urun_sayisi = 0  # Okunan ürün sayısını izlemek için bir değişken
toplam_fiyat = 0  # Toplam satış fiyatını saklamak için bir değişken

# Collect information on products received and other data
alinan_urunler = []

while okunan_urun_sayisi < toplam_urun_sayisi:
    ret, frame = cap.read()  # Kameradan bir görüntü alın.

    # Barkodları tara ve çözümle.
    try:
        decoded_objects = decode(frame)
    except Exception as e:
        print("Barkod çözümleme hatası:", e)
        continue

    for obj in decoded_objects:
        barkod_data = obj.data.decode('utf-8')
        print("Barkod Okundu:", barkod_data)

        # Check if the barcode has been read before
        if barkod_data not in okunan_barkodlar:
            # Barkodun fiyatını .txt dosyasından alın.
            if barkod_data in urunler:
                urun_bilgisi = urunler[barkod_data]['urun_bilgisi']
                fiyat = urunler[barkod_data]['fiyat']
                print("Ürün Adı:", urun_bilgisi)
                print("Ürün Fiyatı:", fiyat)

                # Play the beep
                pygame.mixer.music.load(ses_dosyasi)
                pygame.mixer.music.play()

                # Mark the read barcode as read once
                okunan_barkodlar[barkod_data] = True

                # Count the barcode scanned and update the total price
                okunan_urun_sayisi += 1
                toplam_fiyat += fiyat

                # Save received products
                alinan_urunler.append({'urun_bilgisi': urun_bilgisi, 'barkod': barkod_data, 'fiyat': fiyat})
            else:
                print("Ürün bulunamadı.")
        else:
            print("Bu barkod daha önce okundu.")

    cv2.imshow('Barkod Okuma', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Print total selling price
print(f"{toplam_urun_sayisi} ürünün toplam fiyatı: {toplam_fiyat}")

# Ask about the money taken from the customer
while True:
    try:
        odeme = float(input("Müşteriden alınan parayı girin: "))
        break
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

# Calculate the amount to be returned and print it on the screen
geri_verilecek_tutar = odeme - toplam_fiyat
if geri_verilecek_tutar >= 0:
    print(f"Geri verilmesi gereken tutar: {geri_verilecek_tutar:.2f} TL")
else:
    eksik_tutar = abs(geri_verilecek_tutar)
    print(f"Müşteriden {eksik_tutar:.2f} TL daha almanız gerekiyor.")

# Get date and time information
tarih_ve_saat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Specify the directory of the a.txt file
dosya_dizini = '\\Users\\seths\\PycharmProjects\\pythonProject\\a.txt'

# Write data to a.txt file
with open(dosya_dizini, 'a', encoding='utf-8') as dosya:
    dosya.write(f"Tarih ve Saat: {tarih_ve_saat}\n")
    dosya.write("Alınan Ürünler:\n")
    for urun in alinan_urunler:
        dosya.write(f"   Ürün Adı: {urun['urun_bilgisi']}, Barkod: {urun['barkod']}, Fiyat: {urun['fiyat']}\n")
    dosya.write(f"Toplam Ürün Sayısı: {toplam_urun_sayisi}\n")
    dosya.write(f"Toplam Satış Fiyatı: {toplam_fiyat:.2f} TL\n")
    dosya.write(f"Alınan Para: {odeme:.2f} TL\n")
    dosya.write(f"Geri Verilen Tutar: {geri_verilecek_tutar:.2f} TL\n\n")
