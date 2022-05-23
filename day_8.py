################
#### Part 1 ####
################

# import math

# def paint_calc(height, width, cover):
#     num_of_cans = (height * width) / cover
#     print(f"You'll need {math.ceil(num_of_cans)} cans of paint")

# h = int(input("Height of the wall: "))
# w = int(input("Height of the wall: "))
# coverage = 5

# paint_calc(height = h, width = w, cover = coverage)

################
#### Part 2 ####
################

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
    
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")

# n = int(input("Check this number: "))
# prime_checker(number = n)

##############
#### Main ####
##############

def cipher(decision, string, shift):
    """
    ==========================================================================
    Returns an encoded or decoded string based decision and a specified shift.
    ==========================================================================

    Parameters:
    ==========
            decision: either 'encode' or 'decode'
            string: message to be encoded
            shift: argument that specifies how much forward to shift the letters
    """

    new_text = ""

    for character in string:
        # Check for special characters
        if character not in alphabet:
            new_text += character

        # Shiftting characters
        else:
            index = alphabet.index(character)
            letter = index + shift

            if decision == "encode":
                # Looping to the beginning of the list
                if letter <= len(alphabet) - 1:
                    new_text += alphabet[letter]
                else:
                    new_text += alphabet[letter - len(alphabet)]

            elif decision == "decode":
                letter = index - shift
                new_text += alphabet[letter]

    if decision == "encode":
        return new_text
    elif decision == "decode":
        return new_text.capitalize()


permission = True
while permission:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    string = input("Enter message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % len(alphabet)

    print(cipher(direction, string, shift))

    user = input("Do you want to restart the cipher program?: ").lower()
    if user == "no":
        permission = False