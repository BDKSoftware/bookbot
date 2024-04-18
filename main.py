
def main():
    bookPath = "books/frankenstein.txt"

    with open(bookPath) as f:
        file_contents = f.read();
        

        # Word Count
        word_count = get_num_words(file_contents)

        # Letter Count
        chars_dict = get_char_dict(file_contents)
        
        #Sorted Dict
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

        # Create Report
        create_report(bookPath, word_count, chars_sorted_list)


        

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(words):
    letters = {}
    for s in words:
        if s in letters:
            if s.isalpha():

                letters[s.lower()] += 1
        else:
            if s.isalpha():
                letters[s.lower()] = 1


    return letters


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




def create_report(bookPath, word_count, chars_sorted_list):
    
    
    #TODO: Need to sort letters as list and return them to a dict after sorting

    print(f"--- Begin report of {bookPath} ---")
    print(f"{word_count} words found in this document")
    print("\n")


    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

    return None
        
        


main()
