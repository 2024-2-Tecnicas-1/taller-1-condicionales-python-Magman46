def evaluar(peso, estatura, edad):
    imc = peso / (estatura ** 2)
    
    # Determinar la condición de riesgo
    if edad < 45:
        if imc < 22.0:
            return "bajo"
        else:
            return "medio"
    else:
        if imc < 22.0:
            return "medio"
        else:
            return "alto"

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
