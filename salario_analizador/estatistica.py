def calculate_profession_stats(data):
    """Calcula estatísticas por profissão: média salarial, média de idade e total"""
    estatisticas = {}

    for item in data:
        profissao = item['profissao']
        idade = item['idade']
        salario = item['salario']

        if profissao not in estatisticas:
            estatisticas[profissao] = {
                'total_salario': 0,
                'total_idade': 0,
                'quantidade': 0
            }

        estatisticas[profissao]['total_salario'] += salario
        estatisticas[profissao]['total_idade'] += idade
        estatisticas[profissao]['quantidade'] += 1

    # Calcula as médias finais
    resultado_final = {}
    for profissao, valores in estatisticas.items():
        qtd = valores['quantidade']
        resultado_final[profissao] = {
            'media_salario': round(valores['total_salario'] / qtd, 2),
            'media_idade': round(valores['total_idade'] / qtd, 1),
            'total': qtd
        }

    return resultado_final
