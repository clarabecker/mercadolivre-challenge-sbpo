import csv
from collections import defaultdict

resultados = defaultdict(list)

with open("results.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Status"] == "OK":
            hms = int(row["hms"])
            par = float(row["par"])
            ofv = float(row["OFV"])
            resultados[(hms, par)].append(ofv)

# Agora calcula a média para cada combinação
medias = {
    config: sum(ofvs) / len(ofvs)
    for config, ofvs in resultados.items()
}

# Encontra a combinação com menor média
melhor_config, melhor_media = min(medias.items(), key=lambda x: x[1])

print("Melhor configuração média:")
print(f"hms = {melhor_config[0]}, par = {melhor_config[1]}")
print(f"Média OFV = {melhor_media}")
