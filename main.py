import pathlib, os
from dotenv import load_dotenv
from workflow.automation_flow import run_workflow
from correios_report.wonca_labs_api import (
    get_shipping_details, prepare_datas
)


# Access Wonca Labs api key to get Correios shipping datas
load_dotenv()
wonca_apk = os.environ.get("woncalabs_apikey")

# Access the text message to send for customers
message_template = ""
with open("message.txt", "r", encoding = "utf-8") as f:
    message_template = f.read()


# Main function to process the Correios orders report
def main():
    with open(
        (
            pathlib.Path.cwd()/"correios_report"/"correios_report.csv"
        ).as_posix(),
        "r+", encoding="utf-8"
    ) as report_file:
        rows = report_file.readlines()

        # Prepare CSV columns mapping
        def get_col_idx(name):
            return rows[0].replace("\n", "").split(",").index(name)

        orders_col = get_col_idx("PEDIDO")
        code_col = get_col_idx("CODIGO RASTREIO")

        try:
            # Start work operations for each row
            for idx, row in enumerate(rows[1:], start = 1):
                row = row.replace("\n", "").split(",")

                details =\
                    get_shipping_details(
                        row[code_col], wonca_apk
                    )
                pickup_addr =\
                    prepare_datas(details)

                run_workflow(
                    row[orders_col],
                    row[code_col],
                    pickup_addr,
                    message_template          
                )

        except Exception as e:
            print("Erro de execução capturado\n")

            print("A editar arquivo CSV...")
            remaining_rows = [rows[0]] + rows[idx:]
            report_file.seek(0)
            report_file.writelines(remaining_rows)
            report_file.truncate()
            print("Edição concluída.")

            raise e


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()