# API Rekomendasi Olahraga 

API ini merekomendasikan olahraga yang paling cocok berdasarkan kondisi pengguna.  
Pilihan olahraga: **Badminton**, **Tenis Lapangan**, **Padel**, atau **Golf**.

---

## Struktur File

```
olahraga_api/
├── buat_dataset.py       # (tidak dikumpulkan) Script membuat dataset
├── train_model.py        # (tidak dikumpulkan) Script melatih model
├── dataset_olahraga.csv  # (tidak dikumpulkan) Dataset hasil generate
├── model.pkl             # File model yang sudah dilatih
├── predictor.py          #  Modul validasi dan prediksi
├── main.py               #  Web service (FastAPI)
└── README.md             #  Dokumentasi ini
```

---

## Cara Menjalankan

### 1. Install library

```bash
pip install fastapi uvicorn scikit-learn pandas
```

### 2. Jalankan API

```bash
uvicorn main:app --reload
```

API berjalan di: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Cara Menggunakan API

### Endpoint

| Method | URL       | Keterangan             |
|--------|-----------|-----------------------|
| GET    | `/`       | Cek API aktif          |
| POST   | `/predict`| Kirim data untuk rekomendasi |

---

### Format Input (JSON)

```json
{
  "budget_per_bulan": 500000,
  "waktu_luang_per_minggu": 5,
  "level_fisik": 7,
  "tujuan": 1,
  "jumlah_teman": 3
}
```

### Keterangan Kolom

| Kolom | Tipe | Keterangan | Batas |
|-------|------|------------|-------|
| `budget_per_bulan`      | angka | Budget olahraga per bulan (Rp) | 100.000 – 5.000.000 |
| `waktu_luang_per_minggu`| angka | Jam luang dalam seminggu        | 1 – 20 |
| `level_fisik`           | angka | Kondisi fisik. 1=sangat lemah, 10=sangat bugar | 1 – 10 |
| `tujuan`                | angka | 1=Kesehatan, 2=Sosial/Gaul, 3=Kompetisi | 1 – 3 |
| `jumlah_teman`          | angka | Jumlah teman yang bisa diajak olahraga | 0 – 10 |

---

### Contoh Respons

**Rekomendasi sukses:**

```json
{
  "rekomendasi_olahraga": "Padel",
  "status": "sukses"
}
```

**Jika input salah:**

```json
{
  "error": "Nilai 'tujuan' harus antara 1 dan 3.",
  "status": "gagal"
}
```

---

## Penjelasan Olahraga

- `"Badminton"` — budget terbatas, fleksibel, cocok semua kondisi  
- `"Tenis Lapangan"` — budget menengah, fisik bagus, suka kompetisi  
- `"Padel"` — budget menengah-tinggi, suka olahraga sosial, butuh teman  
- `"Golf"` — budget tinggi, waktu banyak, tujuan sosial/eksklusif  

---

## Dokumentasi Interaktif

Buka browser setelah API dijalankan: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
