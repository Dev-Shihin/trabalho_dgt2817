def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Não foi possível realizar a divisão por 0'
    return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'soma':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    return resultado

saida = ''
while saida.lower() != 'n':
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação (+, -, *, / ou soma, subtracao, multiplicacao, divisao): ')
        resultado = calculadora(num1, num2, operacao)
        print('Resultado da operação: ' + str(resultado))
    except ValueError:
        print('Entrada inválida. Por favor, digite números válidos.')
    saida = input('Deseja continuar? (S/N): ')