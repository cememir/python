# defkullanici = "cem"
# defparola = "123"
# yeni_list = list(defkullanici)
# yenilist_parola = ["1", "2", "3"]
# print(yeni_list)
# print(yenilist_parola)
############################################################
listem = [1, 2, 3, 4, 5, 6]
print(listem)
############################################################
listem.append("append(9)")
print(listem, " ==== > listem.append(9)")
############################################################
listem.insert(1, "insert(1,9)")
print(listem, " ==== > listem.insert(1,9)")
############################################################
listem.pop(1)
print(listem, " ==== > listem.pop(1)")
listem.pop()
print(listem, " ==== > listem.pop()")
############################################################
print(listem * 3, " ==== > listem * 3")
print(listem, " ==== > listem")
############################################################

muslu_listesi = [35, 58]
toplu_listem = listem + muslu_listesi

print("listem + muslu_listesi   ====>>  ", toplu_listem)

############################################################
