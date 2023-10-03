import datetime
import time

alarm_saati = "10:13:55" #input("Alarm saati (HH:MM:SS) formatında girin: ")

while True:
    zaman = datetime.datetime.now()
    suanki_zaman = zaman.strftime("%H:%M:%S")
    print("suanki_zaman",suanki_zaman)
    if suanki_zaman < alarm_saati:
        print("daha var")
    if suanki_zaman == alarm_saati:
        print("tam zamanı")
    if suanki_zaman > alarm_saati:
        print("zaman geçti")
        break

    time.sleep(1)