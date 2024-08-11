import streamlit as st
import base64

# Function to set background image
def set_background(image_file_base64):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{image_file_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            width: 100%;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Load the image file and encode it to base64
def load_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Define the path to your image
image_path = r"C:\Users\harshal pardhi\Desktop\background.jpg"  # Use raw string to handle backslashes

# Load and encode the image
image_file_base64 = load_image(image_path)

# Set the background image
set_background(image_file_base64)

# Add some content to the app
st.title("My Streamlit App with Background Image")
st.write("This is a Streamlit app with a custom background image.")
