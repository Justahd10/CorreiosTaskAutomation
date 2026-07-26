import requests, json
from dotenv import load_dotenv

load_dotenv()

# Pickup address template
pickup_address = """
Rua: street
Número: number
Bairro: neighborhood
Cidade: city
Estado: state
"""

# Status associeted to order awaiting pickup event
awaiting_pickup_status = [
    "Objeto aguardando retirada no endereço indicado",
    "Objeto encaminhado para retirada no endereço indicado",
    "Objeto aguardando retirada na Caixa Postal"
]


# Get Correios shipping details by tracking code
def get_shipping_details(tracking_code: str, api_key):
    """
    Fetches shipping details from the Wonca Labs API using 
    the provided tracking code.

    Args:
        tracking_code: The tracking code for which to 
        retrieve shipping details.
    """

    url = "https://api-labs.wonca.com.br/wonca.labs.v1.LabsService/Track"

    print(f"Consultando rastreamento. Código: {tracking_code}...\n")

    req_payload = {
        "code": tracking_code,
    }

    response = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Apikey {api_key}",
        },
        json=req_payload,
    )

    print("[PROGRESS] Resposta da API recebida.\n")
    return json.loads(response.json()['json'])


def prepare_datas(datas):
    """
    Prepares the shipping details data for further processing.
    """
    print("Preparando os dados de rastreamento...\n")

    events = datas['eventos']
    address_template = pickup_address

    for event in events:
        if event['descricao'] in awaiting_pickup_status:
            addr_data = event['unidade']['endereco']

            print("Montando endereço de retirada...\n")

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

            print("Endereço montado com sucesso.")

            return address_template