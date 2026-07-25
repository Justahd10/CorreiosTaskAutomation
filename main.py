from automation_flow import run_workflow
from wonca_labs_api import (
    get_shipping_details,
    prepare_datas
)

# Access orders report
import pandas as pd

report_df = pd.DataFrame(pd.read_excel("correios_report.xlsx"))
tracking_codes = report_df['CODIGO RASTREIO']
order_numbers = report_df['PEDIDO']


# Main function to process the report data
def main(report_datas):
    for code, order in zip(
        report_datas['CODIGO RASTREIO'],
        report_datas['PEDIDO']
    ):
        details = get_shipping_details(code)
        pickup_addr = prepare_datas(details)

        run_workflow(code, order, pickup_addr)


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main(report_df)