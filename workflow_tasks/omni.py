import keyboard, time, pyautogui as auto, pathlib
from pyautogui import ImageNotFoundException
from workflow_tasks.auto_functions import (
    click_on_img, run_keys_sequence,
    click_on_imgs_sequence
)

auto.FAILSAFE = True
auto.PAUSE = 0.5

# Access relative path  fot images folder
imgs_path = (pathlib.Path.cwd() / "screenshots").as_posix()



def send_email_message(msg):
    """
    Sends an email message through the Omni interface.

    Args:
        msg: Content of the message to be sent to the 
        customer.

    Returns:
        True when the phone number already exists, False 
        when a new number needs to be registered.
    """
    print("Enviando mensagem de email ao usuário.\n")

    click_on_imgs_sequence(
        [
            (imgs_path + "/omni_nome_aba.png", 0.99),
            (imgs_path + "/omni_botao_enviar_mensagem.png", 0.99)
        ],interval = 0.1
    )
    
    auto.hotkey("ctrl", "v")
    time.sleep(5)
    auto.press("tab")
    auto.press("enter")
    time.sleep(1)

    found_img = click_on_img(
        imgs_path + "/omni_opcao_email_contato_hesed.png"
    )
    time.sleep(1)

    if not found_img:
        click_on_img(
            imgs_path + "/omni_botao_enviar_mensagem.png"
        )
        return False

    keyboard.write("Pedido aguardando retirada")
    time.sleep(1)

    click_on_img(
        imgs_path + "/omni_texto_escrever_mensagem.png"
    )
    time.sleep(1)

    keyboard.write(msg)
    time.sleep(3)

    click_on_imgs_sequence(
        [
            (imgs_path + "/omni_botao_enviar.png", 0.8),
            (imgs_path + "/omni_link_vizualizar.png", 0.8),
            (imgs_path + "/omni_botao_macro.png", 0.95),
            (imgs_path + "/omni_botao_abrir_conversa.png", 0.95)
        ]
    )

    auto.click(duration=0.5)
    auto.click(1350, auto.position()[1], duration=0.5)
    time.sleep(1)

    print("Mensagem de email enviada!")

    return True

def check_phone_number():
    try:
        auto.locateOnScreen(
            imgs_path + "/omni_numero_indisponivel.png",
            confidence = 0.95
        )
    except ImageNotFoundException:
        print(" Usuário já está com o telefone informado.\n")
        return True
    else:
        return False


def past_customer_phone_number():
    print(" Atualizando telefone do usuário.\n")

    click_on_imgs_sequence(
        [
            (imgs_path + "/omni_nome_aba.png", 0.99),
            (imgs_path + "/botao_editar_contato.png", 0.95),
            (imgs_path + "/omni_campo_adicionar_numero.png", 0.99)
        ]
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

    # If an image indicates the phone number already exists, move left and click
    existing_img = imgs_path + "/omni_numero_existente.png"
    try:
        found = auto.locateOnScreen(existing_img, confidence=0.8)
    except ImageNotFoundException:
        print("Edição de número de telefone feita!\n")
        return False
    else:
        # move to the left side (x) of the found image and click
        auto.click(1253, 802)
        print("Número já existe — clique realizado à esquerda.\n")

        return True


def send_whatsapp_message(msg):
    """
    Sends a WhatsApp message through the Omni workflow.

    Args:
        msg: Text of the personalized message for the 
        customer.
    """
    print("Enviando mensagem por WhatsApp ao usuário.\n")

    def send_msg():
        nonlocal msg

        keyboard.write(msg)
        time.sleep(5)
        auto.hotkey("ctrl", "enter")

    time.sleep(1)
    click_on_imgs_sequence(
        [
            (imgs_path + "/omni_botao_nova_mensagem.png", 0.8),
            (imgs_path + "/omni_texto_mostrar_caixas_entradas.png", 0.99),
            (imgs_path + "/omni_caixa_entrada_loja_hesed.png", 0.99),
            (imgs_path + "/omni_botao_selecionar_modelo.png", 0.99),
            (imgs_path + "/omni_opcao_mensagem3.png", 0.99),
            (imgs_path + "/omni_botao_enviar_mensagem2.png", 0.9),
            (imgs_path + "/omni_link_vizualizar.png", 0.8)
        ]
    )
    time.sleep(2)

    # Check if the message was successfully sent.
    # If pyautogui finds the reload icon, it proceeds.
    click_on_img(
        imgs_path + "/omni_botao_recarregar_mensagem.png",
        confidence = 0.85
    )
    time.sleep(1)

    # Check whether the private-message send option is already selected.
    try:
        auto.locateOnScreen(
            imgs_path + "/omni_botao_enviar_mensagem_privada_selecionado.png",
            confidence = 0.95
        )
    except ImageNotFoundException:
        click_on_img(
            imgs_path + "/omni_botao_mensagem_privada.png",
            confidence = 0.9
        )
        time.sleep(1)
        
    finally:
        click_on_img(
            imgs_path + "/omni_area_texto_mensagem_privada.png",
            confidence = 0.95
        )
        time.sleep(1)

        send_msg()
        time.sleep(3)

        # Add label to customer conversation
        click_on_img(
            imgs_path + "/omni_botao_macro.png",
            confidence = 0.95
        )
        time.sleep(1)

    # End of the process!