import streamlit as st
import easyocr
import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Streamlit UI
st.title("OCR & QR Code Scanner S")

# Show options for OCR or QR Code scanning
option = st.selectbox("Select Mode", ("OCR from Image", "Scan QR Code"))

if option == "OCR from Image":
    st.subheader("Capture Image for OCR")
    # Upload image or take a picture from the camera
    image_file = st.camera_input("Take a picture")

    if image_file:
        # Convert the uploaded image to a format that OpenCV can use
        img = np.array(bytearray(image_file.read()), dtype=np.uint8)
        img = cv2.imdecode(img, 1)
        
        # Perform OCR
        results = reader.readtext(img)
        
        # Display OCR results
        if results:
            st.write("OCR Text Extracted:")
            for result in results:
                st.write(result[1])  # result[1] is the detected text
        else:
            st.write("No text detected!")

elif option == "Scan QR Code":
    st.subheader("Capture Image for QR Code")
    # Upload image or take a picture from the camera
    qr_image = st.camera_input("Take a picture")

    if qr_image:
        # Convert the uploaded image to a format that OpenCV can use
        img = np.array(bytearray(qr_image.read()), dtype=np.uint8)
        img = cv2.imdecode(img, 1)

        # Decode QR code
        qr_codes = decode(img)
        
        # Display the QR code data
        if qr_codes:
            for qr in qr_codes:
                qr_data = qr.data.decode("utf-8")
                st.write("QR Code Data:", qr_data)
        else:
            st.write("No QR code detected!")
