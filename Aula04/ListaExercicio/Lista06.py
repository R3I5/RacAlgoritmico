# Escreva um programa que solicite ao usuário o valor da compra e verifique se ele tem direito a um desconto. Se o valor da compra for maior que R$ 100,00
# Caso contrário, não conceda o desconto

valorCompra = float(input('Insira o valor da compra: '))
desconto = (valorCompra * 0.1)
if valorCompra > 100.00:
    valorFinal = valorCompra - desconto
    print(f'Seu desconto é de: {desconto} R$, Totalizando: {valorFinal}')
else:
    print('Sua compra não recebe desconto')