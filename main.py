import sys
from stats import get_num_words, count_characters, get_character_report


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    # check if we have the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # use the command-line argument as the book path
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    char_counts = count_characters(book_text)
    char_report = get_character_report(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_report:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['count']}")

    print("============= END ===============")


main()
