# -*- coding: utf-8 -*-

def detect_language(text, languages):
    """Returns the detected language of given text."""
    words = text.split()
    detectedlang = ''
    most_matches = 0
    for lang in languages: 
        matches = [word for word in words if word.lower() in lang['common_words']]
        if len(matches) > most_matches:
            detectedlang = lang['name']
            most_matches = len(matches)
    return detectedlang
        
