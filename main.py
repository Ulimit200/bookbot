

def main():
    #file path to book location
    book_location = "books/frankenstein.txt"
    #gets text contents of the book/text
    contents = get_contents(book_location)
    #gets word count and then prints it on next line
    word_count = get_word_count(contents)
    print(f"{word_count} words found in text")
    #gets count of each individual char
    chars_dict = get_character_count(contents)
    #sorts out just the alphabetical characters
    alpha_dict = sort_characters_alpha(chars_dict)
    #sorts the alpha_dict list
    alpha_dict.sort(reverse=True, key=lambda alpha: alpha["num"])
    #formats the list into a nicer view
    formated_alpha = format_output(alpha_dict)

    #all printer statements below were for testing or previous parts of the build but are no
    #longer needed for scoring

    #print(contents)
    #print(chars_dict)
    #print(alpha_dict)
    #print(formated_alpha)
    #print(type(sorted_alpha))
    #print(format_output(sorted_alpha))
    


def get_word_count(text):
    words = text.split()
    return len(words)

def get_contents(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    total_characters = {}
    lower = text.lower()
    for char in lower:
        if char in total_characters:
           total_characters[char] += 1
        else:
            total_characters[char] = 1
    return total_characters

def sort_characters_alpha(all_chars):
    alpha_only = []
    for a in all_chars:
        if a.isalpha():
            alpha = {"name": a, "num": all_chars[a]}
            alpha_only.append(alpha)
    return(alpha_only)

def format_output(input_list):
    for dic in input_list:
        print(f"The '{dic['name']}' character was found {dic['num']} times")


main()