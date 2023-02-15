defkullanici = "cemir"
defparola = "123"

print("babaloşko hoşgeldin:)")

kullanici = input("kullanıcı adı:\t")
parola = input("parolanız:\t")

if (defkullanici == kullanici) and (parola == defparola):
    print("baba nasılsın?")
elif (defkullanici != kullanici) and (parola == defparola):
    print("baba bundan sonra oyun oynayabilir miyim?")
elif (defkullanici == kullanici) and (parola != defparola):
    print("baba iyi misin?")
else:
    print("çok yanlış yaptın")
