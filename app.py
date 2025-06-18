
import streamlit as st

st.set_page_config(page_title="Chatbot FAQ Disdukcapil", layout="centered")

st.title("Chatbot FAQ Disdukcapil")
st.write("Halo! Silakan ketik pertanyaan Anda seputar layanan Disdukcapil.")

pertanyaan = st.text_input("Pertanyaan Anda")

faq = {
    "cara mengurus akta kelahiran": "Silakan datang ke Disdukcapil dengan membawa KK dan surat kelahiran dari RS.",
    "syarat menikah": "Syaratnya adalah KTP, KK, dan surat pengantar dari RT/RW.",
    "ubah status perkawinan": "Bawa akta nikah atau akta cerai dan datang ke Disdukcapil.",
    "ganti nama di KK": "Bawa surat keputusan pengadilan tentang perubahan nama."
}

if pertanyaan:
    jawaban = "Maaf, saya belum tahu jawaban untuk itu."
    for kunci in faq:
        if kunci in pertanyaan.lower():
            jawaban = faq[kunci]
            break
    st.success(jawaban)
