def indice_massa(peso_kq: float, altura_n: float) -> float:
    
    if peso_kq <= 0 or altura_n <= 0:
    
        return -1.0
    
    
    imc = peso_kq / (altura_n ** 2)
    return round(imc, 1)

imc = indice_massa(70, 1.75)
print(f"IMC: {imc}")

imc2 = indice_massa(95, 1.70)
print(f"IMC: {imc2}")

invalido = indice_massa(-5, 1.70)
print(f"IMC: {invalido}")

#exercicio 2

def Classificar_IMC_risco(imc, verificar_risco=True):
    
    if imc < 18.5:
        print("Abaixo do peso")
    
    elif imc >= 18.5 or <= 24.9:
        print("Peso normal ✅")

    



