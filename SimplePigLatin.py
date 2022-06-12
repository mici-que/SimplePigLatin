def main(sentence=None):
    def validator(sentence=None):
        return "sentence" in vars() and isinstance(sentence, str)

    if validator(sentence):
        return True
    return False
