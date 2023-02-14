import requests


def websitesi_ac(url="http://google.com.au/", return_format="json"):
    response = requests.get(url)
    status_code = response.status_code
    if status_code == 200:
        # print(status_code)  # http status code https://tr.wikipedia.org/wiki/HTTP_durum_kodlar%C4%B1
        # print(response.url)  # request url
        # print(response.headers)  # http headers https://en.wikipedia.org/wiki/List_of_HTTP_header_fields

        if return_format == "text":
            return response.text
        elif return_format == "json":
            return response.json()
        else:
            pass
    else:
        return "sayfa yüklenemedi"


def websitesi_ac_parametreli(url, parametre):
    response = requests.get(url, params=parametre, allow_redirects=True)
    status_code = response.status_code
    if status_code == 200:
        print(status_code)  # http status code https://tr.wikipedia.org/wiki/HTTP_durum_kodlar%C4%B1
        print(response.url)  # request url
        print(response.headers)  # http headers https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
        return response.text
    else:
        return "sayfa yüklenemedi"


def websitesine_data_gonder(url, body):
    """
    Bu fonksiyon tarayıcıda bir web sitesi sayfasına veri göndermek ile aynıdır
    - Örn: Giriş formuna kullanıcı adı parola göndermek ve post işleminden sonraki sayfaya giriş izin durumu

    :param url:
    :param body:
    :return:
    """
    return requests.post(url, data=body).text


# websitesi_html_kodlari = websitesi_ac("https://google.com.tr")
websitesi_html_kodlari = websitesi_ac("https://httpbin.org/uuid", return_format="json")
# websitesi_html_kodlari = websitesi_ac_parametreli("https://httpbin.org/get", "kid1&renk=mor")
# websitesi_html_kodlari_dict = websitesi_ac_parametreli("https://google.com.tr/search", {"q": "muslu yüksektepe django"})

print(websitesi_html_kodlari)
# print(websitesi_html_kodlari_dict)
