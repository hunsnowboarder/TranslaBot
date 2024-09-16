"""This is a module containing the chat engine related module"""

import os
from typing import List

from dotenv import load_dotenv
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


# decorator function
def _load_from_env(func):
    def wrapper(self) -> None:
        load_dotenv()
        func(self)

    return wrapper


class ChatEngine:
    """Module that deals with the connection to the LLM model and creation of
    the answers. This entails initiating and running of LLM chains, prompts
    and parsing results.
    """

    def __init__(self):
        self.user_prompt: str = None
        self.message_history: List[dict[str, str]] = None
        self.language: str = None
        self.api_key: str = None
        self.model: str = None
        self.model_temperature: int = None
        self.model_system_template: SystemMessagePromptTemplate = None
        self.chat_prompt: ChatPromptTemplate = None
        self.llm_model: ChatOpenAI = None

    @_load_from_env
    def get_openai_key(self) -> None:
        """Function that loads OpenAi API key in the ChatEngine module
        from the environments configuration file."""
        self.api_key = os.getenv("OPENAI_API_KEY")

    @_load_from_env
    def get_model_parameters(self) -> None:
        """Function that loads model parameters in the ChatEngine module
        from the environment configuration file."""
        self.model = os.getenv("LLM_MODEL")
        self.model_temperature = os.getenv("MODEL_TEMPERATURE")
        self.model_system_template = os.getenv("SYSTEM_PROMPT")

    def initialize_model(self) -> None:
        """Function that instantiates chat model"""

        self.llm_model = ChatOpenAI(
            model=self.model,
            temperature=self.model_temperature,
            max_tokens=None,
            max_retries=2,
            api_key=self.api_key,
        )

    def create_llm_prompt(self, user_prompt: str, language: str) -> None:
        """Function that creates the system and human prompt for the LLM, using
        the human message and the selected language as inputs.

        Args:
            user_prompt (str): the text that needs to be translated; coming
            from the streamlit webapp input field.
            language (str): the destination language (to be translated to);
            coming from the streamlit webapp selection box
        """
        system_message_prompt: SystemMessagePromptTemplate = (
            SystemMessagePromptTemplate.from_template(
                self.model_system_template
            )
        )

        human_template: str = f"""{user_prompt} Translate it to: {language}. Do not
        forget to NOT TRANSLATE text inside the square brackets!"""
        human_message_prompt = HumanMessagePromptTemplate.from_template(
            human_template
        )

        self.chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

    def get_answer(self) -> str:
        """Function that builds the LLM chain and and based on the prompt
        streams back the translation.

        Returns:
            str: streaming text of the translation
        """
        chain = self.chat_prompt | self.llm_model | StrOutputParser()

        return chain.stream({"User": self.chat_prompt})

    def run_engine(self, user_prompt: str, language: str) -> str:
        """Main function that contains all the functions that need to be run
        in order for the application to work. It gets the user prompt and selected
        language as inputs and provides the streaming string of the translation.

        Args:
            user_prompt (str): the text that needs to be translated; coming
            from the streamlit webapp input field.
            language (str): the destination language (to be translated to);
            coming from the streamlit webapp selection box

        Returns:
            str: streaming text of the translation
        """
        self.get_openai_key()
        self.get_model_parameters()
        self.initialize_model()
        self.create_llm_prompt(user_prompt, language)
        ai_answer = self.get_answer()
        return ai_answer
