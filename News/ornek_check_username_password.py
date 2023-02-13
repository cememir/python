# Kullanıcı adı ve parola sözlüğü
user_pass = {"user1": "password1", "user2": "password2", "user3": "password3"}

tamam_artik_parola_ve_username_var = False

while not tamam_artik_parola_ve_username_var:

    # Kullanıcı adı ve parolayı alma
    username = input("Kullanıcı Adı: ")
    password = input("Parola: ")


    # Kullanıcı adı ve parolayı kontrol etme
    if username in user_pass:
        if password == user_pass[username]:
            print("Giriş Başarılı\n")
            tamam_artik_parola_ve_username_var = True
        else:
            print("Parola yanlış\n\n")
    else:
        print("Kullanıcı adı bulunamadı\n\n\n")
