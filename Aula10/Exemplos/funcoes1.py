# Funções são fragmentos de códigos que permitem organizar algoritmos e reduzir sua repetição.
# A partir do uso correto de funções um projeto fica mais fácil de manter, bem como torna-se mais legível, uma vez que funcionalidades específcas podem ser colocadas em poucas linhas
# Exemplo:

def soma(num1, num2):
    s = num1 + num2
    return s

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

resultado = soma(numero1,numero2)

print(f"O resultado é: {resultado}")
