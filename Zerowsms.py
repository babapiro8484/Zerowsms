from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

            
while 1:
    system("cls||clear")
    print("""{}

███████╗███████╗███████╗██████╗  ██████╗ ██╗    ██╗
╚══███╔╝██╔════╝██╔════╝██╔══██╗██╔═══██╗██║    ██║
  ███╔╝ █████╗  █████╗  ██████╔╝██║   ██║██║ █╗ ██║
 ███╔╝  ██╔══╝  ██╔══╝  ██╔══██╗██║   ██║██║███╗██║
███████╗███████╗███████╗██║  ██║╚██████╔╝╚███╔███╔╝
╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ 
    
    Sms: {}           {}by {}@zerowbabaa\n  
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX))
    try:
        menu = (input(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX+ " 1- SMS Gönder (RELAX)\n\n 2- SMS Gönder (DEHŞET)\n\n 3-SİKTİR GİT \n\n" + Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX + "Hatalı giriş yaptin nabion aq tekrar dene")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX+ "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna bas kral): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX+ "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yaz kral: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX+ "Hatalı dosya dizini nabion aq tekrar dene")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna bas kral)"
            except ValueError:
                system("cls||clear")
                print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX + "Hatalı telefon numarası nabion aq tekrar dene")
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(
    Fore.YELLOW + Fore.LIGHTYELLOW_EX +
    Fore.GREEN + Fore.LIGHTGREEN_EX +
    Fore.CYAN + Fore.LIGHTCYAN_EX +
    Fore.BLUE + Fore.LIGHTBLUE_EX +
    Fore.MAGENTA + Fore.LIGHTMAGENTA_EX +
    "Mail adresi (Bilmiyorsan 'enter' tuşuna bas kral dert değil): ",
    end=""
            )
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(
    Fore.YELLOW + Fore.LIGHTYELLOW_EX +
    Fore.GREEN + Fore.LIGHTGREEN_EX +
    Fore.CYAN + Fore.LIGHTCYAN_EX +
    Fore.BLUE + Fore.LIGHTBLUE_EX +
    Fore.MAGENTA + Fore.LIGHTMAGENTA_EX +
    "Hatalı mail adresi nabion aq tekrar dene",
    end=""
)
sleep(3)
continue
system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyon kral {sonsuz}: "+ Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX + "Hatalı giriş yaptın nabion aq tekrar dene") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX+ "Kaç saniye aralıkla göndermek istiyorsun kral: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX + "Hatalı giriş yaptın nabion aq tekrar dene")
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX + "\nMenüye dönmek için 'enter' tuşuna bas kral...")
        input()
    elif menu == 3:
        system("cls||clear")
        print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX + "SİKTİR OLUP GİDİLİYOR...")
        break
    elif menu == 2:
        system("cls||clear")
        print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX + "Telefon numarasını başında '+90' olmadan yaz kral: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX+ "Hatalı telefon numarası nabion aq tekrar dene") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX+ "Mail adresi (Bilmiyorsan 'enter' tuşuna bas kral): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.RED, Fore.LIGHTRED_EX,
        Fore.YELLOW, Fore.LIGHTYELLOW_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.CYAN, Fore.LIGHTCYAN_EX,
        Fore.BLUE, Fore.LIGHTBLUE_EX,
        Fore.MAGENTA, Fore.LIGHTMAGENTA_EX+ "Hatalı mail adresi nabion aq tekrar dene") 
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()
        def Turbo():
            while not dur.is_set():
                thread = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread.append(t)
                    t.start()
                for t in thread:
                    t.join()
        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)
