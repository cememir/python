import random

def kelime_tahmin_oyunu():
    kelimeler = ["elma", "armut", "muz", "çilek", "portakal"]
    secilen_kelime = random.choice(kelimeler)

    print("Kelime tahmin oyununa hoş geldiniz!")
    print("Kelimenin uzunluğu:", len(secilen_kelime))

    tahmin_edilen = []
    for _ in range(len(secilen_kelime)):
        tahmin_edilen.append("_")

    tahmin_hakki = 5
    while tahmin_hakki > 0:
        print(" ".join(tahmin_edilen))

        tahmin = input("Bir harf tahmin edin: ").lower()

        if len(tahmin) != 1:
            print("Yanlış giriş. Sadece bir harf girin.")
            continue

        if tahmin in tahmin_edilen:
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        if tahmin in secilen_kelime:
            for i in range(len(secilen_kelime)):
                if secilen_kelime[i] == tahmin:
                    tahmin_edilen[i] = tahmin

            if "_" not in tahmin_edilen:
                print("Tebrikler! Kelimeyi doğru tahmin ettiniz.")
                break
        else:
            tahmin_hakki -= 1
            print("Yanlış tahmin. Kalan hakkınız:", tahmin_hakki)

    if tahmin_hakki == 0:
        print("Maalesef, kelimeyi doğru tahmin edemediniz.")
        print("Doğru kelime:", secilen_kelime)

kelime_tahmin_oyunu()