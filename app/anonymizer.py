import re
from typing import Tuple, Dict

try:
    import spacy
    nlp = spacy.load('en_core_web_sm')
except Exception:
    nlp = None

_TOKEN_PREFIX = {
    'NAME': 'NAME_',
    'ADDRESS': 'ADDRESS_',
    'POLICY': 'POLICY_NUMBER_',
    'CLAIM': 'CLAIM_NUMBER_',
    'PHONE': 'PHONE_NUMBER_',
    'SSN': 'SSN_',
}

class Anonymizer:
    def __init__(self):
        self._counter = 0
        self._map: Dict[str, str] = {}

    def _token(self, prefix: str) -> str:
        self._counter += 1
        return f"[{prefix}{self._counter}]"

    def anonymize_text(self, text: str) -> Tuple[str, Dict[str, str]]:
        """Return anonymized text and mapping."""
        mapping = {}
        # Simple regex patterns for numbers and SSN/phone
        patterns = {
            'POLICY': r'\bPOLICY\s*#?\s*(\d{4,})\b',
            'CLAIM': r'\bCLAIM\s*#?\s*(\d{4,})\b',
            'PHONE': r'(\+?1?[ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4})',
            'SSN': r'\b\d{3}-\d{2}-\d{4}\b',
        }
        for key, pattern in patterns.items():
            def repl(m):
                token = self._token(_TOKEN_PREFIX[key])
                mapping[token] = m.group(0)
                return token
            text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
        if nlp:
            doc = nlp(text)
            for ent in doc.ents:
                if ent.label_ in {'PERSON', 'GPE', 'ORG'}:
                    token = self._token(_TOKEN_PREFIX['NAME'])
                    mapping[token] = ent.text
                    text = text.replace(ent.text, token)
        self._map.update(mapping)
        return text, mapping

    def rehydrate_text(self, text: str, mapping: Dict[str, str]) -> str:
        for token, original in mapping.items():
            text = text.replace(token, original)
        return text
