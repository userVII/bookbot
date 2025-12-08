from stats import number_of_words

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    text_word_count = number_of_words(text)
    print(text_word_count)
    
main()