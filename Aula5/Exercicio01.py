string = input('Digite algo: ')
print(string)
vogais = {'a','e','i','o','u'}
vogaisPresentes = set(string) & vogais
print(vogaisPresentes)