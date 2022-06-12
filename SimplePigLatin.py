letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
addchars = "ay"


class PiggerClass:
    piggedString = ""
    clipboard = ""
    fullclipboard = False

    # append clipboard to newString
    def drop(self, character):
        self.piggedString = self.piggedString + self.clipboard + character
        self.fullclipboard = False

    # cut current character and add addchars, store in clipboard
    def cut(self, character):
        self.clipboard = character + addchars
        self.fullclipboard = True

    # add current character to newString
    def go(self, character):
        self.piggedString = self.piggedString + character

    # call when end of string reached, if there is still something on the clipboard, paste it
    def finish(self):
        if self.fullclipboard:
            self.drop("")

    # decide what to do with current character
    def pig(self, character):
        if self.fullclipboard:
            # we already have a character on the clipboard and this is a letter, so go on
            if character in letters:
                self.go(character)
            # this is not a letter, drop clipboard content
            else:
                self.drop(character)
        # clipboard is empty
        else:
            # this is a letter, cut it
            if character in letters:
                self.cut(character)
            # this is not a letter, go on
            else:
                self.go(character)


def main(sentence=None):
    def validator(sentence=None):
        return "sentence" in vars() and isinstance(sentence, str)

    if validator(sentence):
        Pigger = PiggerClass()
        for character in sentence:
            Pigger.pig(character)
        Pigger.finish()
        return Pigger.piggedString
    return False
