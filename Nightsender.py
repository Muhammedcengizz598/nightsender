from colorama import Fore, Style, init
from time import sleep, time
from os import system
from sms import SendSms
import threading
from datetime import datetime, timedelta

init(autoreset=True)

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

def banner():
    """Geliştirilmiş banner tasarımı"""
    system("cls||clear")
    print(f"""{Fore.CYAN}
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███████╗███████╗   ║
    ║   ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝██╔════╝██╔════╝   ║
    ║   ██╔██╗ ██║██║██║  ███╗███████║   ██║   ███████╗█████╗     ║
    ║   ██║╚██╗██║██║██║   ██║██╔══██║   ██║   ╚════██║██╔══╝     ║
    ║   ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ███████║███████╗   ║
    ║   ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝   ║
    ║                                                               ║
    ║   ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗         ║
    ║   ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗        ║
    ║   ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝        ║
    ║   ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ���█╔══██╗        ║
    ║   ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║        ║
    ║   ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝        ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    
    {Fore.YELLOW}┌─────────────────────────────────────────────────────────────┐
    │  {Fore.GREEN}Toplam Servis: {Fore.WHITE}{len(servisler_sms):<45}{Fore.YELLOW}│
    │  {Fore.GREEN}Yapımcı: {Fore.WHITE}Muhammed Cengiz{Fore.YELLOW}                                 │
    │  {Fore.GREEN}Versiyon: {Fore.WHITE}2.0 - Advanced Edition{Fore.YELLOW}                       │
    └─────────────────────────────────────────────────────────────┘
    {Style.RESET_ALL}""")

def get_time_input():
    """Turbo mod için zaman girişi"""
    print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"{Fore.CYAN}║  {Fore.YELLOW}Turbo Mod - Süre Ayarları{Fore.CYAN}                            ║")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════╝\n")
    
    try:
        print(f"{Fore.GREEN}[?] Yıl (0 için boş bırakın): {Fore.WHITE}", end="")
        years = int(input() or 0)
        print(f"{Fore.GREEN}[?] Ay (0 için boş bırakın): {Fore.WHITE}", end="")
        months = int(input() or 0)
        print(f"{Fore.GREEN}[?] Gün (0 için boş bırakın): {Fore.WHITE}", end="")
        days = int(input() or 0)
        print(f"{Fore.GREEN}[?] Saat (0 için boş bırakın): {Fore.WHITE}", end="")
        hours = int(input() or 0)
        print(f"{Fore.GREEN}[?] Dakika (0 için boş bırakın): {Fore.WHITE}", end="")
        minutes = int(input() or 0)
        
        # Toplam süreyi saniyeye çevir
        total_seconds = (
            years * 365 * 24 * 60 * 60 +
            months * 30 * 24 * 60 * 60 +
            days * 24 * 60 * 60 +
            hours * 60 * 60 +
            minutes * 60
        )
        
        if total_seconds <= 0:
            print(f"\n{Fore.RED}[!] Hata: En az bir zaman değeri girilmelidir!")
            sleep(2)
            return None
            
        return total_seconds
    except ValueError:
        print(f"\n{Fore.RED}[!] Hata: Geçersiz sayı girişi!")
        sleep(2)
        return None

def format_time(seconds):
    """Saniyeyi okunabilir formata çevir"""
    years = seconds // (365 * 24 * 60 * 60)
    seconds %= (365 * 24 * 60 * 60)
    months = seconds // (30 * 24 * 60 * 60)
    seconds %= (30 * 24 * 60 * 60)
    days = seconds // (24 * 60 * 60)
    seconds %= (24 * 60 * 60)
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    
    parts = []
    if years > 0:
        parts.append(f"{years} yıl")
    if months > 0:
        parts.append(f"{months} ay")
    if days > 0:
        parts.append(f"{days} gün")
    if hours > 0:
        parts.append(f"{hours} saat")
    if minutes > 0:
        parts.append(f"{minutes} dakika")
    if seconds > 0:
        parts.append(f"{seconds} saniye")
    
    return ", ".join(parts) if parts else "0 saniye"

def show_menu():
    """Ana menü"""
    print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"{Fore.CYAN}║  {Fore.YELLOW}Ana Menü{Fore.CYAN}                                             ║")
    print(f"{Fore.CYAN}╠══════════════════════════════════════════════════════════╣")
    print(f"{Fore.CYAN}║  {Fore.GREEN}[1]{Fore.WHITE} SMS Gönder (Normal Mod){Fore.CYAN}                         ║")
    print(f"{Fore.CYAN}║  {Fore.GREEN}[2]{Fore.WHITE} SMS Gönder (Turbo Mod - Zamanlı){Fore.CYAN}                ║")
    print(f"{Fore.CYAN}║  {Fore.GREEN}[3]{Fore.WHITE} Çıkış{Fore.CYAN}                                            ║")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════╝\n")
    print(f"{Fore.YELLOW}[>] Seçiminiz: {Fore.WHITE}", end="")

