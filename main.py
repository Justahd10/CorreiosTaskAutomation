from workflow.automation_flow import run_workflow
from correios_report.wonca_labs_api import (
    get_shipping_details, prepare_datas
)
from correios_report.orders_report import (
    get_report_datas, report_worksheet, file_path
)


datas = get_report_datas()


# Main function to process the report data
def main():

    for idx, values in enumerate(zip(
        datas['tracking_codes'],
        datas['orders_numbers']
    ), start = 1):
        details = get_shipping_details(values[0])
        pickup_addr = prepare_datas(details)

        run_workflow(values[1], values[0], pickup_addr)

        # Edit report worksheet
        report_worksheet.active.delete_rows(idx)
        report_worksheet.save(file_path)



# Execute the main function if the script is run directly
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Exeção de execução caputarada:", e)