import subprocess
from itertools import product
import re
import csv
import os

# === CONFIGURAÇÕES ===
parametros = {
    "hms": [10, 20, 30, 40, 50],
    "par": [0.1, 0.3, 0.5, 0.7, 0.9],
}
main_script = "../src/main.py"
modo = "ajuste"

melhor_config = {"hms": 30, "par": 0.7}

diretorios = ['a', 'b']
instancia_inicio = 1
instancia_final = 20
instancias_todas = [f"{d}/instance_{i:04d}.txt" for d in diretorios for i in range(instancia_inicio, instancia_final + 1)]
instancias_ajuste = [
    'a/instance_0001.txt', 'a/instance_0003.txt', 'a/instance_0005.txt',
    'b/instance_0001.txt', 'b/instance_0003.txt', 'b/instance_0005.txt',
    'a/instance_0010.txt', 'b/instance_0010.txt', 'a/instance_0015.txt', 'b/instance_0015.txt'
]
instancias_validacao = [i for i in instancias_todas if i not in instancias_ajuste]

instancias_para_executar = instancias_ajuste if modo == "ajuste" else instancias_validacao


os.makedirs("../src/results", exist_ok=True)
os.makedirs("../src/results/logs", exist_ok=True)
csv_headers = ["Modo", "Instância"] + list(parametros.keys()) + ["OFV", "Status"]

with open("../src/results/results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_headers)

    for instance_name in instancias_para_executar:
        if modo == "ajuste":
            combinacoes = [dict(zip(parametros.keys(), v)) for v in product(*parametros.values())]
        else:
            combinacoes = [melhor_config]

        for params_dict in combinacoes:
            print(f"Executando {instance_name} com {params_dict}")

            command = ["python3", main_script, "--instance", instance_name]
            for k, v in params_dict.items():
                command += [f"--{k}", str(v)]

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate()

            # Extrai valor objetivo e status
            match = re.search(r"Função Objetivo:\s*([-+]?[0-9]*\.?[0-9]+)", stdout)
            if match:
                ofv = float(match.group(1))
                status = "OK"
            else:
                match_timeout = re.search(r"Melhor solução parcial encontrada com OFV = ([-+]?[0-9]*\.?[0-9]+)", stdout)
                if match_timeout:
                    ofv = float(match_timeout.group(1))
                    status = "Parcial"
                else:
                    ofv = "N/A"
                    status = f"Erro: {process.returncode}"

            if status != "OK":
                log_file = f"../src/results/logs/{instance_name.replace('/', '_')}_{params_dict['hms']}_{params_dict['par']}.log"
                with open(log_file, "w") as f:
                    f.write(stdout)
                    f.write("\n--- STDERR ---\n")
                    f.write(stderr)

            writer.writerow([modo, instance_name] + list(params_dict.values()) + [ofv, status])
