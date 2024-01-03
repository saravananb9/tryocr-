from wand.image import Image as WandImage
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    # Read the image using Wand
    with WandImage(filename=image_path) as img:
        # Convert the image to grayscale
        img.type = 'grayscale'
        img_path = r"E:\360`  assignmentes\intern  project -text exxtraction\images of store bills\Invoices\Invoice8.jpeg"
        img.save(filename=img_path)

    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(Image.open(img_path))
    return extracted_text

# Provide the path to your image
image_path = r"E:\360`  assignmentes\intern  project -text exxtraction\images of store bills\Invoices\Invoice8.jpeg"
# Extract text from the image
text = extract_text(image_path)

# Display the image
image = Image.open(image_path)
plt.imshow(image)
plt.show()

# Print the extracted text
print("Extracted Text:",text)


                                        ##### model evaluatio or accuracy #####
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ground_truth_text = open("D:\invoice texts\invoice 8 text.txt", 'r',).read()

# Preprocess text 
ocr_text = text.strip().lower()  
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

                                                   ##### model data frame ##### 

import re
import pandas as pd

# Extracting Bill Date
matching_bill_date = re.search(r"(\d{2}/\d{2}/\d{4})", text)
bill_date = matching_bill_date.group(1) if matching_bill_date else None

# Extracting Bill Number
matching_bill_number = re.search(r"(\d{9}-\d{6})", text)
bill_number = matching_bill_number.group(1) if matching_bill_number else None

# Extracting Product Details
product_details = []

matches = re.finditer(r"(\d+)\s*(\w+(?:\s+\w+)*)\s*(\d+\.\d+)\s*(\d+\.\d+)", text)

for match in matches:
    product_details.append({
        "product_name": match.group(2),
        "quantity": match.group(1),
        "value": match.group(4)
    })


df = pd.DataFrame(product_details)

# Adding Bill Date and Bill Number to the DataFrame
df["Bill Date"] = bill_date
df["Bill Number"] = bill_number

print(df)
