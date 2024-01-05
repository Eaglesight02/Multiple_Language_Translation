import os

os.system('pip3 install -r requirements.txt')
os.system('python3 languages.py')
os.system('python3 translation.py')
os.system('streamlit run streamlit_app.py')