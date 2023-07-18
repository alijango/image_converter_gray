import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

upload_img = st.file_uploader("Upload Image")




with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input('Camera')


if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)
    # convert the pillow img to grayscale
    img_gray = img.convert('L')
    # render the grayscale img to webpage
    st.image(img_gray)

if upload_img:
    image_loc = Image.open(upload_img)
    image_loc_gray = image_loc.convert('L')
    st.image(image_loc_gray)
