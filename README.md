#  Akıllı Arama ve Sorgu Analiz Sistemi

Bu proje, hem dünya şehirlerini hem de genel kelime haznesini (Unigram) birleştirerek kullanıcıya en doğru arama önerilerini sunan, hibrit skorlama mantığına sahip gelişmiş bir web portalıdır. **Streamlit** tabanlı arayüzü ile arama motoru mantığını istatistiksel grafiklerle birleştirir.

##  Öne Çıkan Özellikler

- **Hibrit Veri Seti:** 40.000+ şehir verisi (World Cities) ve 300.000+ genel kavramın (English Word Frequency) birleşiminden oluşur.
- **Akıllı Skorlama Motoru:**
    - **Substring (Alt-Dizgi):** Kelime içinde harf eşleşmesi kontrolü.
    - **Token Overlap (Kelime Örtüşmesi):** Çoklu kelime sorgularında anlamlı kesişim yakalama.
    - **Ağırlıklı Popülerlik:** Eşleşen sonuçları %10 (0.1 katsayısı) popülerlik ağırlığı ile sıralama.
- **Kapsamlı Analiz Paneli:** Sol panelde toplam kelime haznesi, ortalama CTR ve sorgu uzunluğu gibi metrikler anlık hesaplanır.
- **Görsel İstatistikler:** Karakter uzunluğu ve kelime sayısı dağılımı histogram grafiklerle sunulur.

## Sanal Ortam(venv) Kurulumu

 1) Sanal ortam oluşturma
python -m venv venv

 2) Sanal ortamı aktif etme (Windows)
venv\Scripts\activate

 3) Sanal ortamı aktif etme (Mac/Linux)
source venv/bin/activate



### Kurulum
Sistem gereksinimlerini yüklemek için:
`pip install streamlit pandas matplotlib`

### Çalıştırma
Uygulamayı başlatmak için:
`streamlit run app/streamlit_app.py`
##  Dosya Yapısı

```text
search-suggestion-project/
├── app/
│   └── streamlit_app.py     # Ana uygulama ve arayüz
├── data/
│   ├── worldcities.csv      # Lokasyon verileri
│   └── unigram_freq.csv     # Genel kelime haznesi
├── src/
│   ├── preprocess.py        # Veri temizleme ve birleştirme
│   └── suggest.py           # Arama ve skorlama motoru
└── README.md                # Proje dökümantasyonu


