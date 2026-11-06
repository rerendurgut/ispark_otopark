# 🚗 İBB İSPARK Canlı Otopark Doluluk & Harita Uygulaması

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Folium](https://img.shields.io/badge/Folium-Geospatial_Map-77B800?style=flat-square&logo=python&logoColor=white)](https://python-visualization.github.io/folium/)
[![İBB Open Data](https://img.shields.io/badge/İBB_Açık_Veri-API-blue?style=flat-square&logo=openstreetmap&logoColor=white)](https://data.ibb.gov.tr/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

İstanbul Büyükşehir Belediyesi (İBB) Açık Veri Portalı API'si üzerinden tüm İSPARK otoparklarının anlık doluluk verilerini çekerek interaktif harita üzerinde görselleştiren, anlık kapasite istatistikleri ve tek tıkla navigasyon imkanı sunan açık kaynaklı web uygulaması.

---

## 🌟 Temel Özellikler

- **📡 Anlık Canlı Veri:** İBB açık veri sunucularına doğrudan bağlanarak güncel boş/dolu kapasite verilerini çeker (60 saniye akıllı önbellekleme ile API yükünü optimize eder).
- **🗺️ Akıllı Harita Kümeleme (Marker Clustering):** İstanbul genelindeki yüzlerce otoparkı Leaflet/Folium tabanlı kümeleme ile kasmadan, akıcı bir harita deneyimiyle sunar.
- **🎨 Renk Kodlu Doluluk Durumu:**
  - 🟢 **Yeşil:** Rahat (%50 altı doluluk)
  - 🟠 **Turuncu:** Yoğun (%50 - %90 arası doluluk)
  - 🔴 **Kırmızı:** Dolu (%90 üzeri doluluk)
- **📍 Konum & Arama Desteği:** Kullanıcının mevcut konumunu harita üzerinde bulma (`LocateControl`) ve ilçe/mekan bazlı arama (`Geocoder`).
- **🚗 Tek Tıkla Navigasyon:** Seçilen otoparka doğrudan Google Maps üzerinden rota oluşturma bağlantısı.
- **📊 Şehir İçi Canlı Özet:** Toplam aktif otopark sayısı ve anlık toplam boş yer kapasitesi sayaçları.

---

## 🛠️ Mimari & Kullanılan Teknolojiler

- **Python 3**: Veri işleme, JSON ayrıştırma ve hesaplama.
- **Streamlit**: Hafif, modern ve reaktif web paneli.
- **Folium & streamlit-folium**: Leaflet.js tabanlı etkileşimli harita motoru, kümeleme eklentileri.
- **Requests**: İBB REST API uç noktası iletişimi.

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.9 veya daha yeni sürüm
- `pip` paket yöneticisi

```bash
# 1. Depoyu klonlayın
git clone https://github.com/rerendurgut/ispark_otopark.git
cd ispark_otopark

# 2. Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# 3. Streamlit uygulamasını başlatın
streamlit run otopark_test.py
```

Uygulama otomatik olarak tarayıcınızda `http://localhost:8501` adresinde açılacaktır.

---

## 📄 Lisans

Bu proje [MIT](LICENSE) lisansı altında sunulmaktadır. Geliştirici: [Recep Eren Durgut](https://github.com/rerendurgut).
