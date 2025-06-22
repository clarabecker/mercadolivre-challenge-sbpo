import subprocess
from itertools import product
import re
import csv

# Valores dos parâmetros
values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

folders = ['a', 'b']
start_idx = 1
end_idx = 20

main_script = "main.py"

with open("results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Instância", "HMCR", "PAR", "OFV", "Status"])

    for folder in folders:
        for i in range(start_idx, end_idx + 1):
            instance_name = f"{folder}/instance_{i:04d}.txt"

            for hmcr, par in product(values, repeat=2):
                print(f"Rodando instância {instance_name} com hmcr={hmcr}, par={par}")

                command = [
                    "python3", main_script,
                    "--instance", instance_name,
                    "--hmcr", str(hmcr),
                    "--par", str(par)
                ]

                result = subprocess.run(command, capture_output=True, text=True)

                # Extrair valor da função objetivo
                match = re.search(r"Valor da função objetivo \(OFV\):\s*([-+]?[0-9]*\.?[0-9]+)", result.stdout)
                if match:
                    ofv = float(match.group(1))
                    status = "OK"
                    print(f"OFV extraído: {ofv}")
                else:
                    ofv = None
                    status = "OFV não extraído"
                    print("Não foi possível extrair o valor da função objetivo (OFV) da saída.")

                if result.returncode != 0:
                    status = f"Erro: {result.returncode}"
                    print("Erro:")
                    print(result.stderr)

                # Escrever no CSV
                writer.writerow([instance_name, hmcr, par, ofv, status])
