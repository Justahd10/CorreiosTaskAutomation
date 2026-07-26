# Importing workflow process
from workflow.bling import (
    copy_customer_email, copy_customer_phone_number
)
from workflow.omni import (
    send_email_message, send_whatsapp_message,
    past_customer_phone_number
)

# Set the FailSafeException
import pyautogui as auto
auto.FAILSAFE = True


def make_msg_template(
    order_number: str, tracking_code: str, pickup_addres: str,
    message: str,
):
    """
    Replaces the template placeholders with the order 
    information.

    Args:
        order_number: Order number to be shared with the 
        customer. tracking_code: Tracking code associated with 
        the order.
        msg_template: Base text containing the 
        replacement markers.

    Returns:
        A ready-to-send message with the data inserted.
    """
    
    message = (
        message.replace(
            "NUMERO_PEDIDO", str(order_number) or ""
        )
    ).replace(
        "CODIGO_RASTREIO", tracking_code
    ).replace("ENDERECO_RETIRADA", pickup_addres)

    return message


def run_workflow(order, code, address, msg_template):
    """
    Run the customer workflow for a Correios order.

    This function builds a personalized message from the 
    provided template, searches for customer data in Bling 
    by tracking code, and then sends the appropriate email 
    and WhatsApp notifications.

    Args:
        order: Order number to use in the message text.
        code: Tracking code used to locate the customer record.
        address: Pickup address to insert into the message.
        msg_template: Template string containing placeholders.

    Returns:
        None
    """

    msg = make_msg_template(order, code, address, msg_template)

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