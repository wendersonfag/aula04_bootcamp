
#Type Hint

# Sem Type Hint
idade = 30
altura = 1.75
nome = "Alice"
is_estudante = True

#Com Type Hint
idade: int = 30
altura: float = 1.75
nome: str = "Alice"
estudante: bool = True

### Resoluções de Listas e Dicionários

# 1 . Lista de números ao quadrado

numeros = list(range(1,11))

for i in numeros:
    print(i**2)


#2. Modificar lista de linguagens
linguagens = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")
print(linguagens)

#3. Informações de um livro
livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}

for chave, valor in livro.items():
    print(f"{chave},{valor}")

#4. Contar ocorrências de caracteres
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

#5. Preço total da lista de compras
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
 
total = 0 
for item in lista_compras:
    total += precos[item]

total2 = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")

print(total)
print(total2)

## Exercícios intermediários e mais avançados

#6. Eliminação de Duplicatas
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

emails_unicos = list(set(emails))

print(emails_unicos)


# 7. Filtragem de Dados
idades = [22, 15, 30, 17, 18]
idade_valida = [i for i in idades if i >= 18]

print(idade_valida)

# 8. Ordenação Personalizada
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

pessoas.sort(key=lambda nome: nome["nome"])

print(pessoas)


#9. Agregação de Dados
numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)

print("Média:", media)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [par for par in valores if par % 2 ==0]
impares = [impar for impar in valores if impar % 2 ==1]

print(f"Valore Pares: {pares}")
print(f"Valores Impar: {impares}")

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos)


# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)


# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

filtro_estoque  = {produto: quantidade for  produto, quantidade in estoque.items() if quantidade > 0}

print(filtro_estoque)


# #14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves:", chaves)
print("Valores:", valores)

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)


# 3.Lendo arquivos

import csv

path_file = 'exemplo.csv'


dados = []

with open(file=path_file, mode="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        dados.append(linha)

for registro in dados:
    print(registro)


### 4. Funções

# Função de Ordenação Personalizada

# Implementação do algoritmo de ordenação por seleção
lista = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Ordenando a lista
print("Lista ordenada com função personalizada:", lista)


