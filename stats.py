from typing import TypedDict

def get_word_count(booktext: str) -> int:
    words = booktext.split()
    return len(words)


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def get_letter_count(booktext: str) -> dict[str, int]:
    letters: dict[str, int] = {}

    for letter in booktext:
        letter = letter.lower()
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    return letters


class Letter_Dict(TypedDict):
    char: str
    num: int


def sort_on(items: Letter_Dict) -> int:
    return items["num"]


def get_sorted_letter_dict(letters: dict[str, int]) -> list[Letter_Dict]:

    sorted_letters: list[Letter_Dict] = []
    for letter in letters:
        letter_dict: Letter_Dict = {
            "char": letter,
            "num": letters[letter]
        }
        sorted_letters.append(letter_dict)
    
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters