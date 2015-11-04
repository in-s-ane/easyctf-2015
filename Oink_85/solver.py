# Taken from an old Intro 2 HW

def isVowel(char):
    return char in "AEIOUaeiou"

def isPunc(char):
    # str is just a placeholder for an actual string
    return not str.isalpha(char) and char is not ";"

def isHyphen(char): # is there a hypen in the word?
    return (char.find('-') != -1 )

def hypenchar(word): # Seperates the hyphenated word into two words
    first = word[:word.find('-')]
    second = word[word.find('-')+1:]
    return pigLatinWord(first) + "-" + pigLatinWord(second) # Pig Latin with '-'

#---Main function---#

def pigLatinWord(word):
    new_word = ""
    addToEnd = ""
    addToStart = ""

    if isPunc(word[0]): # Beginning punctuation
        index = 0
        while index < len(word) and isPunc(word[index]):
            index += 1
        addToStart = word[:index]
        word = word[index:]

    if isPunc(word[-1]): # Ending punctuation
        index = len(word)-1
        while index >= 0 and isPunc(word[index]):
            index-=1
        addToEnd = word[index+1:]
        word = word[:index+1]

    if isHyphen(word): # If there is a hyphen
        new_word = hypenchar(word)

    # It is a vowel
    elif isVowel(word[0]):
        new_word = word + "yay"
        # It is a consonant
    else:
        index = 1
        new_word = word[index:] + word[:index] + "ay"

    return addToStart + new_word + addToEnd

def translate(phrase):
    newPhrase = ""
    phrase = phrase.split(" ")
    for word in phrase:
        newPhrase += pigLatinWord(word) + " "
    return newPhrase.strip()

f = open("piglatin1.in", "r").read()
f = open("piglatin1.out", "w").write("%s\n" % (translate(f)))

# easyctf{atinl4y_easyyay_3noughyay_orfay_ayay_1gpay!}
