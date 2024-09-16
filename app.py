""" This module contains the application file which is the entry point of the applicaton"""

# importing packages
import time
from typing import List

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

from custom_modules.chatengine import ChatEngine
from custom_modules.frontend_modules import (
    create_list_of_languages_from_dict,
    get_language_alias,
    get_languages_dictionary,
)
from custom_modules.metrics import EXEC_TIME

# inintializing available languages
LANGUAGES_PATH: str = "languages.json"

st.set_page_config(
    page_title="BrokerChooser Translation Chatbot", page_icon="🤖"
)

languages_dict: dict = get_languages_dictionary(path_to_json=LANGUAGES_PATH)

languages_list: List[str] = create_list_of_languages_from_dict(
    languages_dict=languages_dict
)


selected_language: str = st.selectbox("Select a language:", languages_list)
language_alias = get_language_alias(
    selected_language=selected_language, languages_dict=languages_dict
)

textbox_default_text: str = (
    f"What will we be translating from English to {selected_language} today?"
)

st.title("Let's translate 😎")

# setting up messages in the streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# setting up messages in the streamlit session states
for message in st.session_state.messages:
    with st.chat_message(message.type):
        st.markdown(message.content)

# appending user message to the session state
if prompt := st.chat_input(textbox_default_text):
    user_message: HumanMessage = HumanMessage(prompt)
    st.session_state.messages.append(user_message)

    # displaying user message in the webapp
    with st.chat_message(user_message.type):
        st.markdown(user_message.content)

    # initializing chatmodel
    chat_model: ChatEngine = ChatEngine()

    # starting time measuring
    start_time = time.time()

    # streaming chatmodel answer
    with st.chat_message("ai"):
        ai_translation = st.write_stream(
            chat_model.run_engine(
                user_prompt=user_message.content, language=selected_language
            )
        )

    # appending ai message to streamlit session state
    ai_message: AIMessage = AIMessage(ai_translation)
    st.session_state.messages.append(ai_message)

    # stopping time counter and sendig resulst for latency logging
    exec_time = time.time() - start_time
    EXEC_TIME.labels("page_execution").observe(exec_time)
