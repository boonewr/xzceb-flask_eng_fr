import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
# from dotenv import load_dotenv

# load_dotenv()

# apikey = os.environ['apikey']
# url = os.environ['url']

apikey = 'RB_cj4U96FN4xVOCEITFsbVRRz_vuvZNE6OFxu4qFE86'
url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/c220277a-7133-413f-819f-26d8e665869d'

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    frenchText = language_translator.translate(
        text = englishText,
        model_id = 'en-fr').get_result()
    return frenchText.get("translations")[0].get("translation")

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
        text = frenchText,
        model_id = 'fr-en').get_result()
    return englishText.get("translations")[0].get("translation")

# print(englishToFrench("Hello, how are you?"))
# print(frenchToEnglish("Aujourd'hui, maman est morte. Ou peut-être hier, je ne sais pas"))
