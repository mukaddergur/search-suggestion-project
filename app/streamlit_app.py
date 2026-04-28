import streamlit as st
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocess import load_project_data, preprocess_queries
from src.suggest import get_suggestions

st.set_page_config(page_title="Search Analytics Pro", layout="wide")

@st.cache_data
def get_data():
    raw = load_project_data()
    return preprocess_queries(raw)

df = get_data()


with st.sidebar:
    st.header("⚙️ Kontrol & Analiz")
    
    with st.expander(" Arama Ayarları", expanded=True):
        top_n = st.slider("Öneri Sayısı", 1, 20, 5)
    
    st.markdown("---")
    st.subheader(" Veri Seti Özeti")
    if not df.empty:
        col_m1, col_m2 = st.columns(2)
        col_m1.metric("Toplam Kayıt", f"{len(df):,}")
        col_m2.metric("Benzersiz", f"{df['query'].nunique():,}")
        
        col_m3, col_m4 = st.columns(2)
        col_m3.metric("Ort. CTR", f"{df['ctr'].mean():.2%}")
        col_m4.metric("Max Uzunluk", f"{df['query_length'].max()}")

    st.markdown("---")
    st.subheader(" Kategori Dağılımı")
    if not df.empty:
        st.bar_chart(df['category'].value_counts())
        st.write(f" **Ort. Kelime Sayısı:** {df['word_count'].mean():.2f}")

    st.markdown("---")
    st.subheader("🔌 Sistem Durumu")
    st.success(" Veri Tabanı Aktif")
    st.info("GitHub Yayınına Hazır")


st.title(" Akıllı Arama ve Sorgu Analiz Sistemi")

user_input = st.text_input("Arama yapın...", placeholder="Orn: atatürk, bilgisayar, ankara")

if user_input:
    res = get_suggestions(user_input, df, top_n)
    if not res.empty:
        st.subheader(" İlgili Sonuçlar")
        for idx, row in res.iterrows():
            st.markdown(f"🔹 **{row['display']}**")
    else:
        st.warning("Eşleşen bir sonuç bulunamadı.")

st.markdown("---")
st.subheader(" İstatistiksel Analiz")
if not df.empty:
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Karakter Uzunluğu Dağılımı**")
        fig1, ax1 = plt.subplots()
        ax1.hist(df['query_length'], bins=20, color='skyblue', edgecolor='black')
        st.pyplot(fig1)
    with c2:
        st.write("**Kelime Sayısı Dağılımı**")
        fig2, ax2 = plt.subplots()
        ax2.hist(df['word_count'], bins=range(1, 10), color='salmon', edgecolor='black', align='left')
        st.pyplot(fig2)