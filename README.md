<!-- 🎥 Üstte Hareketli Twitch Logosu -->
<p align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGZod2NrenNxbTVkbzVwMzFmdHNweGl6MzVraGsxanV0OTJtc2FhdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/nvnCtgFUPvXS9MELci/giphy.gif" width="130" alt="Twitch Logo">
</p>

<h1 align="center">✨ Toprak Chat Bot</h1>

<p align="center">
  Modern, temalı ve kullanıcı dostu Twitch izleyici botu.<br>
  Sekme yenileme, renkli arayüz, proxy desteği ve daha fazlası!
</p>

---

## 🚀 Özellikler

- 🎨 Tema seçimi (dinamik renk butonları)
- 🌐 Rastgele veya manuel proxy seçimi
- 👥 İzleyici sayısını belirleme
- 🖥️ Sekme göster/gizle seçeneği
- 🔁 Otomatik sekme yenileme (her 3 dakikada bir)
- ⏱️ Geri sayım sayacı
- 🌀 Hareketli Twitch logosu (web'den çekiliyor)
- 🔗 GitHub yönlendirmesi
- ✍️ “Coded by Toprak” imzası

---

## 🔧 Nasıl Çalışır?

Bu uygulama, **Selenium** kütüphanesini kullanarak arka planda sahte izleyiciler oluşturur. İşleyiş mantığı şu şekildedir:

1. **Kullanıcı girişleri alınır** (kanal adı, izleyici sayısı, proxy türü)
2. Uygulama, arka planda **Chrome tarayıcı sekmeleri** açar
3. Her sekmede seçilen bir **proxy sitesi** üzerinden Twitch kanalına bağlanılır
4. Sekmeler otomatik olarak Twitch yayınına yönlendirilir
5. Eğer aktifse, her **3 dakikada bir sekmeler yenilenir** (AFK koruması)
6. İsteğe bağlı olarak sekmeler **görünmez (headless)** olarak çalışır
7. Tüm bu işlemler kullanıcı arayüzünü dondurmadan arka planda çalışır

> 🎯 Amaç: Twitch’e aktif izleyici gibi gözüken otomasyon sekmeleri göndermek.

---

🧠 Not: Proxy’ler, Twitch’in IP tekrar tespiti ve bot korumalarını aşmak için kullanılır.  
Rastgele proxy kullanımı bu yüzden önerilir.

## ⚙️ Gereksinimler

- **Python 3.8** veya üzeri
- Gerekli kütüphaneler:

pip install customtkinter selenium pillow requests

Chromedriver (Chrome sürümüne uygun):

https://chromedriver.chromium.org/downloads

Dosyayı uygulama klasörüne ekleyin (chromedriver.exe)

📸 Ekran Görüntüsü

<img width="897" height="676" alt="image" src="https://github.com/user-attachments/assets/ea8bad17-1afb-4b18-8b90-faf8636cd27f" />

⚠️ Uyarı
Bu yazılım yalnızca test ve eğitim amaçlıdır.
Twitch'in hizmet koşullarını ihlal edebilecek kullanımlar kullanıcının sorumluluğundadır.

👨‍💻 Geliştirici
Toprak
🔗 github.com/toprak1224
