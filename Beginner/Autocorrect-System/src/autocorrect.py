
import re
from spellchecker import SpellChecker


class AutocorrectSystem:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_word(self, word):
        if not word or not word.strip():
            return word

        match = re.fullmatch(r"([^A-Za-z]*)([A-Za-z]+)([^A-Za-z]*)", word)

        if not match:
            return word

        prefix, core, suffix = match.groups()
        corrected = self.spell.correction(core.lower())

        if corrected is None:
            return word

        if core.isupper():
            corrected = corrected.upper()
        elif core.istitle():
            corrected = corrected.capitalize()

        return prefix + corrected + suffix

    def correct_text(self, text):
        if not text:
            return text

        return re.sub(
            r"\b[A-Za-z]+\b",
            lambda match: self.correct_word(match.group()),
            text
        )

    def suggest_corrections(self, word, limit=5):
        if not word or not word.strip():
            return []

        candidates = self.spell.candidates(word.lower()) or set()
        return sorted(candidates)[:limit]
