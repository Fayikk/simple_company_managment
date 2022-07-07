
# overloading polimorfizim virtual kullanildi

from os import remove
import random
#from Personel import personel


class araclar():
    def __init__(self, ad):
        self.ad = ad
    
    def otomobil(self):
        araba=["1-OPEL VECTRA","2-FORD FİESTA","3-WOLKSWAGEN PASSAT","4-MERCEDES CLA180","5-FORD FOCUS","6-OPEL COMBO","7-HYUDAİ İ20"]
        
        
        
        for a in araba:
            print(a)

        b=int(input("Secmek istediğiniz aracı belirtiniz:     \n"))

        if b>=1 and b<=7:
           
           print(araba[b-1])
           print("araç garaj verilerinden silindi" + str(araba.pop(b-1)))
           print("aracın yanına gidip yan taraftaki kodu tuşlayın: ",random.randint(100000, 999999))
           
        elif b>=8 or b<=30:
            print("böyle bir araba bulunamadi")
            
            

           
            
            


class taseron():
    def __init__(self, ad):
        self.ad = ad
    
    def taseronfirma(self):
        ekle=input("TASERON FİRMA EKLEYİNİZ:")
        with open(r"C:\Users\fayik\Desktop\simple_company_management\taseron.txt", "a+") as dosya:
            dosya.write(ekle +" "+"SİRKETİ"+"\n")
        with open(r"C:\Users\fayik\Desktop\simple_company_management\taseron.txt","r") as dosya: 
            okut=dosya.readlines()
            for j in okut:
                print(j)                 
                
            #return personel.menusecim

               

                


