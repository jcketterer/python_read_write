def get_letter(ltr):
    morse_lookup = {
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
        ", ": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
        "\n": "\n",
    }
    return morse_lookup.get(ltr.upper(), "")


def get_morse_code(phrase):
    return " ".join([get_letter(char) for char in phrase])


def morse_to_letter(code):
    CODE_reversed = {
        "..-.": "F",
        "-..-": "X",
        ".--.": "P",
        "-": "T",
        "..---": "2",
        "....-": "4",
        "-----": "0",
        "--...": "7",
        "...-": "V",
        "-.-.": "C",
        ".": "E",
        ".---": "J",
        "---": "O",
        "-.-": "K",
        "----.": "9",
        "..": "I",
        ".-..": "L",
        ".....": "5",
        "...--": "3",
        "-.--": "Y",
        "-....": "6",
        ".--": "W",
        "....": "H",
        "-.": "N",
        ".-.": "R",
        "-...": "B",
        "---..": "8",
        "--..": "Z",
        "-..": "D",
        "--.-": "Q",
        "--.": "G",
        "--": "M",
        "..-": "U",
        ".-": "A",
        "...": "S",
        ".----": "1",
    }
    return CODE_reversed.get(code, "")


def get_english(phrase):
    letters = phrase.split(" ")
    return "".join([morse_to_letter(letter) for letter in letters])


input_file = open("morse.txt", "r")
output_file = open("translated.txt", "w")
for line in input_file:
    output_file.write(get_english(line))

input_file.close()
output_file.close()

# file.seek(0)
# all_text = file.read()
# file.close()

# file = open("demo.txt", "w")

# file.write("I AM A DEMO FILE!")

# file.close()
