def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    count = count_words(text)
    charcount = countchar(text)
    presorted_charcount = presortdict(charcount)
    # print(presorted_charcount)
    presorted_charcount.sort(reverse=True, key=sort_on)
    print(presorted_charcount)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    for char in presorted_charcount:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")


def get_text(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


def countchar(text):
    countchar_dict = dict()
    for char in text:
        lower_text = char.lower()
        if lower_text in countchar_dict and lower_text.isalpha():
            countchar_dict[lower_text] += 1
        elif lower_text.isalpha():
            countchar_dict[lower_text] = 1
    return countchar_dict


def presortdict(countchar_dict):
    list_countchar = list(countchar_dict)
    presortlist = list()
    for key in list_countchar:
        # print(key)
        presortdict = dict()
        presortdict["char"] = key
        # print(presortdict)
        presortdict["count"] = countchar_dict[key]
        # print(presortdict)
        presortlist.append(presortdict)
        # print(presortlist)

    return presortlist


def sort_on(dict):
    return dict["count"]


main()
