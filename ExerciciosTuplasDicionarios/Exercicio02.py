# 2. Frota Alfa

ano_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557609.92
}
unidades = [
    "Parsec (pc)", 
    "Ano-Luz (al)", 
    "Unidade Astronômica (ae)",
    "Minuto-Luz(ml)", 
    "Segundo-Luz (sl)"]

# Imprimir a lista de unidades de conversão;
while True:
    print("Iniciando conversão de unidades...")
    for unidade in unidades:
        print(unidade)
    print()
# Solicitar o valor que se deseja converter usando a frase "Valor a ser convertido: "
    try:
        valor = float(input("Valor a ser convertido: "))
    
# Solicitar a unidade origem do valor usando a frase "Converter de:"

        unidadeOrigem = input("Converter de: ").strip().lower()
    
# Solicitar a unidade destino de conversão usando a frase "Converter para:"   
    
        unidadeDestino = input("Converter para:").strip().lower()
        
# Exibir o valor convertido 

        if unidadeOrigem not in ano_luz or unidadeDestino not in ano_luz:
            print("Unidade invalida!")
            continue
        valorOrigem = valor/ano_luz[unidadeOrigem]
        valorConvertido = valorOrigem * ano_luz[unidadeDestino]
        print(f"Conversão: {valor} {unidadeOrigem} = {valorConvertido:.2f} {unidadeDestino}")
        print()
        continuar = input("Deseja fazer outra conversão? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até a proxima!")
            break
    except ValueError:
        print("Valor inválido")
