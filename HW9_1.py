def popular_words(text, words):
    text = text.lower()
    text_words = text.split()
    
    result = {}
    for w in words:
        result[w] = text_words.count(w)
    
    return result
