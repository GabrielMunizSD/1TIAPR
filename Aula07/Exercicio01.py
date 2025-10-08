# Função para soma
def soma(a, b):
    return a + b

# Função para subtração
def subtracao(a, b):
    return a - b

# Função para multiplicação
def multiplicacao(a, b):
    return a * b

# Função para divisão
def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero"
    return a / b

# Parte principal do programa (entrada de dados)
# Solicita os dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza e exibe cada operação
print("Soma:", soma(num1, num2))
print("Subtração:", subtracao(num1, num2))
print("Multiplicação:", multiplicacao(num1, num2))
print("Divisão:", divisao(num1, num2))

