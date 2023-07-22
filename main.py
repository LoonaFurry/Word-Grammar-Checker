from spellchecker import SpellChecker

spell = SpellChecker()

word_list = []

while True:
    word = input("Enter a word (or 'exit' to quit): ")
    if word == "exit":
        break
    if word not in word_list:
        # Check for typos and fix them
        corrected_word = spell.correction(word)
        if corrected_word != word:
            print(f"Typo detected: '{word}' -> '{corrected_word}'")
        word_list.append(corrected_word)
    else:
        print("Duplicate word detected.")

print("Final word list:", word_list)