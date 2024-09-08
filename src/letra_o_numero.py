def evaluar(caracter):
    if caracter.isdigit():
        return "Es número"
    elif caracter.isalpha():
        if caracter.isupper():
            return "Es letra mayúscula"
        else:
            return "Es letra minúscula"
    else:
        return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
