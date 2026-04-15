#Um dicionário guarda parâmetros em chaves -> valor

# -> Ideal quando voce quer buscar dados por 'nome' (chave)
# -> Muito usado para configurações, contagem, mapeamento, json,etc

aluno = {
    "nome": "Luis Pedro",
    "idade": 19,
    "curso": "Engenharia de Computação",
    "notas": [8.5, 9.0, 7.5]
}

print(aluno)
print("Nome do aluno:", aluno["nome"])
print("Idade do aluno:", aluno["idade"])
print("Curso do aluno:", aluno["curso"])
print("Notas do aluno:", aluno["notas"])

print("--------------------------------------------------")

#NOVO ALUNO
aluno_novo = {
    "nome": "Pedro Luis",
    "idade": 25,
    "curso": "Engenharia de Software",
    "notas": [6.2, 10.0, 1]
}


print(aluno_novo)
print("Nome do aluno:", aluno_novo["nome"])
print("Idade do aluno:", aluno_novo["idade"])
print("Curso do aluno:", aluno_novo["curso"])
print("Notas do aluno:", aluno_novo["notas"])

aluno_novo["nome"] = "Pedro Luis Costa"
aluno_novo["idade"] = 20

print("Nome do aluno:", aluno_novo["nome"])
print("Idade do aluno:", aluno_novo["idade"])