while True:
    banner()
    show_menu()
    
    try:
        menu = input()
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        print(f"\n{Fore.RED}[!] Hatalı giriş! Lütfen 1-3 arası bir sayı girin.")
        sleep(2)
        continue
    
    if menu == 1:
        # Normal Mod
        banner()
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║  {Fore.YELLOW}Normal Mod - SMS Gönderimi{Fore.CYAN}                           ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════╝\n")
        
        print(f"{Fore.GREEN}[?] Telefon numarası (başında +90 olmadan): {Fore.WHITE}", end="")
        tel_no = input()
        tel_liste = []
        
        if tel_no == "":
            print(f"{Fore.GREEN}[?] Telefon listesi dosya yolu: {Fore.WHITE}", end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                print(f"\n{Fore.RED}[!] Dosya bulunamadı!")
                sleep(2)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz için boş bırakın)"
            except ValueError:
                print(f"\n{Fore.RED}[!] Geçersiz telefon numarası!")
                sleep(2)
                continue
        
        print(f"{Fore.GREEN}[?] Mail adresi (opsiyonel): {Fore.WHITE}", end="")
        mail = input()
        if ("@" not in mail or ".com" not in mail) and mail != "":
            print(f"\n{Fore.RED}[!] Geçersiz mail adresi!")
            sleep(2)
            continue
        
        print(f"{Fore.GREEN}[?] Kaç SMS gönderilsin {sonsuz}: {Fore.WHITE}", end="")
        kere = input()
        if kere:
            try:
                kere = int(kere)
            except ValueError:
                print(f"\n{Fore.RED}[!] Geçersiz sayı!")
                sleep(2)
                continue
        else:
            kere = None
        
        print(f"{Fore.GREEN}[?] Gönderim aralığı (saniye): {Fore.WHITE}", end="")
        try:
            aralik = int(input())
        except ValueError:
            print(f"\n{Fore.RED}[!] Geçersiz sayı!")
            sleep(2)
            continue
        
        banner()
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║  {Fore.YELLOW}SMS Gönderimi Başladı...{Fore.CYAN}                             ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════╝\n")
        
        if kere is None:
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in servisler_sms:
                    exec(f"sms.{attribute}()")
                    sleep(aralik)
        
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                while sms.adet < kere:
                    for attribute in servisler_sms:
                        if sms.adet == kere:
                            break
                        exec(f"sms.{attribute}()")
                        sleep(aralik)
        
        print(f"\n{Fore.GREEN}[✓] İşlem tamamlandı!")
        print(f"{Fore.YELLOW}[>] Menüye dönmek için Enter'a basın...")
        input()
    
    elif menu == 2:
        # Turbo Mod
        banner()
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║  {Fore.YELLOW}Turbo Mod - Hızlı SMS Gönderimi{Fore.CYAN}                      ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════╝\n")
        
        print(f"{Fore.GREEN}[?] Telefon numarası (başında +90 olmadan): {Fore.WHITE}", end="")
        tel_no = input()
        
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}[!] Geçersiz telefon numarası!")
            sleep(2)
            continue
        
        print(f"{Fore.GREEN}[?] Mail adresi (opsiyonel): {Fore.WHITE}", end="")
        mail = input()
        if ("@" not in mail or ".com" not in mail) and mail != "":
            print(f"\n{Fore.RED}[!] Geçersiz mail adresi!")
            sleep(2)
            continue
        
        # Zaman girişi
        duration = get_time_input()
        if duration is None:
            continue
        
        banner()
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║  {Fore.YELLOW}Turbo Mod Aktif!{Fore.CYAN}                                     ║")
        print(f"{Fore.CYAN}╠══════════════════════════════════════════════════════════╣")
        print(f"{Fore.CYAN}║  {Fore.GREEN}Hedef: {Fore.WHITE}{tel_no}{Fore.CYAN}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}Süre: {Fore.WHITE}{format_time(duration)}{Fore.CYAN}")
        print(f"{Fore.CYAN}║  {Fore.RED}Durdurmak için CTRL+C{Fore.CYAN}")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════╝\n")
        
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()
        start_time = time()
        end_time = start_time + duration
        
        def Turbo():
            while not dur.is_set() and time() < end_time:
                thread = []
                for fonk in servisler_sms:
                    if dur.is_set() or time() >= end_time:
                        break
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread.append(t)
                    t.start()
                
                for t in thread:
                    t.join()
                
                # Kalan süreyi göster
                remaining = int(end_time - time())
                if remaining > 0:
                    print(f"{Fore.YELLOW}[⏱] Kalan süre: {format_time(remaining)}", end="\r")
        
        try:
            Turbo()
            dur.set()
            print(f"\n\n{Fore.GREEN}[✓] Süre doldu! Toplam {send_sms.adet} SMS gönderildi.")
        except KeyboardInterrupt:
            dur.set()
            print(f"\n\n{Fore.YELLOW}[!] İşlem kullanıcı tarafından durduruldu.")
            print(f"{Fore.GREEN}[✓] Toplam {send_sms.adet} SMS gönderildi.")
        
        print(f"{Fore.YELLOW}[>] Menüye dönmek için Enter'a basın...")
        input()
    
    elif menu == 3:
        banner()
        print(f"\n{Fore.RED}[!] Çıkış yapılıyor...")
        print(f"{Fore.YELLOW}[✓] Nightsender - Muhammed Cengiz tarafından geliştirildi.\n")
        sleep(2)
        break
    
    else:
        print(f"\n{Fore.RED}[!] Geçersiz seçim! Lütfen 1-3 arası bir sayı girin.")
        sleep(2)
