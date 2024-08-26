def main():
    file_path = "books/frankenstein.txt"
    file_content = read_file(file_path)
    
    # Here starts the report of "main.py".

    print(f"Let's talk about {file_path}!")
    print("----------------------------------------")
    print("")
    print(f"There are {count_words(file_content)} words in {file_path}")
    print("")
    print("And here you can see how often a specific character was used:")
    report_of_characters(file_content)
    print("")
    print("Thank you for using Bookbot!")



# "read_file(file_path)" will eject the whole text in the file meantioned in "file_path".

def read_file(file_path):
    with open (file_path) as f:
        return f.read()



# "count_words(file_content)" will eject the amount of words in the string "file_content".

def count_words(file_content):
    return len(file_content.split())



# "count_characters(file_content)" will eject the amount of each character in the string "file_content".

def count_characters(file_content):
    character_list = {}
    characters = file_content.lower()
    for character in characters:
        if character.isalpha() == True:
            if character in character_list:    
                character_list[character] += 1
            else:
                character_list[character] = 1
    return character_list



# "character_list_gen(file_content)" will eject a list of dictionaries with the fiven character and the number of uses.

def character_list_gen(file_content):
    character_dict = count_characters(file_content)
    gen_character_list = []
    new_dict = {}
    for key in character_dict:
        new_dict = {"chr": key, "num": character_dict[key]}
        gen_character_list.append(new_dict)
    return gen_character_list



# "report_of_characters(file_content)" will eject a short string which shows how often a character was used.

def report_of_characters(file_content):
    character_list = character_list_gen(file_content)
    character_list.sort(reverse=True, key=get_value)
    for dict in character_list:
        character = dict["chr"]
        number = dict["num"]
        print(f"'{character}' was used {number} times.")



# "get_value(character_list)" will eject the value to its key in a given dictionary.

def get_value(character_list):
    return character_list["num"]



# calling of the "main()" function, otherwise nothing will work.

main()