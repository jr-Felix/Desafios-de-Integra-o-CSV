import urllib.request
import csv
import io

def baixar_csv(url):
    try:
        with urllib.request.urlopen(url) as resposta:
            conteudo = resposta.read().decode('utf-8')
            csv_file = io.StringIO(conteudo)
            leitor = csv.DictReader(csv_file)
            return list(leitor)
    except Exception as e:
        print("Erro ao baixar ou processar CSV:", e)
        return []

def media_salarial_por_profissao(dados):
    medias = {}
    contagens = {}
    for linha in dados:
        if 'profissao' not in linha or 'salario' not in linha:
            continue
        try:
            salario = float(linha['salario'])
        except:
            continue
        prof = linha['profissao']
        medias[prof] = medias.get(prof, 0) + salario
        contagens[prof] = contagens.get(prof, 0) + 1
    return {prof: medias[prof] / contagens[prof] for prof in medias}

def melhor_salario_por_experiencia(dados):
    melhor = None
    for linha in dados:
        try:
            salario = float(linha['salario'])
            experiencia = float(linha['experiencia'])
            if experiencia == 0:
                continue
            r = salario / experiencia
            if not melhor or r > melhor['r']:
                melhor = {
                    'nome': linha['nome'],
                    'profissao': linha['profissao'],
                    'r': r
                }
        except:
            continue
    return melhor

def estatisticas_por_faixa_etaria(dados):
    faixas = {
        'até 25': [],
        '26 a 35': [],
        '36 a 50': [],
        'mais de 50': []
    }
    for linha in dados:
        try:
            idade = int(linha['idade'])
            salario = float(linha['salario'])
        except:
            continue
        if idade <= 25:
            faixas['até 25'].append(salario)
        elif idade <= 35:
            faixas['26 a 35'].append(salario)
        elif idade <= 50:
            faixas['36 a 50'].append(salario)
        else:
            faixas['mais de 50'].append(salario)
    resultado = {}
    for faixa, salarios in faixas.items():
        if salarios:
            media = sum(salarios) / len(salarios)
            resultado[faixa] = {'media_salarial': media, 'qtd': len(salarios)}
    return resultado


