from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse
from predictor import prediksi

app = FastAPI(
    title="API Rekomendasi Olahraga 🏸⛳🎾",
    description="""
Rekomendasi olahraga berdasarkan budget, waktu luang, kondisi fisik, tujuan, dan jumlah teman.

**Hasil prediksi:**
- 🏸 Badminton → budget terbatas, fleksibel, cocok semua kondisi
- 🎾 Tenis Lapangan → budget menengah, fisik bagus, suka kompetisi
- 🟢 Padel → budget menengah-tinggi, sosial
- ⛳ Golf → budget tinggi, waktu banyak, eksklusif
""",
    version="1.0.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": 1,
        "docExpansion": "none",
        "deepLinking": True,
    }
)


class DataPengguna(BaseModel):
    budget_per_bulan: int = Field(..., example=500000, description="Budget olahraga per bulan dalam Rupiah")
    waktu_luang_per_minggu: int = Field(..., example=5, description="Jam luang per minggu (1-20)")
    level_fisik: int = Field(..., example=7, description="Kondisi fisik: 1=sangat lemah, 10=sangat bugar")
    tujuan: int = Field(..., example=1, description="Tujuan olahraga: 1=Kesehatan, 2=Sosial/Gaul, 3=Kompetisi")
    jumlah_teman: int = Field(..., example=3, description="Jumlah teman yang bisa diajak")


@app.get("/", response_class=HTMLResponse)
def beranda():
    return """
    <h2 style='color:#2ca02c'>API Rekomendasi Olahraga Aktif 🏸🎾⛳</h2>
    <p style='color:#555'>Gunakan endpoint <b>/predict</b> dengan POST untuk mendapatkan rekomendasi olahraga sesuai kondisi Anda.</p>
    """


@app.post("/predict", description="""
Kirim data kondisi kamu, sistem akan merekomendasikan olahraga yang paling cocok.

**Panduan Pengisian:**
- budget_per_bulan → Budget olahraga per bulan dalam Rupiah. Contoh: `500000`
- waktu_luang_per_minggu → Jam luang dalam seminggu. Contoh: `5` (1-20)
- level_fisik → Kondisi fisik saat ini (1=lemah, 10=bugar)
- tujuan → Tujuan olahraga (1=Kesehatan, 2=Sosial/Gaul, 3=Kompetisi)
- jumlah_teman → Jumlah teman yang bisa diajak

**Hasil prediksi:**
- 🏸 Badminton → budget terbatas, fleksibel, cocok semua kondisi
- 🎾 Tenis Lapangan → budget menengah, fisik bagus, suka kompetisi
- 🟢 Padel → budget menengah-tinggi, sosial, butuh teman
- ⛳ Golf → budget tinggi, waktu banyak, eksklusif
""")
def predict(data: DataPengguna):
    input_data = data.model_dump()
    hasil = prediksi(input_data)
    return hasil