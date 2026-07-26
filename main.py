import os
from dotenv import load_dotenv
from workflow_tasks.automation_flow import run_workflow

from worksheet.wonca_labs_api import (
    get_shipping_details, prepare_datas
)
from worksheet.worksheet_functions import (
    get_worksheet
)


# Access Wonca Labs api key to get Correios shipping datas
load_dotenv()
wonca_apk = os.environ.get("woncalabs_apikey")

# Access the text message to send for customers
message_template = ""
with open("message.txt", "r", encoding = "utf-8") as f:
    message_template = f.read()


def main():
    """
    Main function to process the Correios orders report
    """
    worksheet = get_worksheet(
        workspace = "desenvolvimento automação",
        grid = 10171118
    )
    rows = worksheet.get_all_records()

    try:
        # Start work operations for each row
        for row_number, row in enumerate(rows, start = 2):
            control_cell = worksheet.cell(row_number, 4)

            if control_cell.value == "MENSAGEM ENVIADA":
                continue

            details =\
                get_shipping_details(
                    row['CODIGO RASTREIO'], wonca_apk
                )
            pickup_addr =\
                prepare_datas(details)

            run_workflow(
                row['PEDIDO'],
                row['CODIGO RASTREIO'],
                pickup_addr,
                message_template          
            )

            worksheet.update_cell(
                row_number, 4, "MENSAGEM ENVIADA"
            )

    except Exception as e:
        print("Erro de execução capturado\n")
        raise e


if __name__ == "__main__":
    main()