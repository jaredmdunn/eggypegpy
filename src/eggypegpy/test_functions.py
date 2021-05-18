from eggypegpy.functions import translate_word


def test_translate_word():
    assert translate_word("Hello") == "Heggelleggo"
    assert translate_word("Great") == "Greggeat"
    assert translate_word("eel") == "eggeel"
    assert translate_word("yellow") == "yeggelleggow"
    assert translate_word("a") == "egga"
    assert translate_word("I") == "Eggi"
