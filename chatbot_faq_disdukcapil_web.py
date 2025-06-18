import streamlit as st
from fuzzywuzzy import fuzz

# Data FAQ: keyword → jawaban
faq_data = {
    "ktp baru": "Untuk perekaman KTP baru, Anda hanya perlu membawa fotocopy Kartu Keluarga dan melapor kepada petugas di loket pelayanan Dukcapil.",
    "KTP baru": "Untuk perekaman KTP baru, Anda hanya perlu membawa fotocopy Kartu Keluarga dan melapor kepada petugas di loket pelayanan Dukcapil..",
    "Ktp baru": "Untuk merekam KTP baru, Anda hanya perlu membawa fotocopy Kartu Keluarga dan melapor kepada petugas di loket pelayanan Dukcapil.",
    "ktp rekam baru": "Untuk merekam KTP baru, Anda hanya perlu membawa fotocopy Kartu Keluarga dan melapor kepada petugas di loket pelayanan Dukcapil.",
    "KTP rekam baru": "Untuk merekam KTP baru, Anda hanya perlu membawa fotocopy Kartu Keluarga dan melapor kepada petugas di loket pelayanan Dukcapil.",
    "Ktp rekam baru": "Untuk merekam KTP baru, Anda hanya perlu membawa fotocopy Kartu Keluarga dan melapor kepada petugas di loket pelayanan Dukcapil.",
    "ktp hilang": "Untuk ktp hilang, anda hanya perlu membawa surat keterangan kehilangan dari kepolisian ke kantor Dukcapil.",
    "ktp rusak": "Untuk ktp rusak, anda hanya perlu membawa ktp asli yang rusak ke kantor Dukcapil untuk proses pembuatan KTP baru.",
    "ktp elemen data": "Untuk elemen data atau perubahan data, anda perlu mengkonfirmasi apakah di kartu keluarga elemen tersebut sudah terganti, selanjutnya jika sudah terganti anda hanya perlu membawa ktp asli ke kantor Dukcapil dan apabila belum terganti anda perlu membawa kartu keluarga asli. Namun jika anda ingin melakukan perubahan pada nama,anda perlu membawa ijazah terakhir.",

    "kk baru": "Untuk pembuatan Kartu Keluarga baru bagi pasangan yang baru menikah, silakan membawa KK masing-masing, Akta Perkawinan, serta KTP suami dan istri. Dokumen tersebut juga diperlukan untuk proses perubahan elemen data",
    "kartu keluarga baru": "Untuk pembuatan Kartu Keluarga baru bagi pasangan yang baru menikah, silakan membawa KK masing-masing, Akta Perkawinan, serta KTP suami dan istri. Dokumen tersebut juga diperlukan untuk proses perubahan elemen data",
    "kartu keluarga hilang": "Jika Kartu Keluarga Anda hilang, silakan membawa surat keterangan kehilangan dari kepolisian ke kantor Dukcapil. Namun, jika Anda masih memiliki fotocopynya, petugas operator dapat melakukan pengecekan dan mencetak ulang KK Anda.",
    "kk hilang": "Jika Kartu Keluarga Anda hilang, silakan membawa surat keterangan kehilangan dari kepolisian ke kantor Dukcapil. Namun, jika Anda masih memiliki fotocopynya, petugas operator dapat melakukan pengecekan dan mencetak ulang KK Anda.",
    "kk elemen data": "Untuk melakukan perubahan atau pembaruan elemen data pada Kartu Keluarga, silakan membawa KK Anda ke kantor Dukcapil dan melapor kepada petugas di loket pelayanan.Jika perubahan elemen data berkaitan dengan status perkawinan yang belum tercatat di KK, Anda perlu membawa Akta Perkawinan sebagai dokumen pendukung.Apabila perubahan disebabkan oleh ketidaksesuaian nama, silakan lampirkan ijazah terakhir.Untuk perubahan elemen data pekerjaan, cukup membawa KK asli dan melapor kepada petugas di loket pelayanan.",
    "kartu keluarga elemen data": "Untuk melakukan perubahan atau pembaruan elemen data pada Kartu Keluarga, silakan membawa KK Anda ke kantor Dukcapil dan melapor kepada petugas di loket pelayanan.Jika perubahan elemen data berkaitan dengan status perkawinan yang belum tercatat di KK, Anda perlu membawa Akta Perkawinan sebagai dokumen pendukung.Apabila perubahan disebabkan oleh ketidaksesuaian nama, silakan lampirkan ijazah terakhir.Untuk perubahan elemen data pekerjaan, cukup membawa KK asli dan melapor kepada petugas di loket pelayanan.",
    "kartu keluarga karena pindah(kel/kec)": "anda perlu melampirkan surat keterangan pindah WNI(antar kelurahan atau antar kecamatan) dari kelurahan dan kartu keluarga asli",

    "akta kelahiran baru": "Untuk pembuatan Akta Kelahiran baru bagi anak yang baru lahir, Anda dapat membawa surat keterangan lahir dari rumah sakit atau bidan tempat melahirkan, fotocopy KTP kedua orang tua, dan Kartu Keluarga. Sementara itu, untuk anak yang sudah berusia beberapa tahun namun belum memiliki Akta Kelahiran sejak lahir (misalnya usia 4 tahun), Anda tetap dapat mengurusnya dengan membawa dokumen yang sama dan melapor kepada petugas di loket pelayanan Dukcapil.",
    "akte kelahiran baru": "Untuk pembuatan Akta Kelahiran baru bagi anak yang baru lahir, Anda dapat membawa surat keterangan lahir dari rumah sakit atau bidan tempat melahirkan, fotocopy KTP kedua orang tua, dan Kartu Keluarga. Sementara itu, untuk anak yang sudah berusia beberapa tahun namun belum memiliki Akta Kelahiran sejak lahir (misalnya usia 4 tahun), Anda tetap dapat mengurusnya dengan membawa dokumen yang sama dan melapor kepada petugas di loket pelayanan Dukcapil.",
    "akte baru": "Untuk pembuatan Akta Kelahiran baru bagi anak yang baru lahir, Anda dapat membawa surat keterangan lahir dari rumah sakit atau bidan tempat melahirkan, fotokopi KTP kedua orang tua, dan Kartu Keluarga. Sementara itu, untuk anak yang sudah berusia beberapa tahun namun belum memiliki Akta Kelahiran sejak lahir (misalnya usia 4 tahun), Anda tetap dapat mengurusnya dengan membawa dokumen yang sama dan melapor kepada petugas di loket pelayanan Dukcapil.",
    "akta kelahiran hilang": "Jika Akte Kelahiran Anda hilang, silakan membawa surat keterangan kehilangan dari kepolisian ke kantor Dukcapil. Namun, jika Anda masih memiliki fotocopynya, petugas operator dapat melakukan pengecekan dan mencetak ulang Akte Kelahiran Anda.",
    "akte kelahiran hilang": "Jika Akte Kelahiran Anda hilang, silakan membawa surat keterangan kehilangan dari kepolisian ke kantor Dukcapil. Namun, jika Anda masih memiliki fotocopynya, petugas operator dapat melakukan pengecekan dan mencetak ulang Akte Kelahiran Anda.",

    "akta kematian": "Untuk pembuatan akte kematian berkas/dokumen yang anda perlu lampirkan seperti surat keterangan kematian dari kelurahan, formulir pelaporan kematian dari kelurahan, surat keterangan kematian dari Rumah Sakit(dokter/paramedis), surat pernyataan apabila yang meninggal sudah 1 tahun keatas, SPTJM kematian bagi yang tidak memiliki surat keterangan kematian dari Rumah Sakit,kartu keluarga asli ",
    "akte kematian": "Untuk membuat akta kematian, dibutuhkan surat kematian dari rumah sakit dan KTP serta KK almarhum.",

    "akte perkawinan hilang": "Anda perlu membawa dan melampirkan dokumen sebagai berikut: surat kehilangan dari kepolisian, Kartu Keluarga, KTP, surat nikah gereja atau surat keterangan dari gereja, surat pernyataan, STPJM suami istri, surat permohonan, serta surat keterangan kebenaran suami istri dari kelurahan.",
    "Akte perkawinan hilang": "Anda perlu membawa dan melampirkan dokumen sebagai berikut: surat kehilangan dari kepolisian, Kartu Keluarga, KTP, surat nikah gereja atau surat keterangan dari gereja, surat pernyataan, STPJM suami istri, surat permohonan, serta surat keterangan kebenaran suami istri dari kelurahan.",
    "perkawinan": "Untuk pendaftaran perkawinan, Anda perlu melampirkan dokumen seperti Fotocopy Kartu Keluarga, Fotocopy KTP, Fotocopy Akta Kelahiran, Surat pernyataan belum menikah, surat pernyataan cerai mati atau cerai hidup sesuai  dengan kondisi, Surat pernyataan sudah diberkati tapi belum dicatatkan namun sudah 1 KK, Foto gandeng sebanyak 1 lembar,Materai Rp10.000 sebanyak 2 lembar.",
    "akte perceraian": "Untuk pembuatan akte perceraian anda perlu melampirkan putusan perceraian dari Pengadilan Asli, pengantar dari Pengadilan, akta perkawinan asli suami-istri, KTP suami-istri, Kartu Keluarga suami-istri, formulir pencatatan perceraian, formulir permohonan perceraian.",

    "kia baru": "Untuk pembuatan KIA atau Kartu Identitas Anak, anda hanya perlu membawa fotocopy Kartu Keluarga dan untuk anak usia 5-17 tahun perlu menggunakan pas foto.",
    "KIA baru": "Untuk pembuatan KIA atau Kartu Identitas Anak, anda hanya perlu membawa fotocopy Kartu Keluarga dan untuk anak usia 5-17 tahun perlu menggunakan pas foto.",
    "kia hilang": "Untuk KIA atau Kartu Identitas Anak hilang, anda hanya perlu melapor di kantor Dukcapil dengan membawa fotocopy Kartu Keluarga.",
    "KIA hilang": "Untuk KIA atau Kartu Identitas Anak hilang, anda hanya perlu melapor di kantor Dukcapil dengan membawa fotocopy Kartu Keluarga.",

    "jam buka": "Pelayanan di Disdukcapil Tomohon buka senin-kamis pukul 08:00 - 17:00 WIB, jumat 08:00 - 02:00 WIB",
    "Jam buka": "Pelayanan di Disdukcapil Tomohon buka senin-kamis pukul 08:00 - 17:00 WIB, jumat 08:00 - 02:00 WIB",
}

