__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


from ..settings import EN
from .common import SpellChecker


class EnglishSpellCheckerSingleton(SpellChecker):
    """
    Utility class to manage a single SpellChecker instance for english.
    """

    __instance = None

    @staticmethod
    def get_instance():
        """
        Static access method for singleton pattern.
        :return: EnglishSpellCheckerSingleton
        """
        if EnglishSpellCheckerSingleton.__instance is None:
            EnglishSpellCheckerSingleton.__instance = EnglishSpellCheckerSingleton(
                language=EN["PYSPELL_LANGUAGE"], allowed_punctuation_marks=EN["ALLOWED_PUNCTUATION_MARKS"]
            )
        return EnglishSpellCheckerSingleton.__instance


def fix_spelling(text):
    """
    Tries to correct the spelling of the given text.
    :param text: the text to spell-checked
    :type: str
    :return: spell-checked text
    :type: str
    """
    return EnglishSpellCheckerSingleton.get_instance().fix_text(text)
