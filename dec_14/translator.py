from typing import List
import requests

base_url = 'https://libretranslate.de/'

def detect_language(text: str) -> str:
    response = requests.post(base_url+"/detect", json={'q': text})

    if response.ok:
        py_response = response.json()
        # TODO sort by highest confidence then get value
        return py_response[0].get('language', 'en')
    else:
        raise ConnectionError(
            f"There was a problem attempting to detect the language of your text. Response: {response.text}")


def get_supported_languages(language: str) -> List[str]:
    response = requests.get(base_url+"/languages")

    if response.ok:
        py_response = response.json()

        def filter_match(info):
            return language.casefold() in (
                info['code'].casefold(),
                info['name'].casefold())

        # Lambda version ->. lambda info: language.casefold() in (info['code'].casefold(), info['name'].casefold())

        supported_lang_infos = list(filter(filter_match, py_response))

        if not supported_lang_infos:
            raise ValueError(f"The language {language} is not supported.")
        else:
            supported_lang_info = supported_lang_infos[0]

        return supported_lang_info['targets']

    else:
        raise ConnectionError(
            f"There was a problem attempting to get the supported languages. Response: {response.text}")


def translate(text: str, from_lang:str, to_lang: str) -> str:
    response = requests.post(base_url+"/translate", json={'q': text, 'source': from_lang, 'target': to_lang})

    if response.ok:
        py_response = response.json()
        return py_response["translatedText"]
    else:
        raise ConnectionError(
            f"There was a problem attempting to translate your text. Response: {response.text}")



while True:
    text = input("Enter text to translate: ")
    detected_lang = detect_language(text)
    options = get_supported_languages(detected_lang)
    target = input(f"Enter the language to translate to.({', '.join(options)})\n")
    translation = translate(text, detected_lang, target)
    print(f"Translated text: \"{translation}\"")

    ui = input("Do you want to continue? (y/n)")
    if ui.lower() == 'n':
        break