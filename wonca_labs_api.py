import os, requests, json
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

# Access wonca labs API Key
@lru_cache
def get_wonca_apk():
    return os.environ.get("woncalabs_apikey")

# Defines the pickup address template
pickup_address = """
Rua: street
Número: number
Bairro: neighborhood
Cidade: city
Estado: state
"""

# Get Correios shipping details by tracking code
def get_shipping_details(tracking_code: str):
    """
    Fetches shipping details from the Wonca Labs API using 
    the provided tracking code.

    Args:
        tracking_code: The tracking code for which to 
        retrieve shipping details.
    """

    url = "https://api-labs.wonca.com.br/wonca.labs.v1.LabsService/Track"

    print(f"[PROGRESS] Consultando API da Wonca Labs para o código: {tracking_code}...")

    req_payload = {
        "code": tracking_code,
    }

    response = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Apikey {get_wonca_apk()}",
        },
        json=req_payload,
    )

    print("[PROGRESS] Resposta da API recebida.")
    return json.loads(response.json()['json'])


def prepare_datas(datas):
    """
    Prepares the shipping details data for further processing.
    """
    print("[PROGRESS] Preparando os dados de rastreamento para montar o endereço...")

    events = datas['eventos']
    awaiting_pickup = "Objeto aguardando retirada no endereço indicado"

    address_template = pickup_address

    for event in events:
        if event['descricao'] == awaiting_pickup:
            addr_data = event['unidade']['endereco']

            print("[PROGRESS] Evento de retirada encontrado. Montando endereço...")

            address_template = address_template.replace(
                "street", addr_data['logradouro']
            ).replace(
                "number", addr_data['numero']
            ).replace(
                "neighborhood", addr_data['bairro']
            ).replace(
                "city", addr_data['cidade']
            ).replace(
                "state", addr_data['uf']
            )

            print("[PROGRESS] Endereço montado com sucesso.")
            return address_template