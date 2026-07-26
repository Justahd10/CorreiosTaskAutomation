# Access orders report
import pandas as pd, pathlib, openpyxl

# Get worksheet contaning Correios orders report
file_path = (pathlib.Path.cwd() / "correios_report" / "correios_report.xlsx").as_posix()



def get_report_datas():
    report_df = pd.read_excel(file_path)

    tracking_codes = report_df['CODIGO RASTREIO']
    order_numbers = report_df['PEDIDO']

    return {
        "tracking_codes": tracking_codes,
        "orders_numbers": order_numbers
    }


report_worksheet = openpyxl.load_workbook(file_path)