# Fungsi pencocokan keyword
def get_response(user_input):
    user_input = user_input.lower()
    for keyword, answer in faq_data.items():
        if keyword in user_input:
            return answer
    return "Maaf, saya tidak memahami pertanyaan Anda. Silakan hubungi petugas."

# Header
st.markdown('<h4 class="header">🤖 FAQ Disdukcapil Tomohon</h4>', unsafe_allow_html=True)
st.markdown("---")

# Chat history (agar tidak hilang setelah kirim)
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# BAGIAN SIDEBAR (FAQ)
with st.sidebar:   
    st.markdown("---")
    st.markdown('<div class="info-box">ℹ️ Informasi lebih lanjut hubungi:<br>🌐 disdukcapil.tomohon.go.id<br>🏢 Jl. Slanag, Kel. Kolongan Satu\nKec. Tomohon Tengah</div>', unsafe_allow_html=True)
# === FAQ Dukcapil ===
with st.expander("Kartu Tanda Penduduk"):
    if st.button("Bagaimana cara mengurus KTP hilang?"):
        response = get_response("Bagaimana cara mengurus KTP hilang?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus KTP hilang?"))
        st.session_state.chat_log.append(("🤖", response))

    if st.button("Bagaimana cara melakukan perekaman KTP baru?"):
        response = get_response("Bagaimana cara melakukan perekaman KTP baru?")
        st.session_state.chat_log.append(("", "Bagaimana cara melakukan perekaman KTP baru?"))
        st.session_state.chat_log.append(("🤖", response))

    if st.button("Bagaimana cara mengurus KTP elemen data?"):
        response = get_response("Bagaimana cara mengurus KTP elemen data?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus KTP elemen data?"))
        st.session_state.chat_log.append(("🤖", response))

    if st.button("Apakah bisa mengurus KTP rusak?"):
        response = get_response("Apakah bisa mengurus KTP rusak?")
        st.session_state.chat_log.append(("", "Apakah bisa mengurus KTP rusak?"))
        st.session_state.chat_log.append(("🤖", response))

