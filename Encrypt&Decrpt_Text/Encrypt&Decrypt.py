from logo import logo

print(logo)

alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]

def encrypt(original_value, shift_amount):
    cipher_text = ""
    for char in original_value:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char

    print(f"new value is: {cipher_text}")



def decrypt(original_value, shift_amount):
    normal_text = ""
    for char in original_value:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_amount) % 26
            normal_text += alphabets[new_position]
        else:
            normal_text += char
    print(f"original value is: {normal_text}")


while True:
    task = input("Enter if you want to encrypt or decrypt: ").lower()
    text = input("Enter your message: ").lower()
    shift = int(input("Enter your shift number: "))

    if task == "encrypt":
        encrypt(text, shift)
    elif task == "decrypt":
        decrypt(text, shift)
    else :
        print("Please enter a valid task")
        continue

    again = input("Do you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("Goodbye!")
        break
