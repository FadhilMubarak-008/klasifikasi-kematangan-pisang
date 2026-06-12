import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("model_pisang.keras")

# Nama kelas
class_names = [
    "overripe",
    "ripe",
    "rotten",
    "unripe"
]

st.title("🍌 klasifikasi kematangan pisang")

st.write(
    "Upload gambar pisang dan model akan memprediksi tingkat kematangannya."
)

uploaded_file = st.file_uploader(
    "Pilih gambar",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Gambar yang diupload",
        use_container_width=True
    )

    image = image.resize((224, 224))

    img_array = np.array(image)

    # RGB
    if len(img_array.shape) == 2:
        img_array = np.stack(
            (img_array,) * 3,
            axis=-1
        )

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(
        img_array,
        verbose=0
    )

    predicted_class = class_names[
        np.argmax(prediction)
    ]

    confidence = np.max(prediction)

    st.success(
        f"Prediksi: {predicted_class}"
    )

    st.write(
        f"Confidence: {confidence:.2%}"
    )

    st.subheader("Probabilitas Tiap Kelas")

    for i, class_name in enumerate(class_names):
        st.write(
            f"{class_name}: {prediction[0][i]:.2%}"
        )