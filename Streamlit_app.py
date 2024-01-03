
from wand.image import Image as WandImage
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import re
import pandas as pd
import streamlit as st


def extract_text(image_path):
    # Read the image using Wand
    with WandImage(filename=image_path) as img:
        # Convert the image to grayscale
        img.type = 'grayscale'
        img_path = r"E:\360` assignmentes\intern project -text exxtraction\images of store bills\Invoices\Invoice8.jpeg"
        img.save(filename=img_path)

    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(Image.open(img_path))
    return extracted_text


def extract_product_details(text):
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    ground_truth_text = open("D:\invoice texts\invoice 8 text.txt", 'r',).read()

    # Preprocess text 
    ocr_text = extract_text.strip().lower()  
    ground_truth_text = ground_truth_text.strip().lower()

    #Calculate precision and recall 
    true_positives = 0
    for char in ground_truth_text:
        if char in ocr_text:
            true_positives += 1
    precision = true_positives / len(ground_truth_text) 
    recall = true_positives / len(ocr_text) 

    f1 = 2 * [(precision * recall) / (precision + recall)]

    #Print the results
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)


st.title('Invoice Text Extraction')
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    image.save('image.jpg')
    text = extract_text('image.jpg')
    st.write('Extracted Text:')
    st.write(text)

    product_details = extract_product_details(text)
    df = pd.DataFrame(product_details)
    st.write('Product Details:')
    st.write(df)
