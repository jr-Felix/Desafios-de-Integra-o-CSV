# Abrir e ler todo o conteúdo
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Obter o cabeçalho
cabecalho = linhas[0].strip().split(",")
print("Cabeçalho:", cabecalho)

# Ler o restante das linhas
for linha in linhas[1:]:
    dados = linha.strip().split(",")
    print("Dados:", dados)
