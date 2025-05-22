from stats import count_words, count_characters, sort_character_counts
import sys

def get_book_text(book):
    with open(book, 'r' ) as f: 
        file_contents = f.read()
    return file_contents


def main():
    #path_to_book = "/home/eswerdna0/workspace/boot.dev/bookbot/books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    
    path_to_book = sys.argv[1]
    book_content = get_book_text(path_to_book)
    word_count_total = count_words(book_content)
    character_total = count_characters(book_content)
    characters_sorted = sort_character_counts(character_total)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_total} total words")
    print("--------- Character Count -------")

    # Iterate through the sorted list and print each character's count
    for item in characters_sorted:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()