def parolasor():
    defkullanici = "cem"
    defparola = "123"

    while True:
        kullanici = input("Kullanıcı Adı:")
        parola = input("Parola:")
        if (kullanici == defkullanici) and (parola == defparola):
            print("hoşgeldiniz", kullanici)
            break
        elif (kullanici != defkullanici) and (parola == defparola):
            print("Kullanici Adinda Bir Terslik Var")
        elif (kullanici == defkullanici) and (parola != defparola):
            print("Şifrenizi mi unuttunuz?")
            print("Şifrenizi değiştirmek ister misiniz?")
            cevap = input()

            if cevap == "E":
                yeniparola = input("Yeni Parola:")
                print("Lütfen Bekleyin")
                defparola = yeniparola
                print("Şifre başarıyla değiştirildi")

        else:
            print("Tekrar Deneyin")
