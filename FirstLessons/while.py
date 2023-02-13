# bir liste oluşturalım
numbers = [1, 2, 3, 4, 5, "q", "w", "a",82.5,35.7]
# numbers = (1, 2, 3, 4, 5)
# numbers.append(9)

liste_eleman_sayisi = len(numbers)
print("liste_eleman_sayisi", liste_eleman_sayisi)

print("numbers[-1]", numbers[-1])
# while döngüsü ile listeyi yazdıralım
k = 0
while k < liste_eleman_sayisi:
    print(numbers[k])
    k += 1

# i = 0
# while i < 10:
#     print(f"i ==============> {i}")
#     i += 1
#     print(f"i += 1 {i}")


# agalarscom = ["emiremir", "tugkan", "omer", "cememir"]
# agalarscom = ("emiremir", "tugkan", "omer", "cememir")
