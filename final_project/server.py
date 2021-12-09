#!/usr/bin/env python3

"""
Server module
"""

import json
from machinetranslation import translator
from flask import Flask, render_template, request

APP = Flask( "Web Translator" )

@APP.route( "/englishToFrench" )
def english_to_french():
    """
    End point implementation: en -> fr
    """
    text_to_translate = request.args.get( 'textToTranslate' )
    return translator.english_to_french( text_to_translate )

@APP.route( "/frenchToEnglish" )
def french_to_english():
    """
    End point implementation: fr -> en
    """
    text_to_translate = request.args.get( 'textToTranslate' )
    return translator.french_to_english( text_to_translate )

@APP.route( "/" )
def render_index_page():
    """
    End point implementation: index
    """
    return render_template( "index.html" )

if __name__ == "__main__":
    APP.run( debug = True, host = "0.0.0.0", port = 8080 )