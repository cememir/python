agalarscom = ["emiremir", "tugkan", "omer", "cememir"]
# agalarscom = ("emiremir", "tugkan", "omer", "cememir")

for dongudekisira, arkadasim in enumerate(agalarscom):
    print(dongudekisira, arkadasim)
    if dongudekisira == 1:
        agalarscom[dongudekisira] = "goktug"

# agalarscom[1] = "goktug"

print(agalarscom)
for dongudekisira, arkadasim in enumerate(agalarscom):
    print(dongudekisira, arkadasim)

# sayilar_tuple = (1,2,3,4,5)
#
# for i in sayilar_tuple:
#     print(i)
#     if i < 4:
#         print(i, type(i))
#
# print("ikinci for")
# for i in sayilar_tuple:
#     print(i)
#     if i == 4:
#         print(i, type(i))
