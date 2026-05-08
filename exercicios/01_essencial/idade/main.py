def resposta(ano_nascimento):
    ano_nascimento = int(ano_nascimento)
    idade = 2026 - ano_nascimento
    return idade

ano_nascimento = input("Digite o ano: ")
print(resposta(ano_nascimento))