import streamlit as st 
import os 
import google.generativeai as genai 
from PIL import Image
from dotenv import load_dotenv
# loading all env vairables.
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
print(os.getenv("GOOGLE_API_KEY"))
## Function to load gemini pro model and get repsonses
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_reponse(input,image):
    if input !="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Applicaiton for image to text.")
input=st.text_input("Input Prompt:",key="input")
submit=st.button("Ask the question.")


uplaod_file=st.file_uploader("Choose an image.",type=["jpg","jpeg","png"])
image=""
if uplaod_file is not None:
    image=Image.open(uplaod_file)
    st.image(image,caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the image.")

## if submit is true 
if submit:
    response=get_gemini_reponse(input,image)
    st.header("Response is:")
    st.write(response)