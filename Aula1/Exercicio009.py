# Tendo como entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal
# utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 e para mulheres (62.1h) - 44.7

h = float(input("Por favor insira sua altura:"))
genero = int(input("Você é homen ou mulher? Use 0 para homen e 1 para mulher"))
if genero == 0:
    peso = (72.7*h) - 58
else:
    peso = (62.1*h) - 44.7
print(f"Seu peso ideal é:{peso}")
    

