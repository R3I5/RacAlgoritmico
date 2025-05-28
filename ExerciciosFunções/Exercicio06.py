# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 pm. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para a saída. Registre a informação AM/PM como um valor 'a' para am e 'p' para PM. 
# Assim, a função para efetuar as conversões tera um parâmetro formal para registrar se é AM ou PM. Inclua um loop que permita que o usuario repita esse cálculo para novos valores de entrada todas as vezes que desejar. 


def conversao(horas24, minutos24):
    if horas24<12:
        return f'{horas24:0d}'