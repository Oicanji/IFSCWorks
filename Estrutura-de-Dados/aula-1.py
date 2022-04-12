# 1. Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição,
# subtração, multiplicação e divisão.
def questao1():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print("A soma é: ", num1 + num2)
    print("A subtração é: ", num1 - num2)
    print("A multiplicação é: ", num1 * num2)
    print("A divisão é: ", num1 / num2)

# 2. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando
# um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o
# tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível
# obter a distância percorrida com a fórmula DISTÂNCIA = TEMPO * VELOCIDADE.
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada
# na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve
# apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida
# e a quantidade de litros utilizada na viagem.
def questao2():
    velocidade = int(input("Digite a velocidade média: "))
    tempo = int(input("Digite o tempo gasto na viagem: "))
    distancia = tempo * velocidade
    litros = distancia / 12
    print("A velocidade média é: ", velocidade)
    print("O tempo gasto na viagem é: ", tempo)
    print("A distância percorrida é: ", distancia)
    print("A quantidade de litros utilizada na viagem é: ", litros)

# 3. Leia a idade do usuário e classifique-o em:
# - Criança: 0 a 12 anos;
# - Adolescente: 13 a 17 anos;
# - Adulto: acima de 18 anos;
# - Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida.
def questao3():
    idade = int(input("Digite a sua idade: "))
    if idade < 0:
        print("A idade é inválida.")
    elif idade <= 12:
        print("Você é uma criança.")
    elif idade <= 17:
        print("Você é um adolescente.")
    else:
        print("Você é um adulto.")

# 4. Imprimir a tabuada de um número lido.
def questao4():
    num = int(input("Digite o número para a tabuada: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# 5. (Lista) Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os
# armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para
# somar todos os valores digitados.
def questao5():
    lista = []
    for i in range(5):
        num = int(input("Digite o número: "))
        lista.append(num)
    print("A soma dos números é: ", sum(lista))

# 6. (Dicionário) Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo
# a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova
# estrutura de repetição para somar todas as notas e retornar a média.
def questao6():
    alunos = {}
    for i in range(3):
        nome = input("Digite o nome do aluno: ")
        nota = int(input("Digite a nota do aluno: "))
        alunos[nome] = nota
    print("A média das notas é: ", sum(alunos.values()) / len(alunos))

# 7. (Matriz) Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e
# somar todos os elementos da matriz = np.array([[3, 4, 1], [3, 1, 5]]).
def questao7():
    matriz = np.array([[3, 4, 1], [3, 1, 5]])
    print("A soma dos elementos da matriz é: ", sum(matriz))

# 8. (POO) Crie uma classe chamada aluno com os seguintes atributos: Nome, Nota 1 e Nota
# 2. Crie um construtor para a classe
def questao8():
    class Aluno:
        def __init__(self, nome, nota1, nota2):
            self.nome = nome
            self.nota1 = nota1
            self.nota2 = nota2
    aluno1 = Aluno("João", 7, 8)
    aluno2 = Aluno("Maria", 9, 10)
    print("O aluno 1 é: ", aluno1.nome)
    print("A nota 1 do aluno 1 é: ", aluno1.nota1)
    print("A nota 2 do aluno 1 é: ", aluno1.nota2)
    print("O aluno 2 é: ", aluno2.nome)
    print("A nota 1 do aluno 2 é: ", aluno2.nota1)
    print("A nota 2 do aluno 2 é: ", aluno2.nota2)

# 9. (POO) Crie as seguintes funções (métodos):
# - Calcula média, retornando a média aritmética entre as notas;
# - Mostra dados, que somente imprime o valor de todos os atributos;
# - Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior
# ou igual a 6.0, o aluno está aprovado).
def questao9():
    class Aluno:
        def __init__(self, nome, nota1, nota2):
            self.nome = nome
            self.nota1 = nota1
            self.nota2 = nota2
        def media(self):
            return (self.nota1 + self.nota2) / 2
        def mostra_dados(self):
            print("O aluno é: ", self.nome)
            print("A nota 1 do aluno é: ", self.nota1)
            print("A nota 2 do aluno é: ", self.nota2)
        def resultado(self):
            if self.media() >= 6:
                print("O aluno está aprovado.")
            else:
                print("O aluno está reprovado.")
    aluno1 = Aluno("João", 7, 8)
    aluno2 = Aluno("Maria", 9, 10)
    aluno1.mostra_dados()
    print("A média do aluno é: ", aluno1.media())
    aluno1.resultado()
    aluno2.mostra_dados()
    print("A média do aluno é: ", aluno2.media())
    aluno2.resultado()

# 10. (POO) Crie dois objetos (aluno1 e aluno2) e teste as funções.
def questao10():
    class Aluno:
        def __init__(self, nome, nota1, nota2):
            self.nome = nome
            self.nota1 = nota1
            self.nota2 = nota2
        def media(self):
            return (self.nota1 + self.nota2) / 2
        def mostra_dados(self):
            print("O aluno é: ", self.nome)
            print("A nota 1 do aluno é: ", self.nota1)
            print("A nota 2 do aluno é: ", self.nota2)
        def resultado(self):
            if self.media() >= 6:
                print("O aluno está aprovado.")
            else:
                print("O aluno está reprovado.")
    aluno1 = Aluno("João", 7, 8)
    aluno2 = Aluno("Maria", 9, 10)
    aluno1.mostra_dados()
    print("A média do aluno é: ", aluno1.media())
    aluno1.resultado()
    aluno2.mostra_dados()
    print("A média do aluno é: ", aluno2.media())
    aluno2.resultado()
