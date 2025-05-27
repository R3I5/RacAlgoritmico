# Faça um programa com uma função chamda somaImposto. A função possui dois parâmetros formais: taxaImposto
# que é uma quantida de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
# A função "altera" o valor de custo para incluir o imposto sobre vendas

def somaImposto(taxaImposto, custo):
    valorTotal = ((custo*(taxaImposto/100))+custo)
    return valorTotal

taxa = int(input("Insira o valor da taxa: "))
valor = int(input("Insira o valor do item: "))
print(somaImposto(taxa,valor))