def sinav_notu_toplam(ilksinav, ikincisinav, hocanotu):
    return ilksinav + ikincisinav + hocanotu


def sinav_notu_ortalama(ilksinav, ikincisinav, hocanotu):
    return (ilksinav + ikincisinav + hocanotu) // 3


print(sinav_notu_toplam(hocanotu=58, ikincisinav=100, ilksinav=100))

# print(sinav_notu_ortalama(58, 100, 100))

# def emirgur():
#     print("def topla üst")
#     print(5+9)
#     print("def topla alt")
# def omer():
#     print("def omer üst")
#     print(5+9)
#     print("def omer alt")
#
# print("üst omer()")
# #omer()
# print("alt omer()")
#
# emirgur()
