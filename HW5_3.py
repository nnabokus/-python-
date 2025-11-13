import string

text = input("Введіть ваш текст:")

for symbol in string.punctuation:
    text = text.replace(symbol, "")

words = text.split()
words = [w.capitalize() for w in words]

hashtag = "#" + "".join(words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print("Результат:", hashtag)
