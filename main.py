from collections import Counter 

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = count_characters(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n" )

    for char, count in character_counts:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

def sort_characters_by_count(chars):
    chars_list = [{'character': char, 'count': count} for char, count in chars.items()]
    chars_list.sort(key=lambda x: x['count'], reverse=True)
    return chars_list

def count_characters(text):
    counts = Counter(c.lower() for c in text if c.isalpha())
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()