with st.expander("Akte Kelahiran"):
    if st.button("bagaimana cara mengurus akte kelahiran baru?"):
        response = get_response("Bagaimana cara mengurus akte kelahiran baru?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus akte kelahiran baru?"))
        st.session_state.chat_log.append(("🤖", response))

    if st.button("bagaimana cara mengurus akte kelahiran hilang ?"):
        response = get_response("Bagaimana cara mengurus akte kelahiran hilang?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus akte kelahiran hilang?"))
        st.session_state.chat_log.append(("🤖", response))       

with st.expander("Perkawinan dan Perceraian"):
    if st.button("bagaimana cara mengurus akte perkawinan hilang ?"):
        response = get_response("Bagaimana cara mengurus akte perkawinan hilang?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus akte perkawinan hilang?"))
        st.session_state.chat_log.append(("🤖", response))  
    
    if st.button("bagaimana cara mengurus akte perceraian ?"):
        response = get_response("Bagaimana cara mengurus akte perceraian?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus akte perceraian?"))
        st.session_state.chat_log.append(("🤖", response))  

    if st.button("bagaimana cara mengurus perkawinan ?"):
        response = get_response("Bagaimana cara mengurus perkawinan?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus perkawinan?"))
        st.session_state.chat_log.append(("🤖", response))  
             
             
