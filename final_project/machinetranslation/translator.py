"""
translator.py
A module that will allow EN <-> FR text translations.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Load security information from environment.
load_dotenv()
TRANSLATOR_APIKEY = os.environ['apikey']
TRANSLATOR_URL = os.environ['url']

def create_watson_translator( apikey, url ):
    authenticator = IAMAuthenticator( f'{ apikey }' )
    language_translator = LanguageTranslatorV3(
        version = '2021-10-01',
        authenticator = authenticator
    )

    language_translator.set_service_url( f'{ url }' )
    return language_translator

TRANSLATOR = create_watson_translator( TRANSLATOR_APIKEY, TRANSLATOR_URL )

# originally englishToFrench( englishText ) but pylint wants it snake_case
def english_to_french( english_text ): 
    french_text = ""
    if english_text is not None:
        translation = TRANSLATOR.translate(
            text = f'{ english_text }',
            model_id = 'en-fr'
            ).get_result()
        if translation is not None \
            and 'translations' in translation \
            and len( translation[ 'translations' ] ) > 0:
            french_text = translation[ 'translations' ][0][ 'translation' ]
    return french_text

# originally frenchToEnglish( frenchText ) but pylint wants it snake_case
def french_to_english( french_text ):
    english_text = ""
    if french_text is not None:
        translation = TRANSLATOR.translate(
            text = f'{ french_text }',
            model_id = 'fr-en'
            ).get_result()
        if translation is not None \
            and 'translations' in translation \
            and len( translation[ 'translations' ] ) > 0:
            english_text = translation[ 'translations' ][0][ 'translation' ]
    return english_text

def main():
    print( english_to_french( "Hello World!" ) )
    print( french_to_english( "Bonjour le monde!" ) )
if __name__ == "__main__":
    main()
    