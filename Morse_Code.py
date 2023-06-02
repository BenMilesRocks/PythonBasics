#
# Program to translate a string into Morse Code
#
morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def morse_to_eng(string):
    key_list = list(morse.keys())  # Makes a list of keys, so we can search by their index
    val_list = list(morse.values())  # Makes the dictionary searchable by the index of the values
    out = ""
    lst = []
    temp = ""
    pos = 0
    for i in string:  # compiles the morse code into individual words
        pos += 1
        if pos == len(string):
            temp += i
            lst.append(temp)
        if i == "." or "-":
            temp += i
        if i == "/":
            lst.append(i)
        if i.isspace():
            lst.append(temp.rstrip())
            temp = ""
    for item in lst:  # now translate the words in lst, using the index of the values against the keys
        if item == "/":
            out += " "
        else:
            ind = val_list.index(item)
            out += key_list[ind]
    return out


def eng_to_morse(string):
    out = ""
    for i in string:
        if i.isalnum():
            out += morse[i.upper()] + " "
        if i.isspace():
            out += "/ "
        else:
            pass
    return out


print("Welcome to the Morse Code Translator")
while True:
    print("""Please make a selection:
1) English to Morse Code
2) Morse Code to English
3) End program
""")
    y = input(">")
    if y == "1":
        print(eng_to_morse(input("Input phrase for translation: ")))
    if y == "2":
        try:
            print(morse_to_eng(input("Input morse code: ")))
        except ValueError:
            print("""Morse code not recognized. Please make sure:
- You only input '.' or '-' for dots and dashes.
- Make sure to leave a space ' ' between each word
- Separate each word with a '/' slash (make sure you leave a space either side of it too!)""")
    if y == "3":
        print("""Thank you for using the Morse Code Translator
        
Goodbye!""")
        break
    else:
        print("Please input either 1, 2 or 3")
