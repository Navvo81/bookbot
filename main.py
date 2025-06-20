from stats import number_of_words, char_count, sort_dict
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_loc = sys.argv[1]
    book_text = get_book_text(book_loc)
    word_count = number_of_words(book_text)
    characters = char_count(book_text)
    chars_sorted = sort_dict(characters)
    print_report(book_loc,word_count, chars_sorted)

def print_report(book_loc, word_count, chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_loc}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for i in chars_sorted:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")

main()