"""
Grayscale Camera App using Streamlit.

This app captures an image from the user's webcam, converts it to grayscale,
and displays the processed image on the web interface.

Requirements:
- streamlit
- pillow (PIL)

To run:
    streamlit run app.py
"""

import streamlit as st
from PIL import Image

# Set the title of the app
st.title("Grayscale Camera App")

# Create an expandable section labeled "Start Camera"
with st.expander("Start Camera"):
    # Display the camera input widget. User must take a photo here.
    camera_image = st.camera_input("Camera")

# Check if a photo has been taken and returned by the camera widget
if camera_image:
    # Create a pillow image instace
    # Open the image file from the camera input
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale using Pillow
    gray_img = img.convert("L")

    # Display the grayscale image on the Streamlit app
    st.image(gray_img)


