from classdeneme import taseron

#CLASS
class kurucu(taseron):
    
    #CONSTRUCTER
    def __init__(self,ad):
        self.ad=ad
        self.calisma=True
    #mainde gerekli işlemleri gerçekleştirdikten sonra başlat fonksiyonumuza yönlendiriliyoruz.
    #başlat fonksiyonumuz ise bizi menusecim'e yönlendirmektedir.
    def baslat(self):
        self.menusecim()
    
    def program(self, secim):
        #program fonksiyonumuzda ise gerekli karar blokları ile koşullarımızı belli ediyoruz.Ve gerekli 
        #şartlar sağlandıysa kullanıcının seçimine yönlendiriliyoruz.
                                                                 
        if secim==1:
            self.calisanekle()

        elif secim==2:
            self.calisancikar()

        elif secim==3:
            ay_yil_secim=input("YILLIK OLARAK DEGERLERİ GÖRMEK İSTERMİSİNİZ?(e/h)")
            if ay_yil_secim=="e":
                self.verilecekmaasgoster(hesap="y")
            else:
                self.verilecekmaasgoster()  

        elif secim==4:
            self.maaslariver()

        elif secim==5:
            self.masrafgir()
        elif secim==6:
            self.gelirgir()
        elif secim == 7:
            self.sikayetoku()
        elif secim==8:
            self.taseronfirma()    
          
        elif secim ==9:
            self.cikis()     


    #aşağıdaki menüsecim fonksiyonumuz ile gereken secimler icin verilen karar bloğu ve döngümüz mevcuttur.
    def menusecim(self):
        secim=int(input("{} OTOMASYONUMUZA HOŞGELDİNİZ\n\n1-ÇALIŞAN EKLE\n2-ÇALŞAN ÇIKAR\n3-VERİLECEK MAAŞ\n4-MAAŞLARI VER\n5-MASRAF GİR\n6-GELİR GİR\n7-ŞİKAYETLERİ OKU\n8-TAŞERON FİRMALAR\n9-ÇIKIŞ\nLÜTFEN BİR SEÇİM YAPINIZ:".format(self.ad)))
        # print("\ncalisti\n", secim)
        # if (type(input) == "int")
        while secim < 1 or secim >9:
            secim=input("lütfen 1-9 arasında belirtilen seçeneklerden birini giriniz:")
            return secim
        #eğer gerekli şartları yerine getirdiysek program fonksiyonuna yönlendiriliyoruz.
        return self.program(secim)

    #eğer seçimimiz 1'den yanaysa program fonksiyonundan.calisanekle fonksiyonumuza yönlendiriliyoruz.
    # def calisanekle(self):
    #     id=1
    #     ad=input("CALİSANIN ADINI GİRİNİZ:")
        
    #     soyad=input("CALİSANIN SOYADINI GİRİNİZ:")
        
    #     yas=input("CALİSANIN YASINI GİRİNİZ:")
        
    #     cinsiyet=input("CALİSANIN CİNSİYETİNİ GİRİNİZ:")
        
    #     maas=input("CALİSANIN MAASINI GİRİNİZ:")


    #     #dosya okuma işlemleri yapıyoruz.
    #     with open(r"C:\Users\fayik\Desktop\ana_proje1\calisanlar.txt","r") as dosya:
    #        calisanlistesi=dosya.readlines()

    #     #    print(calisanlistesi)
    #     if len(calisanlistesi)==0:
    #         id=1
    #     else:
    #         #gerekli  veriler dosyada analiz ediliyor ve şartlarımızı sağlıyorlar.
    #         #dosya okuma işlemi için açılan dosyadır
    #         #id'nin hesaplaması burada yapılır.
    #         with open(r"C:\Users\fayik\Desktop\ana_proje1\calisanlar.txt","r") as dosya:
    #             id=int(dosya.readlines()[-1].split(":")[0]) +1
    #     #dosya okuma işlemi için açılan dosyadır.
    #     #dosya yazdırma işlemi burada yapılır.
    #     #dosyadaki verilerin hangi düzene göre sıralanacağı belli edilir.
    #     with open(r"C:\Users\fayik\Desktop\ana_proje1\calisanlar.txt","a+") as dosya:
    #         dosya.write("{}:{}--{}--{}--{}--{}\n".format(id,ad,soyad,yas,cinsiyet,maas))
    #     #calisanekle metodumuza gerekli değerleri girdikten sonra.
    #     #ekrana var olan kullanıcıların yazdırılması işlemi yapılır.
    #     #readlines komutu ile dosyamızı satır satır okuyabiliyoruz.
    #     with open(r"C:\Users\fayik\Desktop\ana_proje1\calisanlar.txt","r") as dosya:
    #        calisanlistesi=dosya.readlines()
    #         #aşağıdaki döngü ile dosyamız alt alta ve göze hitab edecek şekilde görüntülenmesi sağlanıyor.
    #        for i in calisanlistesi:
    #         print(i)
    #     #gerekli işlemleri yerine getirdikten sonra otomatik olarak.Menüye dönüş sağlıyoruz.    
    #     self.menusecim()

    
    def verilecekmaasgoster(self,hesap="a"):
        #dosyadan gerekli okuma işlemleri yapılıyor.
        with open(r"C:\Users\fayik\Desktop\simple_company_management\calisanlar.txt","r") as dosya:
            #satır satır okuma işlemi.
            calisanlar=dosya.readlines()
        #maaslar adında bir dizi olşturuyoruz ve gereken işlemlerim için ortam hazırlamış oluyoruz.   
        maaslar=[]
        #döngümüzü yine calisanlar içerisinde dolaştırıyoruz.        
        for calisan in calisanlar:
            #0'dan geriye doğru sayıp -1.indekse kadar olan aralıkta "--" çift tire işaretini arıyoruz.
            a = str(calisan.split("--")[-1][0:-1])
            #alınan değer veriler analiz edilerek alındığı için int bir maas degerimiz olacaktır ve bunu kayıtlı tutuyoruz.
            a = int(a)
            #maaslar dizimize append ile sayısal olarak girdiğimiz maaş değerlerimizi append fonksiyonu ile kaydediyoruz.
            maaslar.append(a)
            #fonksiyon içerisinde tanımladığımız string "a" değerini burada istenen bir durum için koşul yapısına sokuyoruz.
            #tabi buradaki durumumuzun kontrolü için menü seçime gitmemiiz gerekiyor.
            #eğer seçimimiz "a" dan yanaysa personellerin aylık maaşını ekrana yazdıracaktır.
        if hesap=="a":

            print("BU AY ÖDENMESİ GEREKEN MAAŞ:{}".format(sum(maaslar)))
            #değilse personelin senelik toplam maaşlarını ekrana yazdıracaktır.
        else:
            print("BU YIL ÖDENMESİ GEREKEN MAAŞ:{}".format(sum(maaslar)*12))
        pass
        #işlemlerimiz bittikten sonra menu secime geri dönüyoruz.
        self.menusecim()
    #menusecimde maaslariver'i seçtikten sonra program()ile buraya yönlendiriliyoruz.    
    def maaslariver(self):
        #dosyayı okuma modunda açmak için dosya yolunu ve gerekli ifadeleri kullanırız.
        with open(r"C:\Users\fayik\Desktop\simple_company_management\calisanlar.txt","r") as dosya:
            #calisanlar ile dosyamızı satır satır okuruz.
            calisanlar=dosya.readlines()
        #maaslar adıyla açtığımız diziyi kayıt için tutarız.    
        maaslar=[]
        #döngü içerisinde gerekli verileride analiz ederek döneriz.
        for calisan in calisanlar:
            #split fonksiyonu ile "--" çift tire işaretini her indis değeri için aşama olarak seçeriz.
        #Ve karakter saymaya geriye doğru sayarak split metodumuza göre -1.indis bizim maaş değerlerimizi tuttuğumuz indistir.
            maaslar.append(int(calisan.split("--")[-1]))
        #toplammaas adındaki değişken ile maaslar dizimizin içerisine for döngüsü ile kaydettiğimiz değerlerin toplamını veriyoruz.        
        toplammaas=sum(maaslar)
        #şimdi butce.txt dosyamızın sadece okuma işlemlerini yapıyoruz.
        with open(r"C:\Users\fayik\Desktop\simple_company_management\butce.txt","r") as dosya:
            #tbutce adını verdiğimiz değişken ile butce.txt dosyamızı satır satır okutuyoruz.
            #ve zaten .txt dosyamızda sadece tek bir değer olduğu için 0.indeks işimizi görüyor
            tbutce=int(dosya.readlines()[0])
        #tbutce değerimizden,hesaplamasını yaptığımız toplammaas değerini çıkarıyoruz.    
        tbutce=tbutce-toplammaas
        #ve print fonksiyonu ile tbutce değerimizi ekrana yazdırıyoruz.    
        print("toplambutce",tbutce)
        #butce.txt dosyamıza bütçemizin son halini yazdırmak için dosyamızı hem okuma hemde yazma işlemi için hazır duruma getiriyoruz.
        with open(r"C:\Users\fayik\Desktop\simple_company_management\butce.txt","w") as dosya:
            #yazdırma işlemini burada gerçekleştiriyoruz.
            dosya.write(str(tbutce))
        #işlemlerim bittikten sonra menusecim fonksiyonuna geri dönüyorum.
        self.menusecim()
        
    #menusecim() ve program() ile gerekli koşullar sağlandıktan sonra masrafgir() fonksiyonuna yönlendiriliyoruz.
    def masrafgir(self):
        #int(tamsayı) değişken türü ile masraf değerimizi kullanıcan alıyoruz.
        masraf=int(input("GİDERLERİ GİRİNİZ:"))
        #masraf değerini kullanıcıdan aldıkatan sonra,dosya okuma işlemimize geçiyoruz.
        with open("butce.txt","r") as dosya:
            #daha öncede bahsettiğimiz gibi butce.txt dosyamızda sadece bütçe tutuyoruz.Bundan doalyı 0.indeks işimizi görür hale geliyor.
            tbutce=int(dosya.readlines()[0])
        #veri analizleyerek okuduğumuz tbutce değerimizden,kullanıcıdan alınan masraf değerini çıkarıyoruz.    
        tbutce=tbutce-masraf
        #burada ise gerekli işlemlerden sonra,elde edilen son değeri .txt uzantılı dosyamıza yazdırıyoruz.   
        with open("butce.txt","w") as dosya:
            #yazdırma işlemimiz burada gerçekleşiyor.
            dosya.write(str(tbutce))       
        pass
        #işlemlerimizi gerçekleştirdikten sonra menusecim()'e geri dönüyoruz.
        self.menusecim()

    #menusecim() ve program() ile yönlendiriliyoruz.
    #bu fonksiyon ile kullanıcıdan gelir girmesini bekliyoruz.
    def gelirgir(self):
        #gelir değerini kullanıcıdan tamsayı değşken türü ile alıyoruz.
        gelir=int(input("GELİRİN TOPLAMINI GİRİNİZ:"))
        #butce.txt dosyamızda okuma işlemlerini gerçekleştiryoruz.
        with open("butce.txt","r") as dosya:
            #0.indisteki veriyle işlem göreceğimiz için veri analizini 0.indise göre ayarlıyoruz.
            tbutce=int(dosya.readlines()[0])
        #elle girmiş olduğumuz veriyi,tbutce ile okuyup tuttuğumuz veriye ekliyoruz.    
        tbutce=tbutce+gelir
        #ve yazdırma işlemi gerekli dosya okuma işlemini gerçekleştiryoruz.   
        with open("butce.txt","w") as dosya:
            #yazdırma işlemi burada gerçekleşir.
            dosya.write(str(tbutce))
        pass
        #gerekli koşullar sağlandıktan,ve fonkisyon ile işimiz bittikten sonra çıkış için menusecim()'e yönlendiriliyoruz.
        self.menusecim()

    #menusecim() ve program() ile gerekli atamaları yaptıktan sonra bizi sikayetoku() fonksiyonuna yönlendiriyor. 
    def sikayetoku(self):
        #dosyamızı okuma işlemini burada gerçekleştiriyoruz.
        with open(r"C:\Users\fayik\Desktop\simple_company_management\sikayet_dosyası.txt", "r") as f:
           #okuma adını verdiğimiz değişken ile satır satır okuma işlemini gerçekleştiriyoruz.
            read = f.readlines()
            #döngüde read içerisinde i değişkenini döndürüyoruz. 
            for i in read:
                print(i)
        #gerekli işlemleri hallettikten sonra menusecim() fonksiyonuna gidiyoruz.        
        self.menusecim()
    
    def cikis(self):

        import main
        
        main.giris()

