# sozluk = {'isim': 'muslu', 'yas': 40}
# print(sozluk)
# print(sozluk['isim'])

aranan_arkadas = input("hangi arkadaş\n\n")
# aranan_arkadas = "emirgür"

sinif_arkadaslarim = {'isimler': ['muslu', 'emirgür', 'ömer'], 'yaslar': [40, 9, 10]}
sinif_arkadaslarim_isimleri = sinif_arkadaslarim['isimler']
sinif_arkadaslarim_yaslari = sinif_arkadaslarim['yaslar']

if aranan_arkadas in sinif_arkadaslarim_isimleri:

    index = sinif_arkadaslarim_isimleri.index(aranan_arkadas)

    yasi_kac = sinif_arkadaslarim_yaslari[index]

    print(aranan_arkadas, "listede bulundu. Sırası:", index, "yaşı : ", yasi_kac)
else:
    print(aranan_arkadas, "listede bulunamadı.")




# print(sinif_arkadaslarim)
# print(sinif_arkadaslarim['isimler'])
# print(sinif_arkadaslarim['isimler'][0][2])


# print(omer)
# print(sinif_arkadaslarim['yas'])
# print(sinif_arkadaslarim['yas'][2])
