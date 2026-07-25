import time
import pyautogui as auto
from pyautogui import ImageNotFoundException
from auto_functions import (
    click_on_img, run_keys_sequence
)

auto.FAILSAFE = True


def send_email_message(tracking_code):
    print("Enviando mensagem de email...")
    # 1. Access customer service web page
    click_on_img(
        "screenshots/omni_nome_aba.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_botao_enviar_mensagem.png"
    )
    time.sleep(0.5)

    auto.typewrite("diognasde06@gmail.com")
    time.sleep(1.5)
    auto.press("enter")
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_opcao_email_contato_hesed.png"
    )
    time.sleep(0.5)

    auto.typewrite("Pedido aguardando retirada")
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_texto_escrever_mensagem.png"
    )
    time.sleep(0.5)

    auto.typewrite(f"Mensagem de teste {tracking_code}")
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_botao_enviar.png",
        confidence = 0.8
    )
    time.sleep(1)

    click_on_img(
        "screenshots/omni_link_vizualizar.png",
        confidence = 0.8
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_botao_macro.png"
    )
    time.sleep(0.5)

    print("Mensagem de email enviada!")

    try:
        auto.locateOnScreen(
            "screenshots/omni_numero_indisponivel.png",
            confidence = 0.9
        )
        time.sleep(0.5)
    except ImageNotFoundException:
        print("Não encontrado número de telefone indisponível!")
        return True
    else:
        return False


def past_customer_phone_number():
    print("Editando usuário com o número de telefone...")
    # 1. Access customer service web page
    click_on_img(
        "screenshots/omni_nome_aba.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/botao_editar_contato.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/botao_editar_contato.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_campo_adicionar_numero.png"
    )
    time.sleep(0.5)

    auto.hotkey("ctrl", "v")
    time.sleep(0.5)

    run_keys_sequence(
        [
            "left", "left", "left", "left", 
            "backspace", "left", "left", "left",
            "left", "left",
            "backspace", "backspace", "backspace",
            "backspace", "backspace", "enter"
        ]
    )
    time.sleep(0.5)

    print("Edição de número de telefone feita!\n")


def send_whatsapp_message(tracking_code):
    print("Enviando mensagem por whatsapp...")
    click_on_img(
        "screenshots/omni_botao_nova_mensagem.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_texto_mostrar_caixas_entradas.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_caixa_entrada_loja_hesed.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_botao_selecionar_modelo.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_opcao_mensagem3.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_botao_enviar_mensagem2.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_link_vizualizar.png"
    )
    time.sleep(0.5)

    # Check if message has successfulfy sent
    # if pyautogui found the reload icon
    # he just press than to continues
    click_on_img(
        "screenshots/omni_botao_macro.png"
    )
    time.sleep(0.5)

    click_on_img(
        "screenshots/omni_botao_mensagem_privada.png"
    )
    time.sleep(0.5)

    # Write message
    auto.typewrite(f"Mensagem de teste {tracking_code}")
    time.sleep("0.5")
    auto.press("enter")
    time.sleep("0.5")

    # Add label to customer conversation
    click_on_img(
        "screenshots/omni_botao_macro.png"
    )
    time.sleep(0.5)

    # End of the process!
    print("Processo concluído para o código de rastreio")