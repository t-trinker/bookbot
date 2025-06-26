def get_word_count(filepath: str) -> int:
    booktext = get_book_text(filepath)
    words = booktext.split()
    return len(words)


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
