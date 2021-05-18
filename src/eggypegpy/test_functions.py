from eggypegpy.functions import translate_word, translate_text


def test_translate_word():
    assert translate_word("Hello") == "Heggelleggo"
    assert translate_word("Great") == "Greggeat"
    assert translate_word("eel") == "eggeel"
    assert translate_word("yellow") == "yeggelleggow"
    assert translate_word("a") == "egga"
    assert translate_word("I") == "Eggi"


def test_translate_text():
    assert translate_text("Hello World") == "Heggelleggo Weggorld"
    assert translate_text("Hello, World!") == "Heggelleggo, Weggorld!"
