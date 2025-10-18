🛡️ Log Priority Dashboard (LPD)
SOC Analist Verimlilik Aracı / SOC Analyst Efficiency Tool

Language: Türkçe | English


<a id="english"></a>English
📝 Project Overview (TÜBİTAK 2209-A Project)
This log analysis and prioritization tool is being developed under the scope of the TÜBİTAK 2209-A University Students Research Projects Support Program.

Objective: The main goal is to minimize False Positives that consume significant time for L1 SOC (Security Operations Center) analysts. This Python-based dashboard automatically classifies security logs by severity (CRITICAL, MEDIUM, IGNORE), directing the analyst's attention solely to genuine threats.

🚀 Features and Usability
Priority-Based Filtering: Instantly filter logs by security severity to focus on critical threats.

Splunk-Like Dashboard: A user-friendly, visualized interface that supports rapid decision-making.

Efficiency: Potential to reduce the time spent on manual review of non-critical logs by up to 70%.

💾 Data Set Usage Statement
The log datasets used in this project are provided from the LogHub repository for academic research purposes.

Usage Note: For any usage or distribution of the datasets, please refer to the original LogHub repository URL: https://github.com/logpai/loghub and cite the LogHub paper where applicable.

🎯 FUTURE ENHANCEMENTS (Development Plans)
ADD MACHINE LEARNING 🤖

Current: "E18 = CRITICAL" (fixed rule)

With ML: "This IP has a 94% probability of performing E18" (smart prediction)

REAL-TIME LOG MONITORING ⚡

Current: Read from CSV (static)

Advanced: Monitor the live log file - See live attacks instantly

REPORTING SYSTEM 📊

Automatically generate daily/weekly reports

"Top 10 Attacking IPs"

"Attack Trend Analysis"

AUTOMATED BLOCKING 🛡️

Current: Just display

Advanced: Ban the IP via firewall with a button - "Block this IP" button

MULTIPLE LOG FILE SUPPORT 📁

Not just 1 CSV

Logs from multiple servers

Different formats (Apache, Windows, etc.)

USER MANAGEMENT 👥

SOC analyst login

Different privileges (L1, L2, Admin)

Action history

GEOGRAPHICAL VISUALIZATION 🗺️

Displaying IPs on a map

"50 attacks from China, 20 attacks from the USA"

<a id="türkçe"></a>Türkçe
📝 Proje Özeti (TÜBİTAK 2209-A Projesi)
Bu proje, TÜBİTAK 2209-A Üniversite Öğrencileri Araştırma Projeleri Desteği Programı kapsamında geliştirilmekte olan bir log analiz ve önceliklendirme aracıdır.

Amaç: SOC (Güvenlik Operasyon Merkezi) L1 analistlerinin en büyük zaman kaybı olan Yanlış Pozitifleri (False Positive) en aza indirmektir. Python tabanlı bu kontrol paneli, güvenlik loglarını önem derecesine göre (CRITICAL, MEDIUM, IGNORE) otomatik olarak sınıflandırır ve analistlerin dikkatini yalnızca gerçek tehditlere yönlendirir.

🚀 Özellikler ve Kullanım Kolaylığı
Öncelik Bazlı Filtreleme: Logları güvenlik önemine göre anında filtreleyerek kritik tehditlere odaklanma.

Splunk Benzeri Dashboard: Kullanımı kolay, görselleştirilmiş ve hızlı karar almayı destekleyen arayüz.

Verimlilik: Önemsiz logların manuel incelenmesine harcanan süreyi %70'e kadar azaltma potansiyeli.

💾 Veri Seti Kullanımına Dair Not
Bu projede kullanılan log veri setleri, akademik araştırma amaçlı olarak LogHub deposundan sağlanmıştır.

Kullanım Notu: Veri setinin herhangi bir dağıtımı veya kullanımı için lütfen LogHub deposunun orijinal URL'sine atıf yapınız: https://github.com/logpai/loghub ve ilgili LogHub makalesini (varsa) referans gösteriniz.

🎯 GELİŞTİRME PLANLARI (Gelecek Vizyonu)
MAKİNE ÖĞRENMESİ EKLE 🤖

Normal: "E18 = CRITICAL" (sabit kural)

ML ile: "Bu IP'nin E18 yapma olasılığı %94" (akıllı tahmin)

GERÇEK ZAMANLI LOG İZLEME ⚡

Şimdi: CSV'den oku (statik)

Gelişmiş: Canlı log dosyasını izle - Canlı saldırıları anında gör

RAPORLAMA SİSTEMİ 📊

Günlük/haftalık rapor otomatik üret

"En çok saldıran 10 IP"

"Saldırı trend analizi"

OTOMATİK ENGELLEME 🛡️

Şimdi: Sadece göster

Gelişmiş: Butonla IP'yi firewall'dan banla - "Bu IP'yi engelle" butonu

ÇOKLU LOG DOSYASI DESTEĞİ 📁

Sadece 1 CSV değil

Birden fazla sunucu logu

Farklı formatlar (Apache, Windows, vb.)

KULLANICI YÖNETİMİ 👥

SOC analisti girişi

Farklı yetkiler (L1, L2, Yönetici)

İşlem geçmişi

COĞRAFİ GÖRSELLEŞTİRME 🗺️

IP'lerin haritada gösterimi

"Çin'den 50 saldırı, ABD'den 20 saldırı"
