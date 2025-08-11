# Language Detector
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # Ensure consistent results

def detect_language(text):
    """Detect the language of a given text and return code + name."""
    lang_code = detect(text)
    language_mapping = {
        'es': 'Spanish',
        'en': 'English',
        'sw': 'Swahili',
        'guz': 'Kisii'  # ISO 639-3 code for Ekegusii (Kisii)
    }
    return lang_code, language_mapping.get(lang_code, lang_code)

# Sample texts
texts = [
    '¿Qué te gusta hacer',
    'Nyasae no omuya'
]

# Detect and print results
for text in texts:
    code, name = detect_language(text)
    print(f'This is the {name} language shortened by: {code}')
