import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

np.random.seed(42)
jumlah_data = 400

budget          = np.random.randint(100000, 5000000, jumlah_data)   # Rp per bulan
waktu_luang     = np.random.randint(1, 21, jumlah_data)             # jam per minggu
level_fisik     = np.random.randint(1, 11, jumlah_data)             # skala 1-10
tujuan          = np.random.randint(1, 4, jumlah_data)              # 1=kesehatan, 2=sosial, 3=kompetisi
jumlah_teman    = np.random.randint(0, 11, jumlah_data)             # orang yang bisa diajak

label = []
for i in range(jumlah_data):

    # Golf: budget sangat tinggi, waktu banyak, tujuan sosial/eksklusif
    if budget[i] >= 3000000 and waktu_luang[i] >= 8 and tujuan[i] in [2, 3]:
        label.append("Golf")

    # Padel: budget menengah-tinggi, butuh teman, lagi booming
    elif budget[i] >= 1000000 and jumlah_teman[i] >= 3 and tujuan[i] in [2, 3]:
        label.append("Padel")

    # Tenis: budget menengah, fisik oke, kompetitif
    elif budget[i] >= 500000 and level_fisik[i] >= 6 and tujuan[i] in [1, 3]:
        label.append("Tenis Lapangan")

    # Badminton: semua kondisi, murah, fleksibel
    else:
        label.append("Badminton")

df = pd.DataFrame({
    "budget_per_bulan":       budget,
    "waktu_luang_per_minggu": waktu_luang,
    "level_fisik":            level_fisik,
    "tujuan":                 tujuan,
    "jumlah_teman":           jumlah_teman,
    "label":                  label
})

df.to_csv("dataset_olahraga.csv", index=False)
print("Dataset berhasil dibuat!")
print(df["label"].value_counts())



fitur = ["budget_per_bulan", "waktu_luang_per_minggu", "level_fisik", "tujuan", "jumlah_teman"]
X = df[fitur]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model.pkl berhasil dibuat!")
