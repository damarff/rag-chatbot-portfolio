import streamlit as st
import os
import tempfile
from rag_engine import RAGSystem

# Set Streamlit page config
st.set_page_config(page_title="RAG AI Assistant", page_icon="🤖", layout="centered")

st.title("📄 AI Document Q&A (RAG)")
st.markdown("Unggah dokumen PDF (misalnya SOP Perusahaan, Buku Manual), lalu tanyakan apa saja. AI akan mencari jawabannya **khusus** dari dalam dokumen tersebut tanpa halusinasi!")

# Load RAG Engine (cached so it doesn't re-initialize on every button click)
@st.cache_resource
def get_rag_system():
    try:
        return RAGSystem()
    except Exception as e:
        st.error(f"Gagal memuat sistem AI: pastikan GEMINI_API_KEY sudah terpasang di .env. Error: {e}")
        return None

rag = get_rag_system()

if rag:
    with st.sidebar:
        st.header("📂 Upload Dokumen")
        uploaded_file = st.file_uploader("Pilih file PDF", type="pdf")
        
        if uploaded_file is not None:
            doc_id = uploaded_file.name
            
            if st.button("Proses Dokumen (Embed)"):
                with st.spinner('Membaca dan memproses teks dokumen menjadi Vector Embeddings...'):
                    # Simpan file sementara untuk dibaca oleh pdfplumber
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                        tmp.write(uploaded_file.getvalue())
                        tmp_path = tmp.name
                    
                    try:
                        # Masukkan ke ChromaDB
                        rag.process_pdf(tmp_path, doc_id)
                        st.success(f"✅ Dokumen '{doc_id}' berhasil dipelajari oleh AI!")
                    except Exception as e:
                        st.error(f"Gagal memproses dokumen: {e}")
                    finally:
                        os.unlink(tmp_path)
    
    st.divider()
    
    st.subheader("💬 Chat dengan Dokumen")
    user_query = st.text_input("Tanyakan sesuatu (Contoh: 'Apa aturan cuti sakit di SOP ini?'):")
    
    if st.button("Kirim"):
        if user_query:
            with st.spinner("🤖 AI sedang mencari konteks di Vector Database dan menyusun jawaban..."):
                answer = rag.query(user_query)
                st.info(answer)
        else:
            st.warning("Mohon ketikkan pertanyaan terlebih dahulu.")
