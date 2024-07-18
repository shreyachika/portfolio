import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    try:
        return r.json()
    except ValueError:
        return None

lottie_url = "https://lottie.host/17c36458-45d5-47ae-b9fc-9ff9b5cf73b5/IQmu8jcGOf.json"
lottie_data = load_lottieurl(lottie_url)
image = Image.open("Pic.png")

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
 
st.write('---')

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Shreya Chikatmarla")
            st.title("Grad at SJSU")
        with col2:
            if lottie_data is not None:
                st_lottie(lottie_data)
            else:
                st.error("Failed to load Lottie animation.")

    st.write("---")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Education")
            st.write("""
            - San Jose State University, San Jose - Master of Science in Data Science - Grade: 3.5 / 4
            - Jawaharlal Nehru Technological University of Hyderabad - Master of Technology in Computer Science Engineering - Grade: 3.8 / 4
            - Osmania University - Bachelor of Engineering in Information Technology - Grade: 3.9 / 4
            """)
        with col4:
            st.subheader("Experience")
            st.write("""
            - Graduate Research Assistant - August 2023 to Till Date - San Jose, CA
            - QA Engineer - Data Integration - March 2020 - February 2022 - Accenture, India
            - Software Engineer Intern - January 2017 - July 2017 - AppCloud Software Solutions, India
            """)

    with st.container():
        col5, col6 = st.columns(2)
        with col5:
            st.subheader("Skills")
            st.write("""
            Core Skills:
               - Programming: Python, SQL
               - Machine Learning/Deep Learning: PyTorch, TensorFlow, Keras, scikit-learn
               - Data Engineering: pandas, NumPy, Apache Spark, Hadoop
               - Visualization & Deployment: Matplotlib, Seaborn, Plotly, Tableau, Power BI, Streamlit, Flask
            
            Technologies & Tools:
               - Cloud & DevOps: AWS, Azure, Docker, Git
               - Databases: MySQL, PostgreSQL, MongoDB
               - Collaboration & Project Management: JIRA
            """)
        with col6:
            st.subheader("Certifications and Achievements:")
            st.write("""
            - Introduction to Data Analytics (Simplilearn)
            - Machine Learning & Deep Learning in Python & R (Udemy)
            - Web Development Certification (Internshala)
            - Participated in The Programming League on " Coding in CProgramming" held by Computer Society of India.
            """)

elif selected == "Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6, col7, col8 = st.columns(4)
        with col5:
            st.image(image)
        with col6:
            st.subheader("Network-Slicing-Recognition")
            st.markdown("[Visit GitHub Repo](https://github.com/shreyachika/Network-Slicing-Recognition)")
        with col7:
            st.subheader("Heart Disease Prediction")
            st.markdown("[Visit GitHub Repo](https://github.com/shreyachika/Heart-Disease-Prediction)")
        with col8:
            st.subheader("Demographically-Enhanced Movie Recommendation System for Personalized Book Suggestions in Big Data")
            st.markdown("[Visit GitHub Repo](https://github.com/shreyachika/MovieBookRecSys-BigData)")

elif selected == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out to me for collaboration, inquiries, or just to connect!")
    
    with st.container():
        col9, col10, col11 = st.columns(3)
        with col9:
            st.subheader("Email:")
            st.write("cshreya955@gmail.com")
        with col10:
            st.subheader("LinkedIn:")
            st.write("[Connect on LinkedIn](https://www.linkedin.com/in/shreya-chikatmarla-6669b5242/)")
        with col11:
            st.subheader("Resume:")
            st.write("[View My Resume](https://github.com/shreyachika/portfolio/raw/main/Resume.pdf)")
