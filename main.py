import sys
from stats import get_num_words, get_num_characters, sort_on, sort_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
       file_path = sys.argv[1] 

#    file_path = "./books/frankenstein.txt"
    text = get_book_text(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path} ...")
    print("----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")
    char_list = get_num_characters(text)
    sorted_char_list = sort_characters(char_list)
    for char in sorted_char_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
main()