def main(sentence=None):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def validator(sentence=None):
        return "sentence" in vars() and isinstance(sentence, str)

    if validator(sentence):
        newString = ""
        carrying = False
        for character in sentence:
            if character in letters:
                if carrying == False:
                    carry = character
                    carrying = True
                else:
                    newString = newString + character
            else:
                if carrying == False:
                    newString = newString + character
                else:
                    newString = newString + carry + "ay" + character
                    carrying = False
        if carrying:
            newString = newString + carry + "ay"
        return newString
    return False
