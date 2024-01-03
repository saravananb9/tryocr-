import streamlit as st 
def main():
    st.title('Optical Character Recognition (OCR) App')

    # Get user input for uploading an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Convert the uploaded image to a PIL image
        image = Image.open(uploaded_file)

        # Perform OCR on the image
        ocr_output =  extract_text(image)

        # Display the original image
        st.subheader('Original Image:')
        st.image(image, width=400)

        # Display the OCR output
        st.subheader('OCR Output:')
        st.write(ocr_output)

if __name__ == '__main__':
    main()