# sirket objemizdir.
# sirket=şirket("darkproject")        

# while sirket.calisma:
#     sirket.program()

class yonetici(kurucu):
    def __init__(self, ad):
        self.ad = ad  


    def calisanekle(self):
        id=1
        ad=input("CALİSANIN ADINI GİRİNİZ:")
        
        soyad=input("CALİSANIN SOYADINI GİRİNİZ:")
        
        yas=input("CALİSANIN YASINI GİRİNİZ:")
        
        cinsiyet=input("CALİSANIN CİNSİYETİNİ GİRİNİZ:")
        
        maas=input("CALİSANIN MAASINI GİRİNİZ:")


        #dosya okuma işlemleri yapıyoruz.
        with open(r"C:\Users\fayik\Desktop\simple_company_management\calisanlar.txt","r") as dosya:
           calisanlistesi=dosya.readlines()

        #    print(calisanlistesi)
        if len(calisanlistesi)==0:
            id=1
        else:
            #gerekli  veriler dosyada analiz ediliyor ve şartlarımızı sağlıyorlar.
            #dosya okuma işlemi için açılan dosyadır
            #id'nin hesaplaması burada yapılır.
            with open(r"C:\Users\fayik\Desktop\simple_company_management\calisanlar.txt","r") as dosya:
                id=int(dosya.readlines()[-1].split(":")[0]) +1
        #dosya okuma işlemi için açılan dosyadır.
        #dosya yazdırma işlemi burada yapılır.
        #dosyadaki verilerin hangi düzene göre sıralanacağı belli edilir.
        with open(r"C:\Users\fayik\Desktop\simple_company_management\calisanlar.txt","a+") as dosya:
            dosya.write("{}:{}--{}--{}--{}--{}\n".format(id,ad,soyad,yas,cinsiyet,maas))
        #calisanekle metodumuza gerekli değerleri girdikten sonra.
        #ekrana var olan kullanıcıların yazdırılması işlemi yapılır.
        #readlines komutu ile dosyamızı satır satır okuyabiliyoruz.
        with open(r"C:\Users\fayik\Desktop\simple_company_management\calisanlar.txt","r") as dosya:
           calisanlistesi=dosya.readlines()
            #aşağıdaki döngü ile dosyamız alt alta ve göze hitab edecek şekilde görüntülenmesi sağlanıyor.
           for i in calisanlistesi:
            print(i)
        #gerekli işlemleri yerine getirdikten sonra otomatik olarak.Menüye dönüş sağlıyoruz.    
        self.menusecim()
    

    
    #menusecim fonksiyonumzda seçimimiz '2'den yanaysa buraya yönlendiriliriz.
    def calisancikar(self):
        #calisan cikar ile gerekli dosyamızdan veri görüntülememiz gerekecektir.
        #calisanekle metodu ile kaydettiğimiz dosyayı satır satır okutuyoruz.
        with open(r"C:\Users\fayik\Desktop\simple_company_management\calisanlar.txt","r") as dosya:
            calisanlar=dosya.readlines()

        #dosyamızın okunabilirliğini arttırmak için gerekli veriler analiz edilipi
        #daha optimize hale getiriliyor.
        #bunun için öncellikle boş bir gcalisanlar adlı dize oluşturuyoruz.
        #join işlemi ile dosyamıza bağlantı sağlayıp,hesaplamalarımızı uygulanabilir hale getiriyoruz.
        #calisanlar dosyamızdaki verileri,diziye kaydedip terminalde yazdırma işlemi yapmasını bekliyoruz.
        gcalisanlar=[]
        for calisan in calisanlar:
           gcalisanlar.append(" ".join(calisan[:-1].split("--"))) 
        #döngü ile calisanlar .txt uzantılı dosyamızdaki verileri,
        #gcalisanlar döngümüzüde döndürüyoruz ve alta alta yukarıda gerekli hesaplamalarımızın uygunluğu için alt alta sıralıyoruz. 
        for calisan in gcalisanlar:
            print(calisan)   
        #len fonksiyonu ile gcalisanlar dizimizin uzunluğunu yazdırıyoruz. 
        secim=int(input("LÜTFEN ÇIKARMAK İSTEDİĞİNİZ ÇALIŞANIN KAYITLI OLDUĞU NUMARAYI BELRTİNİZ.(1-{}=".format(len(gcalisanlar))))
        #aşağıda döngümüz ile seçim aralığımızı belli ediyoruz.
        #secim ile gcalisanlar dizimizin aralığını buluyoruz.
        #int secim değerimiz ile çıkarmak istediğimiz çalışanı çıkarıyoruz.
        while secim<1   or secim>len(gcalisanlar):
            secim=int(input("LÜTFEN YANDAKİNE UYGUN DEGER GİRİNİZ.(1-{}=".format(len(gcalisanlar))))
         #pop fonksiyonumuz ile secimden 1 çıkarıp istenen personel dosyamızdan siliniyor. 
        calisanlar.pop(secim-1)
        #sayaç oluşturuyoruz ve silinen elemanın dosyadaki id'leri karışmasını engellemek için.
        #dosyada döndüreceğiz.
        sayac=1
        #şimdide oluşturduğumuz dcalisanlar ile kodumuzdaki id'leri sıralamasını yapacağız.
        dcalisanlar=[]
        #döngü açıp döngümüz ile çıkarma işleminden sonra verilerimizi dosyaya düzenli ve sıralı bir şekilde sıralayabiliyoruz
        for calisan in calisanlar:

            dcalisanlar.append(str(sayac)  + ":" +  calisan.split(":")[1])
            sayac+=1
        #fonksiyonumuzu uyguladıktan sonra dosyamıza yazdırma işlemi burada yapılıyor.    
        with open(r"C:\Users\fayik\Desktop\simple_company_management\calisanlar.txt","w") as dosya:
            dosya.writelines(dcalisanlar)
        #fonksiyonumuz ile işimiz bittikten sonra seçim ekranına yönlendiriliyoruz.
        self.menusecim()

    #personellerin maaşlarının gösterimini burada yapıyoruz.
    #fonksiyon içerisinde string 'a' değeri tutuyoruz.