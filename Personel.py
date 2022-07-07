

#CLASS
from classdeneme import araclar
class personel(araclar):
    
    #CONSTRUCTER
    def __init__(self,ad):  # init class cagrildigi gibi calisir
        self.ad=ad
        self.calisma=True
     #overloading   

    def baslat(self):
        self.menusecim()

    def program(self, secim):
        # secim =self.menusecim()
        # print("secim degerimiz budur", secim)
        # print(type(secim))
        if secim==1:
            self.maasgoster()

        elif secim==2:
            self.gorevekle()

        elif secim==3:
            
            self.sikayet() 

        elif secim==4:
            self.otomobil()    

        elif secim==5:
            self.cikis()


    def menusecim(self):

        secim=int(input("{} OTOMASYONUMUZA HOŞGELDİNİZ\n\n1-MAAŞIMI GÖSTER\n2-GÖREV EKLE\n3-ŞİKAYET VE ÖNERİLERİNİZ\n4-OTOPARK\n5-çıkış\n".format(self.ad)))
        # print("\ncalisti\n", secim)
        # if (type(input) == "int")
        while secim < 1 or secim >5:
            secim=input("lütfen 1-4 arasında belirtilen seçeneklerden birini giriniz:")
            return secim

        return self.program(secim)

    
    def maasgoster(self):
        with open(r"C:\Users\fayik\Desktop\simple_company_management\calisanlar.txt","r") as dosya:
            maas=dosya.readlines()
            for i in maas:
                b = i.split(":")
                if b[0] == "4":
                    c = i.split("--")
                    print(c[4])
        self.menusecim()

    def gorevekle(self):


        id=1
        gorev1=input("gorev ekle:")
        

        with open(r"C:\Users\fayik\Desktop\simple_company_management\gorev_ekle.txt","r") as dosya1:
           gorevler=dosya1.readlines()

           for i in gorevler:
            print(i)
        if len(gorevler)==0:
            id=1
        else:
            with open(r"C:\Users\fayik\Desktop\simple_company_management\gorev_ekle.txt","r") as dosya1:
                id=int(dosya1.readlines()[-1].split(":")[0]) +1

        with open(r"C:\Users\fayik\Desktop\simple_company_management\gorev_ekle.txt","a+") as dosya1:
            dosya1.write("{}:{}\n".format(id,gorev1))

        self.menusecim()


        
    def sikayet(self):

        id=1
        sikayet1=input("ŞİKAYET VE ÖNERİLERİNİZİ GİRİNİZ:")
        

        with open(r"C:\Users\fayik\Desktop\simple_company_management\sikayet_dosyası.txt","r") as dosya:
           sikayetler=dosya.readlines()

        if len(sikayetler)==0:
            id=1
        else:
            with open(r"C:\Users\fayik\Desktop\simple_company_management\sikayet_dosyası.txt","r") as dosya:
                id=int(dosya.readlines()[-1].split(":")[0]) +1

        with open(r"C:\Users\fayik\Desktop\simple_company_management\sikayet_dosyası.txt","a+") as dosya:
            dosya.write("{}:{}\n".format(id,sikayet1))

        self.menusecim()
        
    def cikis(self):

        import main
        
        main.giris()