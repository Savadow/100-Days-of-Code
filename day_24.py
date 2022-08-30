with open("modules/day_24/Input/invited_names.txt") as data:
    names = data.readlines()

with open("modules/day_24/Input/starting_letter.txt") as start:
    letter = start.read()

for i in names:
    name = i.strip("\n")

    with open(f"modules/day_24/Output/letter_to_{name}.txt", mode = "w") as file:
        file.write(letter.replace("[name]", name))