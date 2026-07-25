import time
import pyautogui as auto
from pyautogui import ImageNotFoundException
from auto_functions import (
    click_on_img, run_keys_sequence
)

auto.FAILSAFE = True
auto.PAUSE = 0.5


def send_email_message(msg):
    """
    Sends an email message through the Omni interface.

    Args:
        msg: Content of the message to be sent to the 
        customer.

    Returns:
        True when the phone number already exists, False 
        when a new number
        needs to be registered.
    """
    print("[PROGRESS] Enviando mensagem de email ao usuário.\n")

    click_on_img(
        "screenshots/omni_nome_aba.png"
    )

    click_on_img(
        "screenshots/omni_botao_enviar_mensagem.png"
    )

    auto.write("diognasde06@gmail.com")
    auto.press("enter")

    click_on_img(
        "screenshots/omni_opcao_email_contato_hesed.png"
    )

    auto.write("Pedido aguardando retirada")

    click_on_img(
        "screenshots/omni_texto_escrever_mensagem.png"
    )

    auto.write(msg)

    click_on_img(
        "screenshots/omni_botao_enviar.png",
        confidence = 0.8
    )

    click_on_img(
        "screenshots/omni_link_vizualizar.png",
        confidence = 0.8
    )

    #
    click_on_img(
        "screenshots/omni_botao_macro.png",
        confidence = 0.95
    )
    click_on_img(
        "screenshots/omni_botao_abrir_conversa.png",
        confidence = 0.95
    )
    auto.click()
    auto.click(1350, auto.position()[1])

    print("Mensagem de email enviada!")

    try:
        auto.locateOnScreen(
            "screenshots/omni_numero_indisponivel.png",
            confidence = 0.95
        )
    except ImageNotFoundException:
        print("[PROGRESS] Usuário já está com o telefone informado.\n")
        return True
    else:
        return False


def past_customer_phone_number():
    print("[PROGRESS] Atualizando cadastro do usuário com o telefone informado.\n")

    click_on_img(
        "screenshots/omni_nome_aba.png"
    )

    click_on_img(
        "screenshots/botao_editar_contato.png"
    )

    click_on_img(
        "screenshots/botao_editar_contato.png"
    )

    click_on_img(
        "screenshots/omni_campo_adicionar_numero.png"
    )

    auto.hotkey("ctrl", "v")

    run_keys_sequence(
        [
            "left", "left", "left", "left", 
            "backspace", "left", "left", "left",
            "left", "left", "backspace", "backspace", 
            "left", "left", "backspace", "enter"
        ]
    )

    print("Edição de número de telefone feita!\n")


def send_whatsapp_message(msg):
    """
    Sends a WhatsApp message through the Omni workflow.

    Args:
        msg: Text of the personalized message for the 
        customer.
    """
    print("[PROGRESS] Enviando mensagem por WhatsApp ao usuário.\n")

    def send_msg():
        nonlocal msg

        auto.write(msg)
        auto.hotkey("ctrl", "enter")

    click_on_img(
        "screenshots/omni_botao_nova_mensagem.png",
        confidence = 0.8
    )

    click_on_img(
        "screenshots/omni_texto_mostrar_caixas_entradas.png"
    )

    click_on_img(
        "screenshots/omni_caixa_entrada_loja_hesed.png"
    )

    click_on_img(
        "screenshots/omni_botao_selecionar_modelo.png"
    )

    click_on_img(
        "screenshots/omni_opcao_mensagem3.png"
    )

    click_on_img(
        "screenshots/omni_botao_enviar_mensagem2.png",
        confidence = 0.9
    )

    click_on_img(
        "screenshots/omni_link_vizualizar.png",
        confidence = 0.8
    )

    # Check if the message was successfully sent.
    # If pyautogui finds the reload icon, it proceeds.
    click_on_img(
        "screenshots/omni_botao_recarregar_mensagem.png",
        confidence = 0.85
    )

    # Check whether the private-message send option is already selected.
    try:
        auto.locateOnScreen(
            "screenshots/omni_botao_enviar_mensagem_privada_selecionado.png",
            confidence = 0.95
        )
    except ImageNotFoundException:
        click_on_img(
            "screenshots/omni_botao_mensagem_privada.png",
            confidence = 0.9
        )
        
    finally:
        click_on_img(
            "screenshots/omni_area_texto_mensagem_privada.png",
            confidence = 0.95
        )

        send_msg()

        # Add label to customer conversation
        click_on_img(
            "screenshots/omni_botao_macro.png",
            confidence = 0.95
        )

    # End of the process!
    print("Processo concluído para o código de rastreio")