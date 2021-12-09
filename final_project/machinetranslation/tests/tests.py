#!/usr/bin/env python3

"""
Test case for translator.py module from machinetranslation package.
"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslator( unittest.TestCase ):
    """
    Test suite for translator.py
    """
    def test_e2f( self ):
        """
        Test case for English to French translation.
        """
        testcase = english_to_french( "Hello" )
        expected = "Bonjour"
        # Null input test should return empty translation
        self.assertEqual( english_to_french( None ), "" )
        self.assertGreater( len( testcase ), 0 )
        self.assertNotEqual( testcase, "" )
        self.assertEqual( testcase, expected )

    def test_f2e( self ):
        """
        Test casde for French to English translation.
        """
        testcase = french_to_english( "Bonjour" )
        expected = "Hello"
        # Null input test should return empty translation
        self.assertEqual( french_to_english( None ), "" )
        self.assertGreater( len( testcase ), 0 )
        self.assertNotEqual( testcase, "" )
        self.assertEqual( testcase, expected )

if __name__ == "__main__":
    unittest.main()