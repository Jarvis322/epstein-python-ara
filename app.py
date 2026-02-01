import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Epstein TR Tarayıcı", page_icon="🇹🇷", layout="centered")

# CSS ile Görsel Düzenleme
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #1F2937;
        color: white;
        border: 1px solid #374151;
        padding: 15px;
        border-radius: 8px;
    }
    .stButton>button:hover {
        border-color: #3B82F6;
        color: #3B82F6;
    }
    h1 { color: #3B82F6; }
    .warning { 
        background-color: #331111; 
        padding: 10px; 
        border-radius: 5px; 
        border: 1px solid #550000; 
        font-size: 0.8rem;
        color: #ffaaaa;
    }
    </style>
""", unsafe_allow_html=True)

# Başlık
st.title("🕵️‍♂️ Epstein Belgeleri TR")
st.markdown("Bu araç **justice.gov** veritabanındaki resmi PDF dosyalarını tarar.")

# Fonksiyon: Türkçe Karakter Temizleme
def temizle(metin):
    ceviri = str.maketrans({
        'ç': 'c', 'Ç': 'C',
        'ğ': 'g', 'Ğ': 'G',
        'ı': 'i', 'I': 'I', 'İ': 'I', 'i': 'i',
        'ö': 'o', 'Ö': 'O',
        'ş': 's', 'Ş': 'S',
        'ü': 'u', 'Ü': 'U'
    })
    return metin.translate(ceviri)

# Fonksiyon: Link Oluşturucu
def link_ver(sorgu):
    base_url = "https://www.google.com/search?q=site:justice.gov/epstein+filetype:pdf+"
    # Çift tırnak içine alarak kesin arama yapıyoruz
    final_query = f'%22{temizle(sorgu)}%22'
    
    # Eğer "OR" kullanılmışsa tırnakları kaldırıp paranteze alıyoruz
    if " OR " in sorgu:
        final_query = f'(%22{temizle(sorgu.replace(" OR ", "%22+OR+%22"))}%22)'
        
    return base_url + final_query

# --- SEKME YAPISI ---
tab1, tab2, tab3 = st.tabs(["🔍 İsim Ara", "🏢 Şirket & Siyaset", "🚀 Derin Tarama"])

with tab1:
    st.subheader("Kişi Sorgulama")
    isim = st.text_input("Aranacak İsim Girin", placeholder="Örn: Banu, Gökhan, Mehmet")
    
    if isim:
        temiz_isim = temizle(isim)
        st.info(f"Sistem şu şekilde arayacak: **{temiz_isim}**")
        
        # Link Button (Streamlit'in en güvenli yönlendirme yöntemi)
        st.link_button(f"📂 {isim} İçin Belgeleri Aç", link_ver(isim))
    else:
        st.markdown("Bir isim girin ve butona basın.")

with tab2:
    st.subheader("Özel Listeler")
    st.markdown("İstediğiniz kategorideki isimleri tek tıkla tarayın.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**İş Dünyası & Mekanlar**")
        st.link_button("Hüsnü Özyeğin", link_ver("Husnu Ozyegin"))
        st.link_button("Rixos Hotels", link_ver("Rixos"))
        st.link_button("Grand Hyatt", link_ver("Grand Hyatt Istanbul"))
        st.link_button("Sanko Holding", link_ver("Sanko"))
        st.link_button("Sembol İnşaat", link_ver("Sembol"))

    with col2:
        st.markdown("**Siyaset & Bürokrasi**")
        st.link_button("R. Tayyip Erdoğan", link_ver("Recep Tayyip Erdogan"))
        st.link_button("Ahmet Davutoğlu", link_ver("Ahmet Davutoglu"))
        st.link_button("Mevlüt Çavuşoğlu", link_ver("Mevlut Cavusoglu"))
        st.link_button("Egemen Bağış", link_ver("Egemen Bagis"))
        st.link_button("Tansu Çiller", link_ver("Tansu Ciller"))

with tab3:
    st.subheader("Keşif Modu")
    st.markdown("Bilinmeyen bağlantıları bulmak için genel taramalar.")
    
    st.link_button("🇹🇷 Tüm Türkiye Kayıtları", link_ver("Turkey OR Turkish OR Istanbul"))
    st.link_button("📕 Türk Pasaportları", link_ver("Turkish Passport"))
    st.link_button("📞 +90 Telefon Numaraları", link_ver("+90 OR 0090"))
    st.link_button("✈️ Uçuş & İncirlik Üssü", link_ver("Incirlik OR Ataturk Airport OR Esenboga"))
    
    st.markdown("---")
    st.markdown("**Otomatik Soyadı Taraması (Toplu):**")
    st.caption("Aşağıdaki buton en yaygın 5 Türk soyadını aynı anda arar.")
    st.link_button("Yılmaz, Kaya, Demir, Şahin, Çelik", link_ver("Yilmaz OR Kaya OR Demir OR Sahin OR Celik"))

st.markdown("---")
st.markdown("""
<div class="warning">
⚠️ <strong>YASAL UYARI:</strong><br>
Bu uygulama sadece aracıdır. Sonuçlar Google üzerinden justice.gov sitesinden çekilir. 
İsim benzerlikleri olabilir. Bir ismin belgede geçmesi suçlu olduğu anlamına gelmez.
</div>
""", unsafe_allow_html=True)
