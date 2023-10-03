import random

cevaplanan_soru_sayisi = 0
dogru_cevaplar = 0
soru_sayisi = 100

print("#" * 100)
print("Sorulara yalnızca rakam cevabı veriniz!")
print("Rakam yazılmazsa programdan çıkılır!")
print("#" * 100)

for _ in range(soru_sayisi):
    cevaplanan_soru_sayisi += 1


    sayi1 = random.randint(1, 10)
    sayi2 = random.randint(1, 10)
    islemler = ["+", "-", "*"]
    islem = random.choice(islemler)

    if islem == "+":
        sonuc = sayi1 + sayi2
    elif islem == "-":
        sonuc = sayi1 - sayi2
    else:
        sonuc = sayi1 * sayi2

    soru = f"{sayi1} {islem} {sayi2} = "

    try:
        cevap = int(input(soru))
    except:
        print("Sadece tam sayı kabul ediyorum!!!")
        exit()

    if cevap == sonuc:
        print("Tebrikler, doğru cevap!")
        dogru_cevaplar += 1
    else:
        print("Üzgünüm, yanlış cevap.")

    print("cevaplanan soru:", cevaplanan_soru_sayisi, "kalan", soru_sayisi-cevaplanan_soru_sayisi)

basari_orani = (dogru_cevaplar / soru_sayisi) * 100
print(f"\nBaşarı oranınız: {basari_orani}%")
