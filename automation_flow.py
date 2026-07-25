# Importing workflow process
from flows.bling import (
    copy_customer_email,
    copy_customer_phone_number
)
from flows.omni import (
    send_email_message,
    send_whatsapp_message,
    past_customer_phone_number
)

# Set the FailSafeException
import pyautogui as auto
auto.FAILSAFE = True


# Prepare message template
message_template = ""
with open("message.txt", "r", encoding = "utf-8") as f:
    message_template = f.read()


def make_msg_template(
    order_number: str, tracking_code: str, pickup_addres: str
):
    """
    Replaces the template placeholders with the order 
    information.

    Args:
        order_number: Order number to be shared with the 
        customer. tracking_code: Tracking code associated with 
        the order.msg_template: Base text containing the 
        replacement markers.

    Returns:
        A ready-to-send message with the data inserted.
    """
    msg_template = message_template

    msg_template = (
        msg_template.replace(
            "NUMERO_PEDIDO", order_number or ""
        )
    ).replace(
        "CODIGO_RASTREIO", tracking_code
    ).replace("ENDERECO_RETIRADA", pickup_addres)

    return msg_template


# Start automation, running the flows for each tracking code
# All workflow consists of the flow for invoices management
# and customer service platforms

def run_workflow(order, code, address):
    msg = make_msg_template(order, code, address)

    print(f"Trabalhando no pedido {order}, código de rastreio {code}...")

    # Search customer datas using Correios tracking code
    # If no results, and send email message
    if copy_customer_email(code):
        print("[PROGRESS] Email do usuário coletado.\n")

        # After send email message, check for phone number
        # If not exists, get the data from invoices web site
        if not send_email_message(msg):
            print("[PROGRESS] Verificando telefone do usuário.\n")
            copy_customer_phone_number()

            print("[PROGRESS] Número de telefone coletado.\n")
            past_customer_phone_number()
        else:
            print("[PROGRESS] Usuário contém telefone.\n")

        print("[PROGRESS] Enviando mensagem de WhatsApp.\n")
        send_whatsapp_message(msg)

        print("[PROGRESS] Mensagem por WhatsApp enviada.\n")