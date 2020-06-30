#!/usr/bin/python3

import os
import time
import pyshorteners
from time import sleep


def clear():
    os.system('clear' if os.name == "nt" "cls" else "clear")

def Main():
    print("\033[93m--------------------------------------------")
    print("   Hide custom URL for social engineering   ")
    print("   Created by @perez_mascato as URLCADIZ   ")
    print("\n Edited by Sercan Yılmaz for Turkish Users   ")
    print("        bilgi@sercanyilmaz.com.tr   ")
    print("--------------------------------------------")
    print("\n[*1]  Google")
    print("[*2]  Youtube")
    print("[*3]  Spotify")
    print("[*4]  Instagram")
    print("[*5]  Facebook")
    print("[*6]  Sabah")
    print("[*7]  Hürriyet")
    print("[*8]  Yeni Şafak")
    print("[*9]  Medium")
    print("[*10] Haberler.Com")
    print("[*11] CHP")
    print("[*12] MHP")
    print("[*13] AKP")
    print("[*14] BTC Türk")
    print("[*15] Udemy")
    print("[*16] Hepsiburada")
    print("[*17] n11")
    print("[*18] Trendyol")
    print("[*19] Personalized")
    print("\n[*99]  Exit")
    Selector()


def Selector():
    select = int(input("\nSeçim: "))
    if select == 1:
        EnlaceGoogle()
    elif select == 2:
        EnlaceYoutube()
    elif select == 3:
        EnlaceSpotify()
    elif select == 4:
        EnlaceInstagram()
    elif select == 5:
        EnlaceFacebook()
    elif select == 6:
        EnlaceSabah()
    elif select == 7:
        EnlaceHurriyet()
    elif select == 8:
        EnlaceYeniSafak()
    elif select == 9:
        EnlaceMedium()
    elif select == 10:
        EnlaceHaberlerCom()
    elif select == 11:
        EnlaceCHP()
    elif select == 12:
        EnlaceMHP()
    elif select == 13:
        EnlaceAKP()
    elif select == 14:
        EnlaceBtcTurk()
    elif select == 15:
        EnlaceUdemy()
    elif select == 16:
        EnlaceHepsiburada()
    elif select == 17:
        EnlaceNeOnbir()
    elif select == 18:
        EnlaceTrendyol()
    elif select == 19:
        EnlacePersonalized()
    elif select == 99:
        clear()
        print("Çıkış yapılıyor...")
        sleep(1)
        clear()
        exit()
    else:
        clear()
        print("Hatalı giriş...")
        sleep(1)
        clear()
        Main()


def EnlaceGoogle():
    clear()
    print("Seçiminiz Google.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: onemli-bir-gelisme")
    Postlink = str(input("\nLink uzantısı: "))
    clear()
    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    print(f"\033[95m\nSahte link hazır: https://www.google.com-{Postlink}@{Withouthttp}")
    Other()

def EnlaceYoutube():
    clear()
    print("Seçiminiz Youtube.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: inanilmaz-video-herkesi-sasirtti")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.youtube.com-watch-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceSpotify():
    clear()
    print("Seçiminiz Spotify.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: yeni-album-play-list")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.spotify.com-album-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceInstagram():
    clear()
    print("Seçiminiz Instagram.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: photos-new")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.instagram.com-photo-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceFacebook():
    clear()
    print("Seçiminiz Facebook.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: new-post-in-facebook")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.facebook.com-profile-{Postlink}@{Withouthttp}")
    Other()

def EnlaceSabah():
    clear()
    print("Seçiminiz Sabah Gazetesi.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: beklenen-haber-sevindirdi-gozlerinize-inanamayacaksiniz")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.sabah.com.tr-sondakika-{Postlink}@{Withouthttp}")
    Other()

def EnlaceHurriyet():
    clear()
    print("Seçiminiz Hürriyet Gazetesi.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: beklenen-haber-sevindirdi-gozlerinize-inanamayacaksiniz")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.hurriyet.com.tr-gundem-{Postlink}@{Withouthttp}")
    Other()

def EnlaceYeniSafak():
    clear()
    print("Seçiminiz Yeni Şafak Gazetesi.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: beklenen-haber-sevindirdi-gozlerinize-inanamayacaksiniz")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.yenisafak.com.tr-sondakika-{Postlink}@{Withouthttp}")
    Other()


def EnlaceMedium():
    clear()
    print("Seçiminiz Medium.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: beklenen-haber-sevindirdi-gozlerinize-inanamayacaksiniz")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.medium.com-turkiye-{Postlink}@{Withouthttp}")
    Other()


def EnlaceHaberlerCom():
    clear()
    print("Seçiminiz Haberler.Com.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: beklenen-haber-sevindirdi-gozlerinize-inanamayacaksiniz")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.haberler.com-son-dakika-{Postlink}@{Withouthttp}")
    Other()


def EnlaceCHP():
    clear()
    print("Seçiminiz CHP (Cumhuriyet Halk Partisi).")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: onemli-gelisme")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.chp.org.tr-haberler-{Postlink}@{Withouthttp}")
    Other()

def EnlaceMHP():
    clear()
    print("Seçiminiz MHP (Milliyetçi Hareket Partisi).")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: onemli-gelisme")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.mhp.org.tr-htmldocs-mhp-4687-{Postlink}@{Withouthttp}")
    Other()

def EnlaceAKP():
    clear()
    print("Seçiminiz AKP (Adalet Ve Kalkınma Partisi).")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: onemli-gelisme")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.akparti.org.tr-haberler-{Postlink}@{Withouthttp}")
    Other()

def EnlaceBtcTurk():
    clear()
    print("Seçiminiz BTC Türk.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: onemli-gelisme")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.btcturk.com-{Postlink}@{Withouthttp}")
    Other()


def EnlaceUdemy():
    clear()
    print("Seçiminiz Udemy.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: onemli-gelisme")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.udemy.com-course-{Postlink}@{Withouthttp}")
    Other()


def EnlaceHepsiburada():
    clear()
    print("Seçiminiz Hepsiburada.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: yuzde-doksan-indirim")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.hepsiburada.com-urun-detay-{Postlink}@{Withouthttp}")
    Other()


def EnlaceNeOnbir():
    clear()
    print("Seçiminiz n11.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: yuzde-doksan-indirim")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://urun.n11.com-firsatlar-{Postlink}@{Withouthttp}")
    Other()


def EnlaceTrendyol():
    clear()
    print("Seçiminiz Trendyol.")
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: yuzde-doksan-indirim")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://trendyol.com-firsatlar-{Postlink}@{Withouthttp}")
    Other()


def EnlacePersonalized():
    clear()
    print("Seçiminiz Personalized.")
    Domain = str(input("ozelalanadim.com/es... input domain: "))
    OriginalLink = str(input("\nOrijinal URL(yönlendirmek istediğiniz asıl adres): "))
    
    print("\nİnandırıcı bir uzantı yazmalısın, mesela: inandirici-bir-link-gibi-gorunmeli")
    Postlink = str(input("\nLink uzantısı: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    clear()
    print(f"\033[95m\nSahte link hazır: https://www.{Domain}-{Postlink}@{Withouthttp}")
    
    Other()

def Other():
    print("\033[93m\nYeni bir link oluşturmak ister misin?")
    print("Evet [*1] \nHayır [*2]")
    select=int(input("\nSeçim: "))
    if select == 1:
        clear()
        Main()
    else:
        clear()
        exit()

Main()
