PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_files:
    names=names_files.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_files:
    letter_contents=letter_files.read()
    for name in names:
        stripped_name=name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as complete_letter:
            complete_letter.write(new_letter)
