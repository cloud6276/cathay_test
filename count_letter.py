def count_letters(sentence):
    letter_count = {}
    for letter in sentence:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

sentence = "Hello welcome to Cathay 60th year anniversary"
letter_frequency = count_letters(sentence)
print(letter_frequency)