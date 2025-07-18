from collections import defaultdict

def media_salarial_por_profissao(dados):
    soma = defaultdict(float)
    contagem = defaultdict(int)
    
    for pessoa in dados:
        profissao = pessoa['Profissão']
        salario = float(pessoa['Salário (R$)'])
        soma[profissao] += salario
        contagem[profissao] += 1
    
    medias = {prof: soma[prof]/contagem[prof] for prof in soma}
    return medias

def melhor_salario_por_experiencia(dados):
    melhor = None
    for pessoa in dados:
        salario = float(pessoa['Salário (R$)'])
        experiencia = float(pessoa['Experiência (anos)'])
        if experiencia > 0:
            relacao = salario / experiencia
            if not melhor or relacao > melhor['r']:
                melhor = {'nome': pessoa['Nome'], 'profissao': pessoa['Profissão'], 'r': relacao}
    return melhor

def estatisticas_por_faixa_etaria(dados):
    faixas = {'20-30': [], '31-40': [], '41+': []}
    
    for pessoa in dados:
        idade = int(pessoa['Idade'])
        salario = float(pessoa['Salário (R$)'])
        if 20 <= idade <= 30:
            faixas['20-30'].append(salario)
        elif 31 <= idade <= 40:
            faixas['31-40'].append(salario)
        elif idade >= 41:
            faixas['41+'].append(salario)
    
    resultado = {}
    for faixa, salarios in faixas.items():
        if salarios:
            media = sum(salarios) / len(salarios)
            resultado[faixa] = {'media_salarial': round(media, 2), 'qtd': len(salarios)}
        else:
            resultado[faixa] = {'media_salarial': 0, 'qtd': 0}
    return resultado
