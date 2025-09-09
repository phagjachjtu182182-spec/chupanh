import streamlit as st
import cv2
import numpy as np
import os
from datetime import datetime

# Thư mục lưu ảnh
SAVE_DIR = "uploaded_images"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

st.set_page_config(page_title="Ứng dụng nhận diện gà", layout="centered")
st.title("🐓 Ứng dụng nhận diện gà")

# Hàm chèn chữ lên ảnh
def add_text_to_image(image, text):
    img = image.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, text, (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return img

# Upload ảnh
uploaded_file = st.file_uploader("Tải ảnh gà lên", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Thêm chữ nếu cần
    label = st.text_input("Nhập chữ muốn in lên ảnh (ví dụ: Gà số 1):")
    if label:
        img = add_text_to_image(img, label)

    # Lưu ảnh
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    filepath = os.path.join(SAVE_DIR, filename)
    cv2.imwrite(filepath, img)

    st.image(img, channels="BGR", caption="Ảnh vừa tải lên")
