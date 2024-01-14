from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":yum:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")

#Load assets
lottie_coding = load_lottieurl("https://lottie.host/670b7831-f663-4752-8dda-40eed5e5f4d7/uiFtMRTeWy.json")
img_contact_form = Image.open("images/BlueberryCheesecake.png")
img_contact_form_2 = Image.open("images/lecheflan.png")

#Header

with st.container():
    st.subheader("Hi, I'm Gwen. :wave:")
    st.title("A baker from the Philippines.")
    st.write("I am passionate about baking different types of pastries and learning about new recipes.")
    st.write("[Learn more >](https://www.facebook.com/gwensbakeshop/)")

#What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do:")
        st.write("##")
        st.write("""
        As a baker, it is my passion to invent unique tastes suited for everyone. Here are some of my specialties.
        - Blueberry Cheesecake
        - Cookies
        - Eclairs
        - Macaroons
        - Cream Puffs
        - Birthday Cakes
        """)
        st.write("[Youtube Channel >](https://www.facebook.com/gwensbakeshop/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

 #Project Section
    with st.container():
        st.write("---")
        st.header("Baking Using My Recipes")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.subheader("Blueberry Cheesecake")
            st.write("""

               Learn how to make one of my most famous recipes! 
               Tutorials make everything clear, especially for beginners. 
               In this tutorial, I'll show you exactly how to do it.
               Don't worry, it's both easy and fun!
               """
                     )
            st.markdown("[Watch Video...](https://youtu.be/fBMB_D_jSls?si=42acSbVzaJpQnjaz)")

        with st.container():
            st.write("##")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_contact_form_2)
            with text_column:
                st.subheader("Leche Flan")
                st.write("""
                Another one of my recipes that originated from my home country, the Philippines.
                Learn how to make this sweet treat by just following very simple steps.
                This tutorial is beginner-friendly and will make you a leche flan lover in no time!
               """
                     )
            st.markdown("[Watch Video...](https://youtu.be/o-nkEqHpfF0?si=vgRvS64dDE_9e8w5)")

#Contact form
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action = "https://formsubmit.co/gonzalesgwyneth17@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type ="text" name ="name" placeholder="Your Name" required>
        <input type ="email" name ="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type ="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()




