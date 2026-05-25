from fpdf import FPDF
import sys

def create_dummy_sop():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)
    
    # Title
    pdf.set_font("helvetica", style="B", size=16)
    pdf.cell(200, 10, text="Standar Operasional Prosedur (SOP) - TechCorp ID", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font("helvetica", size=12)
    pdf.cell(200, 10, text="Dokumen Internal Rahasia - Hanya untuk Karyawan", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.cell(200, 10, text="", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", style="B", size=14)
    pdf.cell(200, 10, text="1. Aturan Cuti Karyawan", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", size=12)
    content1 = "Semua karyawan berhak mendapatkan cuti tahunan sebanyak 12 hari per tahun. Pengajuan cuti harus dilakukan melalui portal HRIS selambat-lambatnya 7 hari sebelum tanggal pelaksanaan cuti. Untuk cuti sakit, karyawan wajib melampirkan surat keterangan dokter jika cuti melebihi 2 hari berturut-turut. Jika tidak ada surat dokter, akan dipotong cuti tahunan."
    pdf.multi_cell(0, 8, text=content1)
    
    pdf.cell(200, 10, text="", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", style="B", size=14)
    pdf.cell(200, 10, text="2. Klaim Reimbursement Transportasi", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", size=12)
    content2 = "Penggantian dana (reimbursement) untuk transportasi klien maksimal adalah Rp 150.000 per hari perjalanan. Kwitansi atau bukti struk asli harus diunggah ke sistem keuangan maksimal pada tanggal 25 setiap bulannya. Keterlambatan pengumpulan bukti akan membuat klaim tidak diproses dan hangus."
    pdf.multi_cell(0, 8, text=content2)
    
    pdf.cell(200, 10, text="", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", style="B", size=14)
    pdf.cell(200, 10, text="3. Penggunaan Laptop Perusahaan", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", size=12)
    content3 = "Laptop yang dipinjamkan adalah aset perusahaan. Dilarang menginstal aplikasi bajakan atau game. Segala bentuk kerusakan fisik karena kelalaian (jatuh, ketumpahan air) akan ditanggung 50% oleh karyawan dan 50% oleh perusahaan."
    pdf.multi_cell(0, 8, text=content3)
    
    pdf.output("SOP_Internal_TechCorp.pdf")
    print("Created SOP_Internal_TechCorp.pdf")

if __name__ == "__main__":
    try:
        create_dummy_sop()
    except Exception as e:
        print(f"Failed to generate PDF: {e}")
        print("Note: please ensure fpdf2 is installed (pip install fpdf2)")
