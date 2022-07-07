#aşağıdaki from ve import önadları ile dosyalarımız içerisindeki classları import ediyoruz.
from Personel import personel 
from YONETİCİ import yonetici
#belirlediğimiz şifreler ile giriş ve çıkış sağlanmalı.
yoneticiad = "1"
yoneticisifre = "1"
kullaniciad = "2"
kullanicisifre = "2"
#şifreleme işlemlerimizi yaparak giriş işlemimizi gerçekleştirmemiz gereken yerdir.
def giris():
    while True:

    
        print("          Giris yap\n      1-Yönetici Girisi\n      2-Personel Girisi")

        sec = input()
        #döngümüzle gerekli işlemleri kontrol ediyoruz.
        if sec == "1":
            ad = input("Kullanici adi: ")
            sifre = input("sifre: ")
            if (ad == yoneticiad and sifre == yoneticisifre):
                m = yonetici("ŞIRKET")

                #eğer doğru ise başlat fonksiyonuna yönlendiriyoruz.
                m.baslat()
            else:
                print("yanlis sifre girdiniz!\nlütfen tekrar ediniz.")
                pass
               
        elif sec == "2":
            ad = input("Kullanici adi: ")
            sifre = input("sifre: ")
            if (ad == kullaniciad and sifre == kullanicisifre):

                o = personel("ŞIRKET")
                o.baslat()
        else:
            print("Hatali tuslama yaptiniz. Tekrar deneyiniz.")

giris()
