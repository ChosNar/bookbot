import sys
from stats import text_count,char_count, sorter
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    loct= sys.argv[1]
    txt = get_book_text(loct)
#originally had txt_size under text_count function but the assignment required it to be a string 
    word_num = text_count(txt)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {loct}')
    print('----------- Word Count ----------')
    print(f'Found {word_num} total words')
    print('----------- Character Count -----------')
    for items in sorter(char_count(txt)):
        if items['char'].isalpha():
            print(f"{items['char']}: {items['num']}")
    print('============= END ===============')

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

main()
# Boots recommended adding a guard for main function
#if __name__ == "__main__": main()