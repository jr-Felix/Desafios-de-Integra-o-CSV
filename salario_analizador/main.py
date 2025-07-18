# main.py
from processador import baixar_csv, media_salarial_por_profissao, melhor_salario_por_experiencia, estatisticas_por_faixa_etaria

def main():
    # Link de exportação CSV da planilha
    link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSPKhAvB_jzKbI8_VHg8fUTGmA3WfIaiXLFv6XfviWW4xsBL68dtSXEeVk8C6lArQK4lQcxbFWc0L4D/pub?output=csv"

    dados = baixar_csv(link)

    if not dados:
        print("Erro ao carregar dados.")
        return

    print("\n--- MÉDIA SALARIAL POR PROFISSÃO ---")
    medias = media_salarial_por_profissao(dados)
    for prof, media in medias.items():
        print(f"{prof}: R$ {media:.2f}")

    print("\n--- MELHOR RELAÇÃO SALÁRIO/EXPERIÊNCIA ---")
    melhor = melhor_salario_por_experiencia(dados)
    if melhor:
        print(f"{melhor['nome']} ({melhor['profissao']}): R$/{melhor['r']:.2f} por ano de experiência")

    print("\n--- ESTATÍSTICAS POR FAIXA ETÁRIA ---")
    estatisticas = estatisticas_por_faixa_etaria(dados)
    for faixa, info in estatisticas.items():
        print(f"{faixa}: média salarial = R$ {info['media_salarial']:.2f}, pessoas = {info['qtd']}")

if __name__ == "__main__":
    main()
