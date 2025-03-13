def adicao(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Não e possivel realizar a divisão por 0' 


def calculadora(num1, num2, operacao):
    if operacao == '-' or operacao == 'subtração':
        return subtracao(
            num1=num1,
            num2=num2,
        )
    elif operacao == '+' or operacao == 'adição':
        return adicao(
            num1=num1,
            num2=num2,
        )
    elif operacao == '*' or operacao == 'multiplcação':
        return multiplicacao(
            num1=num1,
            num2=num2,
        )
    elif operacao == '/' or operacao == 'divisão':
        return divisao(
            num1=num1, 
            num2=num2, 
        ) 
 

saida = ''

while saida != 'n':
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    opcao = input('Qual operação deseja fazer? ')
    resultado = calculadora(
        num1=n1,
        num2=n2,
        operacao=opcao
    )

    print(f'Resultado da operação: {resultado}')

    while True:
        saida = input('Deseja continuar digite [S/N]: ').lower()
        if saida == 'n'or saida == 's':
            break
