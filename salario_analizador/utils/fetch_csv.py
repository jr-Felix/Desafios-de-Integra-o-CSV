import csv
import io
import urllib.request

def baixar_csv(link_compartilhado):
    link_csv = link_compartilhado.replace("/edit?usp=sharing", "/export?format=csv")
    try:
        with urllib.request.urlopen(link_csv) as response:
            conteudo = response.read().decode('utf-8')
            return list(csv.DictReader(io.StringIO(conteudo)))
    except Exception as e:
        print("Erro ao baixar ou processar CSV:", e)
        return []
