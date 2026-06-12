# 🍌 Klasifikasi Kematangan Pisang Menggunakan CNN

## 📌 Deskripsi Proyek

Proyek ini merupakan implementasi Computer Vision menggunakan Convolutional Neural Network (CNN) untuk mengklasifikasikan tingkat kematangan pisang berdasarkan gambar.

Model dilatih menggunakan dataset Banana Classification dari Kaggle dan mampu mengklasifikasikan gambar ke dalam empat kategori:

* Overripe
* Ripe
* Rotten
* Unripe

Selain proses training dan evaluasi model, proyek ini juga dilengkapi dengan aplikasi web berbasis Streamlit yang memungkinkan pengguna mengunggah gambar pisang dan mendapatkan hasil prediksi secara langsung.

---

## 🎯 Tujuan Proyek

* Mempelajari alur kerja Computer Vision menggunakan TensorFlow/Keras.
* Mengimplementasikan CNN untuk klasifikasi gambar.
* Melakukan evaluasi model menggunakan data validasi dan data uji.
* Mendeploy model ke dalam aplikasi web sederhana menggunakan Streamlit.

---

## 📂 Dataset

Dataset yang digunakan:

**Banana Classification Dataset**

Kategori:

* Overripe
* Ripe
* Rotten
* Unripe

Struktur dataset:

```text
banana_classification/
│
├── train/
├── valid/
└── test/
```

Dataset tidak disertakan dalam repository karena ukuran file yang besar.

---

## 🔄 Tahapan Proyek

### 1. Pengambilan Dataset

Dataset diunduh menggunakan KaggleHub.

### 2. Eksplorasi Dataset

Melakukan pemeriksaan struktur folder dataset untuk memastikan pembagian data:

* Train
* Validation
* Test

### 3. Loading Dataset

Dataset gambar dimuat menggunakan:

```python
tf.keras.utils.image_dataset_from_directory()
```

Seluruh gambar diubah ukurannya menjadi:

```text
224 x 224 pixel
```

---

### 4. Pembuatan Model CNN

Arsitektur model menggunakan:

* Rescaling
* Conv2D
* MaxPooling2D
* Flatten
* Dense
* Softmax Output Layer

Model digunakan untuk melakukan klasifikasi ke 4 kelas kematangan pisang.

---

### 5. Training Model

Model dilatih menggunakan:

* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy
* Metrics: Accuracy

---

### 6. Evaluasi Model

Evaluasi dilakukan menggunakan:

* Validation Accuracy
* Test Dataset
* Confusion Matrix
* Classification Report

Hasil terbaik yang diperoleh:

**Validation Accuracy ≈ 94.84%**

---

### 7. Deployment Menggunakan Streamlit

Aplikasi web memungkinkan pengguna:

* Upload gambar (.jpg, .jpeg, .png)
* Melihat hasil prediksi
* Melihat confidence score
* Melihat probabilitas untuk setiap kelas

---

## 🛠️ Teknologi yang Digunakan

* Python
* TensorFlow / Keras
* NumPy
* Pillow
* Streamlit
* Matplotlib
* Scikit-Learn

---

## 🚀 Menjalankan Aplikasi

Install dependencies:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
streamlit run app.py
```

---

## 📷 Contoh Penggunaan

1. Upload gambar pisang.
2. Model melakukan prediksi.
3. Sistem menampilkan:

* Kategori kematangan pisang
* Confidence score
* Probabilitas setiap kelas

---

## 📈 Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:

* Transfer Learning (MobileNetV2, EfficientNet)
* Deployment ke Streamlit Cloud
* Penambahan visualisasi Confusion Matrix pada aplikasi
* Optimasi ukuran model
* Dukungan prediksi real-time menggunakan kamera

---


Project pembelajaran Computer Vision dan Deep Learning menggunakan TensorFlow serta Streamlit.
