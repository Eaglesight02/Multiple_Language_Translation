import streamlit as st
import Translation
import Authentication
import Languages
import time

st.title("Translation App")

# Getting the API KEY:
api_key = st.text_input("API KEY: ", type = 'password' , key = 'password')

if st.button("Enter"):
    if api_key and Authentication.check_key(api_key):
        st.success("You have successfully entered the API Key")
    else:
        st.warning("Entered wrong key!")

# Language selection
Languages.source_lang = st.selectbox("Select source language", ("English", "Spanish", "French", "German", "Hindi"))
Languages.dest_lang = st.selectbox("Select target language", ("English", "Spanish", "French", "German", "Hindi"))


# Creating messages list if not already present in session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Printing all the messages with the role and the content
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Taking input from the user with the 'chat_input' function; ':=' is used to assign the value when its not NULL
if prompt := st.chat_input("Enter your text to be translated", max_chars = 500):

    st.chat_message("user").markdown(prompt)                                        # Showing the chat message with the role as user and content as the prompt
    st.session_state.messages.append({"role":"user","content":prompt})              # Saving user's prompt to session_state

    value,response = Translation.collect_messages(prompt)                           # Getting the response using the 'Translation.collect_messages()' function with the user's prompt as input
    
    if(value == False):
        st.warning("Rate Limit Exceeded! Try after some time.")
        time.sleep(10)

    with st.chat_message("assistant"):                                              # Showing the assistant's response with the role as assistant and content as response.
        st.markdown(response)

    st.session_state.messages.append({"role":"assistant","content":response})       # Appending the role and content of the assistant.


# Legacy code for text input boxes

# # Text input
# text = st.text_area("Enter text to translate")

# # print(Languages.source_lang)
# # print(Languages.dest_lang)
# # print("\n")


# # Translate button
# if st.button("Translate"):
#     if text:
#         st.success(f"Original text ({Languages.source_lang}): {text}")
#         st.success(f"Translated text ({Languages.dest_lang}): {Translation.collect_messages(text)}")
#     else:
#         st.warning("Please enter some text to translate.")