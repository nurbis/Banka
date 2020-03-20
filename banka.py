#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:41:00 2020

@author: nurbanuozkan
"""

from time import sleep
class Musteri:
    def __init__(self, isim:str, soyisim:str, idno:int, parola:int):
        self.__isim=isim
        self.__soyisim=soyisim
        self.__idno=idno
        self.___parola=parola
        self.__bakiye=0
    
    def getIsim(self):
        return self.__isim
    def getSoyisim(self):
        return self.__soyisim
    def getIdno(self):
        return self.__idno
    def getParola(self):
        return self.___parola
    def getBakiye(self):
        return self.__bakiye
    def setBakiye(self, miktar:float):
        self.__bakiye = miktar
  
        
class Banka:
    def __init__(self, isim:str):
        self.__isim=isim
        self.__musteriler=list()
        
        
    def paraaktar(self, gonderen:Musteri, alici:Musteri, miktar:float):
        #gönderen ve alıcı bankanın musterisi olmalıdır.
        
        if gonderen in self.__musteriler and alici in self.__musteriler:
            if gonderen.getBakiye() < miktar:
                print("Yetersiz Bakiye!")
            else:
                alici.setBakiye(alici.getBakiye()+miktar)
                gonderen.setBakiye(gonderen.getBakiye()-miktar)
                print("Gönderildi!")
    def musteriol(self,isim:str, soyisim:str, idno:int, parola:int):
        self.__musteriler.append(Musteri(isim, soyisim, idno, parola))
    def musterikontrol(self, idno, parola):
        for i in self.__musteriler:
            if i.getIdno()==idno and i.getParola()==parola:
                return i
        return False
            
    def alicivarmi(self, idno):
        for i in self.__musteriler:
            if i.getIdno()==idno:
                return i
        return False
       
    def paracek(self, musteri:Musteri, miktar):
        if musteri in self.__musteriler:
            if musteri.getBakiye() < miktar:
                print("Bakiye Yetersiz!")
            else:
                if miktar % 10 == 0:
                    musteri.setBakiye(musteri.getBakiye() - miktar)
                else:
                    print("10'un katları para cekebilirsiniz")
    def parayatir(self, musteri:Musteri, miktar):
        if musteri in self.__musteriler:
            if miktar % 10 == 0:
                musteri.setBakiye(musteri.getBakiye()+miktar)
            else:
                print("10'un katları para yatırabilirsiniz")
    def bakiyebilgisi(self, musteri:Musteri):
        print("""
              
              musterinin ismi: {}
              musterinin soyismi: {}
              musterinin bakiyesi: {}
              """.format(musteri.getIsim(), musteri.getSoyisim(), musteri.getBakiye()))
              

akbank=Banka("akbank")
akbank.musteriol("banu", "özkan", 12, 4444)
                
def main():
    banka=Banka("ZALIM BANK")
    while True:
        print("""
              [1] MÜŞTERİ OL
              [2] GİRİŞ YAP 
              """)
        secim1=input("seçim yapınız")
        if secim1=="1":
            isim=input("Isim: ")
            soyisim=input("Soyisim: ")
            idno=input("IDno :")
            parola=input("Parola :")
            banka.musteriol(isim, soyisim, idno, parola)
            yenimusteri=banka.musterikontrol(idno, parola)
            print("SN. {} Bankamıza müşteri kaydınız yapılmıştır".format(yenimusteri.getIsim()))
            input("Ana menüye dönmek için 'enter' basınız")
        if secim1=="2":
            idno=input("IDno: ")
            parola=input("Parola: ")
            if banka.musterikontrol(idno, parola):
                musteri=banka.musterikontrol(idno, parola)
                while True:
                    print("""
                          [1]BAKİYE GÖSTER
                          [2]PARA YATIR
                          [3]PARA ÇEK
                          [4]PARA GÖNDER
                          [5]ÇIKIŞ
                          """)
                    secim2=input("seçim yapınız")
                    if secim2=="1":
                        banka.bakiyebilgisi(musteri)
                        input("Ana menüye dönmek için 'enter' basınız")
                    elif secim2=="2":
                        miktar=input("yatırılacak miktar giriniz")
                        miktar=int(miktar)
                        banka.parayatir(musteri, miktar)
                        input("Ana menüye dönmek için 'enter' basınız")
                    elif secim2=="3":
                        miktar=input("çekilecek miktar giriniz")
                        miktar=int(miktar)
                        banka.paracek(musteri, miktar)
                        input("Ana menüye dönmek için 'enter' basınız")
                    elif secim2=="4":
                        aliciID=input("para gönderilecek kişinin id'sini giriniz")
                        if banka.alicivarmi(aliciID):
                            alici=banka.alicivarmi(aliciID)
                            miktar=input("yatırılacak miktar giriniz")
                            miktar=int(miktar)
                            banka.paraaktar(musteri, alici, miktar)
                            input("Ana menüye dönmek için 'enter' basınız")
                        else:
                            print("Alıcı bulunamadı")
                    
                    elif secim2=="5":
                        print("Ana menüye yönlendiriliyor..")
                        sleep(5)
                        break
                        
                    else:
                        print("hatalı giriş")
                        input("Ana menüye dönmek için 'enter' basınız")
                        
            else:
                print("Banka kaydı bulunamadı ya da hatalı müşterili bilgisi")
                
        else:
            print("hatalı giriş")

if __name__== "__main__":
    main()
            
                
                
            

              
            
            
    