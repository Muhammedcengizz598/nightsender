# 🌙 NightSender - SMS Tool

<div align="center">

![Version](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![License](https://img.shields.io/badge/license-Educational-orange.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux-lightgrey.svg)

**Gelişmiş SMS Gönderim Aracı**

</div>

---

## ⚠️ YASAL UYARI

Bu araç **yalnızca eğitim ve test amaçlıdır**. Kötüye kullanımdan kaynaklanan her türlü yasal sorumluluk kullanıcıya aittir. Geliştirici, bu aracın yasadışı veya etik olmayan kullanımından **hiçbir şekilde sorumlu değildir**.

### 🚫 Yasaklanan Kullanımlar:
- ❌ İzinsiz SMS bombardımanı
- ❌ Taciz veya rahatsızlık verme
- ❌ Hizmet kesintisi oluşturma (DoS)
- ❌ Kişisel verilerin kötüye kullanımı
- ❌ Ticari amaçlı izinsiz kullanım

### ✅ İzin Verilen Kullanımlar:
- ✔️ Kendi sistemlerinizi test etme
- ✔️ Güvenlik araştırmaları (izinli)
- ✔️ Eğitim ve öğrenme amaçlı kullanım
- ✔️ API entegrasyon testleri

**KULLANIM SORUMLULUĞU:** Bu aracı kullanarak, tüm yasal sorumluluğu kabul etmiş sayılırsınız.

---

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Sistem Gereksinimleri](#-sistem-gereksinimleri)
- [Kurulum](#-kurulum)
  - [Linux Kurulumu](#linux-kurulumu)
  - [Termux Kurulumu](#termux-kurulumu)
- [Kullanım](#-kullanım)
- [Özellik Detayları](#-özellik-detayları)
- [Desteklenen Servisler](#-desteklenen-servisler)
- [Sorun Giderme](#-sorun-giderme)
- [SSS](#-sss)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

---

## 🚀 Özellikler

### 🎯 Temel Özellikler
- **50+ Servis Desteği**: Türkiye'deki popüler platformlardan SMS gönderimi
- **Çoklu Mod Desteği**: Normal ve Turbo mod seçenekleri
- **Toplu SMS**: Telefon listesi ile çoklu numara desteği
- **Zamanlı Gönderim**: Yıl, ay, gün, saat, dakika bazlı süre ayarı
- **Renkli Arayüz**: Colorama ile geliştirilmiş kullanıcı dostu terminal arayüzü
- **Gerçek Zamanlı İstatistik**: Anlık başarı/başarısızlık takibi

### 🎨 Gelişmiş Özellikler
- **ASCII Banner**: Profesyonel görünüm
- **Hata Yönetimi**: Detaylı hata mesajları ve loglama
- **Threading Desteği**: Turbo modda çoklu thread kullanımı
- **Otomatik TC Kimlik Üretimi**: Gerekli servislerde otomatik TC no oluşturma
- **Mail Desteği**: Opsiyonel e-posta adresi girişi
- **Geri Sayım**: Turbo modda kalan süre gösterimi

---

## 💻 Sistem Gereksinimleri

### Minimum Gereksinimler
- **Python**: 3.7 veya üzeri
- **RAM**: 512 MB
- **Depolama**: 50 MB boş alan
- **İnternet**: Aktif internet bağlantısı

### Desteklenen Platformlar
- ✅ Linux (Ubuntu, Debian, Kali, Arch, vb.)
- ✅ Termux (Android)
- ✅ Windows (WSL ile)
- ✅ macOS

### Gerekli Python Kütüphaneleri
```
colorama==0.4.6
requests==2.31.0
```

---

## 📦 Kurulum

### Linux Kurulumu

#### 1. Depoyu Klonlayın
```bash
git clone https://github.com/Muhammedcengizz598/nightsender.git
cd nightsender
```

#### 2. Python ve Pip Kurulumu
```bash
# Debian/Ubuntu
sudo apt update
sudo apt install python3 python3-pip -y

# Arch Linux
sudo pacman -S python python-pip

# Fedora
sudo dnf install python3 python3-pip
```

#### 3. Bağımlılıkları Yükleyin
```bash
pip3 install -r requirements.txt
```

#### 4. Çalıştırma İzni Verin
```bash
chmod +x Nightsender.py
```

#### 5. Programı Başlatın
```bash
python3 Nightsender.py
```

---

### Termux Kurulumu

#### 1. Termux'u Güncelleyin
```bash
pkg update && pkg upgrade -y
```

#### 2. Gerekli Paketleri Yükleyin
```bash
pkg install python git -y
```

#### 3. Depoyu Klonlayın
```bash
git clone https://github.com/Muhammedcengizz598/nightsender.git
cd nightsender
```

#### 4. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

#### 5. Programı Başlatın
```bash
python Nightsender.py
```

---

## 🎮 Kullanım

### Başlangıç
Programı başlattığınızda ana menü ile karşılaşacaksınız:

```
╔══════════════════════════════════════════════════════════╗
║  Ana Menü                                                ║
╠══════════════════════════════════════════════════════════╣
║  [1] SMS Gönder (Normal Mod)                            ║
║  [2] SMS Gönder (Turbo Mod - Zamanlı)                   ║
║  [3] Çıkış                                               ║
╚══════════════════════════════════════════════════════════╝
```

### Mod 1: Normal SMS Gönderimi

#### Tek Numara İçin
```bash
[?] Telefon numarası (başında +90 olmadan): 5551234567
[?] Mail adresi (opsiyonel): ornek@mail.com
[?] Kaç SMS gönderilsin (Sonsuz için boş bırakın): 10
[?] Gönderim aralığı (saniye): 5
```

#### Toplu Gönderim İçin
```bash
[?] Telefon numarası (başında +90 olmadan): [ENTER]
[?] Telefon listesi dosya yolu: /path/to/numbers.txt
[?] Mail adresi (opsiyonel): 
[?] Kaç SMS gönderilsin: 5
[?] Gönderim aralığı (saniye): 3
```

**numbers.txt formatı:**
```
5551234567
5559876543
5551112233
```

### Mod 2: Turbo Mod (Zamanlı)

```bash
[?] Telefon numarası (başında +90 olmadan): 5551234567
[?] Mail adresi (opsiyonel): 

╔══════════════════════════════════════════════════════════╗
║  Turbo Mod - Süre Ayarları                               ║
╚══════════════════════════════════════════════════════════╝

[?] Yıl (0 için boş bırakın): 0
[?] Ay (0 için boş bırakın): 0
[?] Gün (0 için boş bırakın): 0
[?] Saat (0 için boş bırakın): 1
[?] Dakika (0 için boş bırakın): 30
```

**Turbo Mod Özellikleri:**
- ⚡ Maksimum hız ile gönderim
- 🔄 Çoklu thread kullanımı
- ⏱️ Gerçek zamanlı geri sayım
- 🛑 CTRL+C ile durdurma

---

## ���� Özellik Detayları

### Normal Mod
- **Amaç**: Kontrollü ve düzenli SMS gönderimi
- **Hız**: Kullanıcı tanımlı aralıklarla
- **Kullanım**: Test ve düşük hacimli işlemler
- **Avantaj**: Daha az kaynak tüketimi

### Turbo Mod
- **Amaç**: Maksimum hızda SMS gönderimi
- **Hız**: Threading ile eşzamanlı gönderim
- **Kullanım**: Yüksek hacimli test senaryoları
- **Avantaj**: Zaman bazlı otomatik durdurma

### Telefon Listesi Desteği
- Her satırda bir numara
- 10 haneli format (5XXXXXXXXX)
- Başında +90 veya 0 olmadan
- UTF-8 kodlamalı metin dosyası

### Mail Adresi Kullanımı
- Bazı servisler mail adresi gerektirir
- Opsiyonel alan (boş bırakılabilir)
- Boş bırakılırsa otomatik rastgele mail üretilir
- Format: kullanici@domain.com

---

## 📡 Desteklenen Servisler

Araç, **50+ farklı servisi** desteklemektedir:

### E-Ticaret & Perakende
- Bim, Koton, Evidea, English Home
- WMF, Akasya, Akbatı
- File Market, Uysal Market

### Yemek & Restoran
- Dominos, Little Caesars, Köfteci Yusuf
- Baydöner, Pidem, Komagene
- Kahve Dünyası, Coffy

### Ulaşım & Belediye
- İDO, Metro, Bodrum Belediye
- Fatih Belediye, Sancaktepe Belediye
- Bayrampaşa Belediye, Hamidiye

### Diğer Hizmetler
- Suiste, KimGB, Tikla Gelsin
- Naosstars, Yapp, Beefull
- Frink, Orwi, Porty
- Taşdelen, Yılmaz Ticaret
- Money, Alixavien, Jimmykey

**Not:** Servis listesi sürekli güncellenmektedir.

---

## 🔍 Sorun Giderme

### Yaygın Hatalar ve Çözümleri

#### 1. ModuleNotFoundError: No module named 'colorama'
```bash
# Çözüm
pip3 install colorama requests
```

#### 2. Permission Denied
```bash
# Çözüm
chmod +x Nightsender.py
```

#### 3. Connection Timeout
```bash
# Çözüm: İnternet bağlantınızı kontrol edin
# Firewall ayarlarını kontrol edin
# VPN kullanıyorsanız kapatmayı deneyin
```

#### 4. Geçersiz Telefon Numarası
```bash
# Doğru format: 5551234567 (10 hane)
# Yanlış: +905551234567, 05551234567
```

#### 5. Termux'ta Python Bulunamadı
```bash
# Çözüm
pkg install python -y
```

---

## ❓ SSS

### S: Bu araç yasal mı?
**C:** Araç kendisi yasaldır, ancak kullanım amacınız yasalara uygun olmalıdır. İzinsiz SMS gönderimi yasalara aykırıdır.

### S: Hangi ülkelerde çalışır?
**C:** Şu anda sadece Türkiye'deki servisleri desteklemektedir.

### S: Kaç SMS gönderebilirim?
**C:** Teknik limit yoktur, ancak etik ve yasal sınırlar içinde kullanılmalıdır.

### S: Servisler neden bazen çalışmıyor?
**C:** Servisler API'lerini değiştirebilir veya güvenlik önlemleri alabilir. Güncellemeler için repo'yu takip edin.

### S: Kendi servisimi ekleyebilir miyim?
**C:** Evet, `sms.py` dosyasına yeni fonksiyon ekleyerek genişletebilirsiniz.

### S: Windows'ta çalışır mı?
**C:** Evet, ancak WSL (Windows Subsystem for Linux) kullanmanız önerilir.

### S: Turbo mod ne kadar hızlı?
**C:** Threading sayesinde saniyede 10-50 istek gönderebilir (servise bağlı).

### S: Loglar tutuluyor mu?
**C:** Hayır, şu anda log tutma özelliği bulunmamaktadır.

---

## 🤝 Katkıda Bulunma

Projeye katkıda bulunmak isterseniz:

1. **Fork** edin
2. Yeni bir **branch** oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi **commit** edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi **push** edin (`git push origin feature/yeniOzellik`)
5. **Pull Request** açın

### Katkı Alanları
- 🆕 Yeni servis ekleme
- 🐛 Bug düzeltmeleri
- 📝 Dokümantasyon iyileştirmeleri
- 🌍 Çeviri desteği
- ⚡ Performans optimizasyonları

---

## 📄 Lisans

Bu proje **eğitim amaçlı** geliştirilmiştir. Ticari kullanım yasaktır.

### Kullanım Koşulları
- ✅ Eğitim ve öğrenme amaçlı kullanım
- ✅ Kişisel test ve geliştirme
- ✅ Açık kaynak katkıları
- ❌ Ticari kullanım
- ❌ Kötü amaçlı kullanım
- ❌ İzinsiz dağıtım

---

## 👨‍💻 Geliştirici

**Muhammed Cengiz**

---

## 🙏 Teşekkürler

Bu projeyi kullandığınız için teşekkür ederiz. Lütfen sorumlu ve etik bir şekilde kullanın.

### Önemli Hatırlatma
> **"Büyük güç, büyük sorumluluk getirir."** - Bu aracı kullanırken başkalarının haklarına saygı gösterin ve yasalara uyun.

---

## 📊 İstatistikler

- **Toplam Servis**: 50+
- **Desteklenen Platform**: 4
- **Versiyon**: 2.0 Advanced Edition
- **Son Güncelleme**: 2024

---

## 🔄 Güncellemeler

### v2.0 - Advanced Edition
- ✨ Turbo mod eklendi
- ⏱️ Zamanlı gönderim özelliği
- 🎨 Geliştirilmiş arayüz
- 📊 Gerçek zamanlı istatistikler
- 🔧 50+ servis desteği

### v1.0 - Initial Release
- 🚀 İlk sürüm
- 📱 Temel SMS gönderimi
- 📋 Toplu gönderim desteği

---

<div align="center">

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

Made with ❤️ by Muhammed Cengiz

</div>
