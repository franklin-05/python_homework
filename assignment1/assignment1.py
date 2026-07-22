# Write your code here.

#Task 1
def hello():
    return "Hello!"
print(hello())

#Task 2
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

#Task 3
def calc(num1, num2, operation="multiply"):
    try:
        if operation == "add":
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
        elif operation == "power":
            return num1 ** num2
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
        return f"You can't convert {value} into  a {data_type}."
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
        return "Invalid data was provided."


#Task 6
def repeat(string, times):
    result = ""
    for _ in range(times):
        result += string
    return result

#Task 7
def student_scores(mode, **kwargs):
    if mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif mode == "best":
        highest_score = max(kwargs.values())
        for student, score in kwargs.items():
            if score == highest_score:
                return student
#Task 8
def titleize(title):
    words = title.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    last_index = len(words) - 1
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
    
    for i, letter in enumerate(word):
        if letter in vowels:
            if letter == 'u' and i > 0 and word[i-1] == 'q':
                return word[i+1:] + word[:i+1] + "ay"
            return word[i:] + word[:i] + "ay"
            
    return word + "ay"

def pig_latin(sentence):
    words = sentence.split()
    translated = []
    for word in words:
        translated.append(translate_word(word))
    return " ".join(translated)