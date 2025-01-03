def main():
    
    with open("books/frankenstien.txt") as f:
        file_contents = f.read()
        #print full contents of book
        #print(file_contents)
    
        #Print nice header message
        print(f"--- Begin report of {f} ---")

        #Print word count for book
        count = len(file_contents.split())
        print(f"{count} words found in the document")
        
        #Print character count for each character
        lower_file = file_contents.lower()
        char_count = {}
        for char in lower_file:
            if char.isalpha() == True:
                if char not in char_count:
                    char_count[char] = 1
                char_count[char] += 1
        #print(char_count)
        ch_list = []
        for x in char_count:
            ch_list.append({"count":char_count[x],"char":x})
        #print(ch_list)
        ch_list.sort(reverse=True, key=sort_on)
        for item in ch_list:
            char=item["char"]
            num=item["count"]
            print(f"The '{char}' character was found {num} times")


def sort_on(dict):
    return dict["count"]

main()