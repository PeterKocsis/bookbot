from stats import get_character_count, get_word_count, sort_character_by_count

def get_book_text(path_to_file):
    """
    Reads a book file and returns its content as a string.
    
    :param path_to_file: Path to the book file.
    :return: Content of the book as a string.
    """
    
    # Open the file in read mode with UTF-8 encoding
    with open(path_to_file, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def word_count_report(number_of_words):
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")

def character_stat_report(character_stats):
    print("--------- Character Count -------")
    for item_set in character_stats:
        if item_set["char"].isalpha():
            print(f"{item_set["char"]}: {item_set["count"]}")

def make_report(number_of_words, character_stats):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    word_count_report(number_of_words)
    character_stat_report(character_stats)
    print("============= END ===============")

        

def main():
    """
    Main function to execute the script.
    """
    # Path to the book file
    path_to_file = './books/frankenstein.txt'
    
    # Get the book text
    try:
        book_text = get_book_text(path_to_file)
        number_of_words = get_word_count(book_text)
        character_stats = sort_character_by_count(get_character_count(book_text), descending=True)
        make_report(number_of_words, character_stats)

    except FileNotFoundError:
        print(f"Error: The file {path_to_file} was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
if __name__ == "__main__":
    main()
    
