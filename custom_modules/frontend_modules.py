"""Module containing the functions called by the frontend"""

import json
from typing import List


def get_languages_dictionary(path_to_json: str) -> dict:
    """Gets the path to languages json file and returns a dictionary.

    Args:
        path_to_json (str): path to the json file

    Returns:
        dict: dictionary containing the languanges and their aliases
    """
    with open(path_to_json, "r", encoding="utf-8-sig") as file:
        languages_dict: dict = json.load(file)
    return languages_dict


def create_list_of_languages_from_dict(languages_dict: dict) -> List[str]:
    """Gets the languages dictionary and returns the list of languages.

    Args:
        languages_dict (dict): dictionary containing the languanges and their
        aliases

    Returns:
        List[str]: list of languages
    """

    all_languages: List = languages_dict.keys()
    return all_languages


def get_language_alias(selected_language: str, languages_dict: dict) -> str:
    """Gets the selected language and returns its alias.

    Args:
        selected_value (str): selected language

    Returns:
        str: alias of the selected language
    """

    language_alias: str = languages_dict[selected_language]
    return language_alias
