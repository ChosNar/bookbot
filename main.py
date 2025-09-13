def main():
    txt = get_book_text("books/frankenstein.txt")
#originally had txt_size under text_count function but the assignment required it to be a string 
    word_num = text_count(txt)
    print(f"{word_num} words found in the document")
def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
def text_count(txt):
    words = txt.split()
    return len(words)
main()
# Boots recommended adding a guard for main function
#if __name__ == "__main__": main()