with st.expander("Kartu Identitas Anak"):
    if st.button("bagaimana cara mengurus KIA baru ?"):
        response = get_response("Bagaimana cara mengurus KIA baru?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus KIA baru?"))
        st.session_state.chat_log.append(("🤖", response))  

    if st.button("bagaimana cara mengurus KIA hilang ?"):
        response = get_response("Bagaimana cara mengurus KIA hilang?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus KIA hilang?"))
        st.session_state.chat_log.append(("🤖", response))            
with st.expander("Kartu Keluarga"):
    if st.button("bagaimana cara mengurus Kartu Keluarga baru ?"):
        response = get_response("Bagaimana cara mengurus kartu keluarga baru?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus kartu keluarga baru?"))
        st.session_state.chat_log.append(("🤖", response))    
            
    if st.button("bagaimana cara mengurus kartu keluarga hilang ?"):
        response = get_response("Bagaimana cara mengurus kartu keluarga hilang?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus kartu keluarga hilang?"))
        st.session_state.chat_log.append(("🤖", response))        
    
    if st.button("bagaimana cara mengurus Kartu Keluarga elemen data ?"):
        response = get_response("Bagaimana cara mengurus Kartu Keluarga elemen data?")
        st.session_state.chat_log.append(("", "Bagaimana cara mengurus Kartu Keluarga elemen data?"))
        st.session_state.chat_log.append(("🤖", response))        
    
#Input pengguna
user_input = st.chat_input("Ketik pertanyaan Anda:")

if user_input:
    response = get_response(user_input)
    st.session_state.chat_log.append(("", user_input))
    st.session_state.chat_log.append(("🤖", response))

# Tampilkan percakapan
for sender, msg in st.session_state.chat_log:
    if sender == "":
        # Pesan pengguna di sebelah kanan dengan warna biru tua
        st.markdown(f'''
            <div style="text-align: right; margin-bottom: 5px;">
                <div style="display: inline-block; background-color: #003366; color: white; padding: 10px; border-radius: 10px 0px 10px 10px; max-width: 80%;">
                    {msg}
                </div>
            </div>
        ''', unsafe_allow_html=True)
    else:
        # Pesan bot di sebelah kiri dengan warna putih
        st.markdown (f'''
            <div style="text-align: left; margin-bottom: 5px;">
                <div style="display: inline-block; background-color: #FFFFFF; color: black; padding: 10px; border-radius: 0px 10px 10px 10px; max-width: 80%; border: 1px solid #ccc;">
                    {msg}
                </div>
            </div>
        ''', unsafe_allow_html=True)


