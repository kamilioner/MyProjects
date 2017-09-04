###Ex2:

def cutter(word):
    shortened = 0
    if len(word) < 4:
        printer = word
    else:
        if (word[:3] in ("pre", "pro", "con", "com")):
            temp_word = word[3:]
            shortened = 1
        else:
            if (word[:4] in ("post", "para")):
                temp_word = word[4:]
                shortened = 1
            else:
                temp_word = word
        if (temp_word[(len(temp_word)-2):]) in ("ed"):
            printer = temp_word[:len(temp_word)-2]
            shortened = 1
        else:
            if (temp_word[(len(temp_word) - 3):]) in ("ing", "ate"):
                printer = temp_word[:len(temp_word) - 3]
                shortened = 1
            else:
                if (temp_word[(len(temp_word) - 4):]) in ("tion", "ment"):
                    printer = temp_word[:len(temp_word) - 4]
                    shortened = 1
                else:
                    printer = temp_word

    if shortened != 1:
        print("Word cannot be shortened")
    else:
        print("Word has been shortened")
    return printer

print(cutter("king"))