import pickle
import pandas as pd

KOLOM = ["budget_per_bulan", "waktu_luang_per_minggu", "level_fisik", "tujuan", "jumlah_teman"]

BATAS = {
    "budget_per_bulan":       (100000, 5000000),
    "waktu_luang_per_minggu": (1, 20),
    "level_fisik":            (1, 10),
    "tujuan":                 (1, 3),
    "jumlah_teman":           (0, 10),
}

KETERANGAN_TUJUAN = {
    1: "Kesehatan",
    2: "Sosial / Gaul",
    3: "Kompetisi"
}


def load_model(path="model.pkl"):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


def validasi_input(data: dict):
    for kolom in KOLOM:
        if kolom not in data:
            raise ValueError(f"Kolom '{kolom}' tidak ditemukan dalam input.")

        nilai = data[kolom]

        if not isinstance(nilai, (int, float)):
            raise TypeError(f"Kolom '{kolom}' harus berupa angka, bukan '{type(nilai).__name__}'.")

        batas_bawah, batas_atas = BATAS[kolom]
        if not (batas_bawah <= nilai <= batas_atas):
            raise ValueError(f"Nilai '{kolom}' harus antara {batas_bawah} dan {batas_atas}.")


def preprocess(data: dict):
    return pd.DataFrame([[data[k] for k in KOLOM]], columns=KOLOM)


def prediksi(data: dict):
    try:
        validasi_input(data)
        model = load_model()
        input_model = preprocess(data)
        hasil = model.predict(input_model)[0]
        return {"rekomendasi_olahraga": hasil, "status": "sukses"}

    except (ValueError, TypeError) as e:
        return {"error": str(e), "status": "gagal"}

    except Exception as e:
        return {"error": "Terjadi kesalahan pada server.", "detail": str(e), "status": "gagal"}
