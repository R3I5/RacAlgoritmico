# Criar um programa que solicita ao usuário 6 números, calculando sua média
# Mostrar ao usuário uma lista com os números iguais ou acima da média e uma lista com os números abaixo da média

nums = []
maior = []
menor = []
for i in range(6):
    num = int(input(f'Digite o {i+1}° numero: '))
    nums.append(num)
print(f'Seus numeros são: {nums}')


media = (sum(nums))/6
print(f'A sua media é: {media:.2f}')


for num in nums:
    if num >= media:
        maior.append(num)
    if num < media:
        menor.append(num)
print(f'Os números menores que a média são: {menor}')
print(f'Os números maiores que a média são: {maior}')