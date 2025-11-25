import streamlit as st
import requests
import folium
from folium.plugins import MarkerCluster, Geocoder, LocateControl
from streamlit_folium import st_folium

# --- AYARLAR ---
st.set_page_config(layout="wide", page_title="İBB Canlı Otopark Haritası")
URL = "https://api.ibb.gov.tr/ispark/Park"

# --- BAŞLIK VE AÇIKLAMA ---
st.title("🚗 İBB İspark Canlı Doluluk Haritası")
st.markdown("Bu harita **anlık** olarak İBB sunucularından veri çeker. Mavi butona basarak verileri tazeleyebilirsiniz.")

# --- YENİLE BUTONU ---
if st.button("🔄 Verileri Şimdi Güncelle"):
    st.rerun()

# --- VERİ ÇEKME FONKSİYONU ---
@st.cache_data(ttl=60) # Veriyi 60 saniye hafızada tutar, sonra yeniler
def verileri_getir():
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("İBB Sunucularına ulaşılamadı.")
            return []
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
        return []

data = verileri_getir()

# --- İSTATİSTİKLER (Üstteki Kutucuklar) ---
if data:
    toplam_otopark = len(data)
    # Basit bir hesaplama ile toplam boş kapasiteyi bulalım
    toplam_bos = sum([int(p.get("emptyCapacity", 0)) for p in data if p.get("emptyCapacity")])
    
    col1, col2 = st.columns(2)
    col1.metric("Toplam Otopark", toplam_otopark)
    col2.metric("Şu Anki Toplam Boş Yer", toplam_bos)

# --- HARİTA OLUŞTURMA ---
m = folium.Map(location=[41.0082, 28.9784], zoom_start=11)

# Eklentiler
LocateControl(strings={"title": "Konumumu Göster"}).add_to(m)
Geocoder(placeholder="Yer Ara (Örn: Kanyon)...").add_to(m)
marker_cluster = MarkerCluster().add_to(m)

# Veriyi İşleme
if data:
    for park in data:
        ad = park.get("parkName")
        lat = park.get("lat")
        lng = park.get("lng")
        kapasite = park.get("capacity")
        bos_yer = park.get("emptyCapacity")
        ilce = park.get("district", "İstanbul")
        
        if lat and lng:
            try:
                lat_flt = float(lat)
                lng_flt = float(lng)
                kapasite_int = int(kapasite) if kapasite else 0
                bos_yer_int = int(bos_yer) if bos_yer else 0
                
                doluluk_orani = 0
                if kapasite_int > 0:
                    doluluk_orani = ((kapasite_int - bos_yer_int) / kapasite_int) * 100
                
                color = "green"
                durum_ikonu = "check"
                if doluluk_orani > 90:
                    color = "red"
                    durum_ikonu = "ban"
                elif doluluk_orani > 50:
                    color = "orange"
                    durum_ikonu = "exclamation"
                
                # Yol Tarifi Linki
                google_maps_link = f"https://www.google.com/maps/dir/?api=1&destination={lat_flt},{lng_flt}"
                
                html = f"""
                <div style="width:200px">
                    <b>{ad}</b><br>
                    <small>{ilce}</small><hr>
                    Boş: <b style="color:{color}">{bos_yer_int}</b> / {kapasite_int}<br>
                    <a href="{google_maps_link}" target="_blank">🚗 Yol Tarifi</a>
                </div>
                """
                
                folium.Marker(
                    [lat_flt, lng_flt],
                    popup=folium.Popup(html, max_width=250),
                    tooltip=f"{ad} (Boş: {bos_yer_int})",
                    icon=folium.Icon(color=color, icon=durum_ikonu, prefix='fa')
                ).add_to(marker_cluster)
            except:
                continue

# Haritayı Web Sitesinde Göster
st_folium(m, width=None, height=500)