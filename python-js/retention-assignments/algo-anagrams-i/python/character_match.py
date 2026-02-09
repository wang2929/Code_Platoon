# Don't forget to run your tests!

def is_character_match(string1, string2):
    string1 = string1.replace(" ", "").upper()
    string2 = string2.replace(" ", "").upper()
    
    if len(string1) != len(string2):
        return False
    else:
        for letter in string1:
            if letter not in string2:
                return False
            idx = string2.index(letter)
            string2 = string2[:idx] + string2[idx+1:]
        return True