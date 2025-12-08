def number_of_words(book_text):
    word_count = 0
    for word in book_text.split():
        word_count += 1
    return f"Found {word_count} total words"