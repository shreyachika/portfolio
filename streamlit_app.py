import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")

def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
     return None
  return r.json()

lottie_coder = load_lottieurl("https://lottie.host/a057da90-ee52-4c20-9503-3cabc899f5f0/2FKseZVZun.lottie")


st.write("##")
st.subheader("Hey Guys :wave:")
st.title("My Portfolio Website")
st.write("""                    
I am Shreya, a passionate data enthusiast pursuing a Master of Science in Data Science at San Jose State University, set to graduate in December 2024. With a background in Computer Science Engineering and Information Technology, I have delved into data analytics and machine learning.

As a Graduate Research Assistant, I was involved in groundbreaking research at SJSU, focusing on enhancing pre-construction cost estimation for Caltrans through machine learning models. Proficient in Python, R, and MySQL, I excel in data analysis and advanced feature engineering.

My experience at Accenture involved leading data quality assurance for ETL projects using Apache Spark and Talend. Additionally, as a Software Engineer Intern at AppCloud Software Solutions, I utilized data mining techniques and AWS services for insightful data extraction.

My projects extend to developing personalized recommendation systems and implementing machine learning models for early disease detection. Skilled in Python, Java, R, databases, data science libraries, and web development technologies, I am driven by curiosity and a passion for AI's transformative potential.

Eager to contribute to technological innovation, I seek opportunities to collaborate on impactful solutions. Let's connect and explore the possibilities together! 🚀🔍
""")
st.write("[Read More](https://share.streamlit.io/)")  
st.write('---')

with st.container():
  selected = option_menu(
    menu_title = None,
    options = ['About', 'Projects', 'Contact'],
    icons = ['person', 'code-slash', 'chat-left-text-fill'],
    orientation = 'horizontal'
  )
if selected == 'About':

  with st.container():
    col1, col2 = st.columns(2)
    with col1:
      st.write("##")
      st.subheader("I am Shreya Chikatmarla")
      st.title("Grad at SJSU")
    with col2:
      st_lottie(lottie_coder)

