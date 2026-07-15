# Write your code here.

#Task 1
def greet():
    return "Hello!"
print(greet())

#Task 2
def personalized_greeting(name):
    return f"Hello, {name}!"
print(personalized_greeting("Alice"))

#Task 3
def calc(num1, num2, operation="multiply"):
    try:
        if operation =="add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            return num1 / num2
        elif operation == "modulo":
            return num1 % num2
        elif operation == "int_divide":
            return num1 // num2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
#Task 4 
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        elif data_type == "bool":
            return bool(value)
    except ValueError:
        return "Invalid value for conversion"
#Task 5 
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except(TypeError, ZeroDivisionError):
        return "Invalid input for grade calculation"


#Task 6
def repeat_string(string, times):
    result = ""
    for _ in range(times):
        result += string
    return result

#Task 7
def student_scores(mode, **kwargs):
    if mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif mode == "best":
        highest_score = -1
        best_student = None
        for student, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = student
        return best_student
#Task 8
def titleize(title):
    words = title.split()
    little_words = ["and", "or", "the", "a", "an", "in", "on", "at", "to", "for", "with"]
    last_index=len(words) - 1
    for i in range(len(words)):
        if i == 0 or i == last_index or words[i].lower() not in little_words:
            words[i] = words[i].capitalize()
        else:
            words[i] = words[i].lower()
    return " ".join(words)

#Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
#Task 10    
def translate_word(word):
    vowels = "aeiou"
    if word[0] in vowels:
        return word + "ay"
    elif word.startswith("qu"):
        return word[2:] + "quay"
    else:
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"  # Fallback if there are no vowels at all

def pig_latin(sentence):
    words = sentence.split()
    translated = []
    for word in words:
        translated.append(translate_word(word))
    return " ".join(translated)