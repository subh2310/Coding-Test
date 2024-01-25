#Challenge 1

In this problem, you will be given one or more integers in English. Your task is to translate these numbers into their integer representation. The numbers can range from negative 999,999,999 to positive 999,999,999. The following is an exhaustive list of English words that your program must account for:

negative, zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, thousand, million


INPUT AND OUTPUT


Notes on input:

•	Negative numbers will be preceded by the word negative.
•	The word “hundred” is not used when “thousand” could be. For example, 1500 is written “one thousand five hundred”, not “fifteen hundred”.


SAMPLE INPUT

six, negative seven hundred twenty nine, one million one hundred one
 

SAMPLE OUTPUT

6, -729, 1000101
________________________________________________
Code:


numbers = {
    "negative": -1,
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred":
 
100,
    "thousand": 1000,
    "million": 1000000,
}

def english_to_integer(text):
    words = text.lower().split()
    is_negative = False
    value = 0

    if words[0] == "negative":
        is_negative = True
        words = words[1:]

    for i, word in enumerate(words):
        if word in numbers:
            if word == "hundred":
                value *= numbers[word] 
            elif word == "thousand":
                value *= numbers[word]
            elif word == "million":
                value *= numbers[word]
            else:
                if i + 1 < len(words) and words[i + 1] in ["hundred", "thousand", "million"]:
                    next_word_value = value + numbers[word]
                    if next_word_value <= 999999999:
                        value = next_word_value
                        continue
                value += numbers[word]
        else:
            raise ValueError(f"Invalid word: {word}")

    return -value if is_negative else value

# Sample input and output
text = "six, negative seven hundred twenty nine, one million one hundred one"
integers = [english_to_integer(t) for t in text.split(",")]
print(", ".join(str(i) for i in integers))