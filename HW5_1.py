import keyword
import string

name = input()

is_valid = True

if name == "":
    is_valid = False

if is_valid:
    if name[0].isdigit():
        is_valid = False

if is_valid:
    if name in keyword.kwlist:
        is_valid = False

if is_valid:
    for symbol in name:
        if symbol.isupper():
            is_valid = False

        if symbol == " ":
            is_valid = False

        if symbol in string.punctuation and symbol != "_":
            is_valid = False

if is_valid:
    only_underscores = True
    for symbol in name:
        if symbol != "_":
            only_underscores = False

    if only_underscores:
        if len(name) > 1:
            is_valid = False

print(is_valid)
