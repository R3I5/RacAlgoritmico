#Criar um programa que lê as temperaturas médias de cada mês do ano e as armazena em uma lista.
#Usar um outro vetor para guardar e exibir, quando necessário, os nomes dos meses do ano.
#Calcular a média anual de temperatura, e informar quais meses ficaram acima desta média anual.

listaT = []
mesesMaiores = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i, mes in enumerate(meses):
        temperatura = int(input(f'Digite a temperatura para o mês {mes}: '))
        listaT.append(temperatura)

media = (sum(listaT))/12
print(f'A temperatura média é: {media:.2f}')

for i, temperatura in enumerate(listaT): #Função enumerate pega o valor e a posição do item na lista
    if temperatura > media:
        mesesMaiores.append(meses[i])

print(f'Os meses com temperatura acima da média foram: ')
for mes in mesesMaiores:
    print(mes)


