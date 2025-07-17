from geralscan_coletor_24h.extrair import extrair_numero
import requests, time, json

with open("config.json", "r") as f:
    config = json.load(f)

URL = config["url"]
DELAY = config["delay_segundos"]

ultimo = None

while True:
    try:
        numero = extrair_numero()
        if numero != ultimo:
            print(f"[COLETA NOVA] Número: {numero}")
            requests.post(URL, json={"numero": numero})
            ultimo = numero
        else:
            print(f"[AGUARDANDO] Número repetido: {numero}")
    except Exception as e:
        print(f"[ERRO] {e}")
    time.sleep(DELAY)
