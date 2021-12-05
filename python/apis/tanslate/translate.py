from googletrans import Translator


def transtate(text, dest="en"):
    if text!="":
        try:
            translator = Translator()
            translation = translator.translate(text, dest=dest)
            return translation.text
        except:
            raise ValueError("can't translate")
    else:
        return "Give some text to translate"
