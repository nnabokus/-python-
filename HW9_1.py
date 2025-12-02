def popular_words(text, words):
    text = text.lower()                # робимо текст нижнього регістру
    text_words = text.split()          # розбиваємо на слова
    
    result = {}
    for w in words:
        result[w] = text_words.count(w)  # рахуємо кількість входжень
    
    return result
