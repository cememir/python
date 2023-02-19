import random

yemek_listesi = ['pişi', 'yağlama']

for i in range(0, 5):
    secilen = random.choice(yemek_listesi)
    print(secilen)
