# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista
# Após isso, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram. 

listaT = []
mesesMaiores = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i, mes in enumerate(meses): #função enumerate pega o valor e a posição do item na lista
        temperatura = int(input(f'Digite a temperatura para o mês {mes}: '))
        listaT.append(temperatura)

media = (sum(listaT))/12
print(f'A temperatura média é: {media:.2f}')

for i, temperatura in enumerate(listaT): 
    if temperatura > media:
        mesesMaiores.append(meses[i])

print(f'Os meses com temperatura acima da média foram: ')
for mes in mesesMaiores:
    print(mes)