import html
import re
from unicodedata import normalize

def clean_text(text):
    text = html.unescape(text)
    text = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", 
                    r"\1", 
                    normalize("NFD", text), 
                    0, 
                    re.I)
    
    text = normalize('NFC', text)
    text = re.sub('[^a-zA-ZñÑ]+', ' ', text)
    text = text.lower()
    return text