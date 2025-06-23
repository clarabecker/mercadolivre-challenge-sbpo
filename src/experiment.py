import subprocess
from itertools import product
import re
import csv

valores = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

diretorios = ['a', 'b']
instancia_inicio = 1
instancia_final = 20

main_script = "main.py"

with open("results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Instância", "HMCR", "PAR", "OFV", "Status"])

    for dir in diretorios:
        for i in range(instancia_inicio, instancia_final + 1):
            instance_name = f"{dir}/instance_{i:04d}.txt"

            for hmcr, par in product(valores, repeat=2):
                print(f"Executando {instance_name} com hmcr={hmcr}, par={par}")

                command = [
                    "python3", main_script,
                    "--instance", instance_name,
                    "--hmcr", str(hmcr),
                    "--par", str(par)
                ]

                result = subprocess.run(command, capture_output=True, text=True)

                #pegar valor da solucao
                match = re.search(r"Objective function value: \s*([-+]?[0-9]*\.?[0-9]+)", result.stdout)

                if match:
                    ofv = float(match.group(1))
                    status = "OK"
                    print(f"ofv: {ofv}")
                else:
                   if result.returncode != 0:
                    status = f"Erro: {result.returncode}"
                    print("Erro:")
                    print(result.stderr)

                #escrever no arquivo csv
                writer.writerow([instance_name, hmcr, par, ofv, status])
