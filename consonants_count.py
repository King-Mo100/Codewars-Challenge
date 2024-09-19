def consanat_count(s):
    vowels = "aeiou"
    counter = 0
    for letter in s.lower():
        if (letter not in vowels) and letter.isalpha():
            counter += 1
    return counter
