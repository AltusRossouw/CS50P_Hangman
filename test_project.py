import pytest

from project import word_formatting
from project import hangman_img_file

def test_word_formatting():

    assert word_formatting("Hello") == "_ _ _ _ _ "
    assert word_formatting("Jakkal") == "_ _ _ _ _ _ "


def test_hangman_img_file():

    assert hangman_img_file(1) == """
                    +---+
                    |   |
                    O   |
                   /|\  |
                   /    |
                        |
                    ========="""
    
    assert hangman_img_file(5) == """
                    +---+
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                    ========="""



def test_function_n():
    ...

