"""Caesar cipher implemented in python."""

from string import ascii_lowercase


def user_values(palabra, cambio):
    abecedario = list(ascii_lowercase)
    vacio = ""
    if type(palabra) != str:
        return "Invalid type, must be a string."

    if cambio.isdigit() == False:
        return "Invalid type, must be an integer."
    cambio = int(cambio)
    if cambio > 27:
        return "Number must be less than 27."

    """Code for encryption"""
    palabra = palabra.lower()
    for letra in palabra:
        if letra in abecedario: #Checks if letter exist in alphabet.
            posicion_nueva = abecedario.index(letra) + cambio #Get a new letter position.
            if posicion_nueva > len(abecedario) - 1: #In case that new position is bigger than alphabet length.
                diferencia = posicion_nueva - len(abecedario) #Diference between new position and alphabet length.
                vacio += abecedario[diferencia]
            else:
                vacio += abecedario[posicion_nueva]
        else: #In case character is not in alphabet.
            vacio += letra
    return vacio


if __name__ == "__main__":
    print("Introduce your phrase: ")
    word = str(input())

    print("How many numbers would you like to rotate?")
    letter_move = input()

    print(user_values(word, letter_move))
